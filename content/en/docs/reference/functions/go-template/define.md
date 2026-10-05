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

## Usage

The `define` statement defines a template with the given name. Use it to fill a [`block`][] in a [base][] template, to create an inline _partial_ template that you call with the [`partials.Include`][] function, or to create a template that you call with the [`template`][] statement.

To create an inline _partial_ template, begin the name with `_partials/`.

When you create a template to call with the `template` statement, give it a name that no other template uses. If two files that do not use a base template define the same name, and their output formats have the same [`isPlainText`][] setting, Hugo uses one of the definitions in both files without warning.

## Examples

```go-html-template
{{ block "main" . }}
  {{ print "default value if 'main' template is empty" }}
{{ end }}

{{ define "main" }}
  <h1>{{ .Title }}</h1>
  {{ .Content }}
{{ end }}
```

Creating an inline _partial_ template, and calling it with the `partials.Include` function:

```go-html-template
{{ partial "inline/foo.html" (dict "answer" 42) }}

{{ define "_partials/inline/foo.html" }}
  {{ printf "The answer is %v." .answer }}
{{ end }}
```

Creating a template to call with the `template` statement:

```go-html-template
{{ template "foo" (dict "answer" 42) }}

{{ define "foo" }}
  {{ printf "The answer is %v." .answer }}
{{ end }}
```

{{% include "/docs/_common/text-template-reference.md" %}}

[`block`]: /docs/reference/functions/go-template/block/
[`isPlainText`]: /docs/reference/configuration/output-formats/#isplaintext
[`partials.Include`]: /docs/reference/functions/partials/include/
[`template`]: /docs/reference/functions/go-template/template/
[base]: /docs/concepts/template-types/#base
