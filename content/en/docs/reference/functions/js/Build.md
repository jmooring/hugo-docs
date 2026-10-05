---
title: js.Build
description: Returns a resource created by bundling, transpiling, tree shaking, and minifying the given JavaScript resource.
categories: []
keywords: []
params:
  functions_and_methods:
    aliases: []
    returnType: resource.Resource
    signatures: ['js.Build [OPTIONS] RESOURCE']
---

The `js.Build` function is backed by the [`evanw/esbuild`][] package, providing a mature, high-performance foundation for bundling, transformation, and minification.

Use the `js.Build` function to:

- Bundle
- Transpile (TypeScript and JSX)
- Tree shake
- Minify
- Create source maps

```go-html-template
{{ with resources.Get "js/main.js" }}
  {{$opts := dict
    "minify" (cond hugo.IsDevelopment false true)
    "sourceMap" (cond hugo.IsDevelopment "linked" "none")
  }}
  {{ with . | js.Build $opts }}
    {{ if hugo.IsDevelopment }}
      <script src="{{ .RelPermalink }}"></script>
    {{ else }}
      {{ with . | fingerprint }}
        <script src="{{ .RelPermalink }}" integrity="{{ .Data.Integrity }}" crossorigin="anonymous"></script>
      {{ end }}
    {{ end }}
  {{ end }}
{{ end }}
```

## Options

The `js.Build` function accepts an options map.

`format`
: (`string`) The output format. One of: `iife`, `cjs`, `esm`. Default is `iife`, a self-executing function, suitable for inclusion as a `<script>` tag.

`importContext`
: {{< new-in 0.165.0 />}}
: (`resource.ResourceGetter`) A [resource getter](g) to use when resolving import statements. Hugo searches this context first, matching by the path as written in the statement, before falling back to the file system.

`targetPath`
: (`string`) If not set, the source path will be used as the base target path. Note that the target path's extension may change if the target MIME type is different, e.g. when the source is TypeScript.

{{% include "/docs/_common/js-build-options.md" %}}

## Import from the assets directory

`js.Build` has full support for Hugo's [unified file system](g). You can see some simple examples in this [test project][], but in short this means that you can do this:

```js
import { hello } from 'my/module';
```

And it will resolve to the top-most `index.{js,ts,tsx,jsx}` inside `assets/my/module` in the layered file system.

```js
import { hello3 } from 'my/module/hello3';
```

Will resolve to `hello3.{js,ts,tsx,jsx}` inside `assets/my/module`.

Any imports starting with `.` are resolved relative to the current file:

```js
import { hello4 } from './lib';
```

For other files (e.g., `JSON`, `CSS`) you need to use the relative path including any extension, e.g:

```js
import * as data from 'my/module/data.json';
```

Also note the [`params`](#params) option that can be passed from template to your JS files, e.g.:

```go-html-template
{{ $js := resources.Get "js/main.js" | js.Build (dict "params" (dict "api" "https://example.org/api")) }}
```

And then in your JS file:

```js
import * as params from '@params';
```

Hugo will, by default, generate a `assets/jsconfig.json` file that maps the imports. This is useful for navigation/intellisense help inside code editors, but if you don't need/want it, you can [turn it off][].

## Import npm packages

To import a package from npm, install it with `npm install` before you build your site.

If an import does not resolve to a file in the `assets` directory, or if the importing file is outside the `assets` directory, [`esbuild`][] resolves the import. It looks for packages in `node_modules` directories, starting from the project directory, but only within the allowed paths. See [file system access](#file-system-access).

If you are developing a module that depends on npm packages, see [Node.js dependencies][] to learn how Hugo consolidates the dependencies of all imported modules into your project.

## File system access

{{% include "/docs/_common/node-permissions-imports.md" %}}

## Artifacts

{{< new-in 0.165.0 />}}

In addition to the main output, Hugo may publish other files as part of the build:

- Files copied to the output directory by esbuild's `file` loader, such as fonts and images
- A source map, when the `sourceMap` option is `external` or `linked`

The `Data` method on the returned resource exposes these files as a slice of artifacts, where each artifact provides `MediaType`, `Permalink`, and `RelPermalink` methods.

For example, to render preload links for image files published by the build:

```go-html-template
{{ with resources.Get "js/main.js" }}
  {{ with . | js.Build }}
    {{ range .Data.Artifacts }}
      {{ if eq .MediaType.MainType "image" }}
        <link rel="preload" href="{{ .RelPermalink }}" as="image" type="{{ .MediaType.Type }}">
      {{ end }}
    {{ end }}
    <script src="{{ .RelPermalink }}"></script>
  {{ end }}
{{ end }}
```

## Examples

```go-html-template
{{ $built := resources.Get "js/index.js" | js.Build "main.js" }}
```

Or with options:

```go-html-template
{{ $externals := slice "react" "react-dom" }}
{{ $defines := dict "process.env.NODE_ENV" `"development"` }}

{{ $opts := dict "targetPath" "main.js" "externals" $externals "defines" $defines }}
{{ $built := resources.Get "scripts/main.js" | js.Build $opts }}
<script src="{{ $built.RelPermalink }}" defer></script>
```

[Node.js dependencies]: /docs/concepts/modules/#nodejs-dependencies
[`esbuild`]: https://esbuild.github.io/
[`evanw/esbuild`]: https://github.com/evanw/esbuild
[test project]: https://github.com/gohugoio/hugoTestProjectJSModImports
[turn it off]: /docs/reference/configuration/build/#nojsconfiginassets
