---
title: transform.Highlight
description: Renders code with a syntax highlighter.
categories: []
keywords: [highlight]
params:
  functions_and_methods:
    aliases: [highlight]
    returnType: template.HTML
    signatures: ['transform.Highlight CODE LANG [OPTIONS]']
---

The `highlight` function uses the [Chroma][] syntax highlighter, supporting over 200 languages with more than 40 [highlighting styles][].

## Arguments

The `transform.Highlight` shortcode takes three arguments.

CODE
: (`string`) The code to highlight.

LANG
: (`string`) The language of the code to highlight. Choose from one of the [supported languages][]. This value is case-insensitive.

OPTIONS
: (`map or string`) A map or comma-separated key-value pairs wrapped in quotation marks. Set default values for each option in your [project configuration][]. The key names are case-insensitive.

## Examples

```go-html-template
{{ $input := `fmt.Println("Hello World!")` }}
{{ transform.Highlight $input "go" }}

{{ $input := `console.log('Hello World!');` }}
{{ $lang := "js" }}
{{ transform.Highlight $input $lang "lineNos=table, style=api" }}

{{ $input := `echo "Hello World!"` }}
{{ $lang := "bash" }}
{{ $opts := dict "lineNos" "table" "style" "dracula" }}
{{ transform.Highlight $input $lang $opts }}
```

## Options

{{% include "/docs/_common/syntax-highlighting-options.md" %}}

[Chroma]: https://github.com/alecthomas/chroma
[highlighting styles]: /docs/reference/miscellaneous/syntax-highlighting-styles/
[project configuration]: /docs/reference/configuration/markup#highlight
[supported languages]: /docs/concepts/syntax-highlighting/#languages
