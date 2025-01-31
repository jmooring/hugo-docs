---
title: Ref
description: Returns the absolute URL of the page with the given path, language, and output format.
categories: []
keywords: []
action:
  related:
    - methods/shortcode/RelRef
    - functions/urls/RelRef
    - functions/urls/Ref
  returnType: string
  signatures: [SHORTCODE.Ref OPTIONS]
---

{{% include "_common/ref-and-relref-options.md" %}}

## Examples

The examples below show the rendered output when visiting a page on the English language version of the site:

```go-html-template
{{ $opts := dict "path" "/books/book-1" }}
{{ .Ref $opts }} → https://example.org/en/books/book-1/

{{ $opts := dict "path" "/books/book-1" "lang" "de" }}
{{ .Ref $opts }} → https://example.org/de/books/book-1/

{{ $opts := dict "path" "/books/book-1" "lang" "de" "outputFormat" "json" }}
{{ .Ref $opts }} → https://example.org/de/books/book-1/index.json
```

{{% include "_common/ref-and-relref-error-handling.md" %}}
