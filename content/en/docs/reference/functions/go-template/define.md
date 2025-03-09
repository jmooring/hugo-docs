---
title: define
description: Defines a template.
categories: []
keywords: []
params:
  functions_and_methods:
    aliases: []
    returnType:
    signatures: [define NAME]
---

Use with the [`block`] statement:

```go-html-template
{{ block "main" . }}
  {{ print "default value if 'main' template is empty" }}
{{ end }}

{{ define "main" }}
  <h1>{{ .Title }}</h1>
  {{ .Content }}
{{ end }}
```

Use with the [`partial`] function:

```go-html-template
{{ partial "inline/foo.html" (dict "answer" 42) }}

{{ define "_partials/inline/foo.html" }}
  {{ printf "The answer is %v." .answer }}
{{ end }}
```

Use with the [`template`] function:

```go-html-template
{{ template "foo" (dict "answer" 42) }}

{{ define "foo" }}
  {{ printf "The answer is %v." .answer }}
{{ end }}
```

> [!warning]
> Only [template comments] are allowed outside of the `define` and `end` statements. Avoid placing any other text, including HTML comments, outside of these boundaries. Doing so will cause rendering issues, potentially resulting in a blank page.

For example, don't do this:

```go-html-template {file="layouts/do-not-do-this.html"}
<div>This div element broke your template.</div>
{{ define "main" }}
  <h2>{{ .Title }}</h2>
  {{ .Content }}
{{ end }}
<!-- An HTML comment will break your template too. -->
```

{{% include "/docs/_common/functions/go-template/text-template.md" %}}

[template comments]: /docs/concepts/templating/#comments
[`block`]: /docs/reference/functions/go-template/block/
[`template`]: /docs/reference/functions/go-template/block/
[`partial`]: /docs/reference/functions/partials/include/
