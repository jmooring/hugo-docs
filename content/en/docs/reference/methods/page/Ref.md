---
title: Ref
description: Returns the absolute URL of the page with the given logical path, language, and output format.
categories: []
keywords: []
params:
  functions_and_methods:
    returnType: string
    signatures: [PAGE.Ref OPTIONS]
---

## Usage

The `Ref` method accepts a single argument: an options map.

## Options

{{% include "/docs/_common/ref-and-relref-options.md" %}}

## Examples

The following examples show the rendered output for a page on the English version of the site:

```go-html-template
{{ $opts := dict "path" "/books/book-1" }}
{{ .Ref $opts }} → https://example.org/en/books/book-1/

{{ $opts := dict "path" "/books/book-1" "lang" "de" }}
{{ .Ref $opts }} → https://example.org/de/books/book-1/

{{ $opts := dict "path" "/books/book-1" "lang" "de" "outputFormat" "json" }}
{{ .Ref $opts }} → https://example.org/de/books/book-1/index.json
```

## Error handling

{{% include "/docs/_common/ref-and-relref-error-handling.md" %}}
