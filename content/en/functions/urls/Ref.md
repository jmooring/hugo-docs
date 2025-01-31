---
title: urls.Ref
description: Returns the absolute URL of the page with the given path, language, and output format.
categories: []
keywords: []
action:
  aliases: [ref]
  related:
    - functions/urls/RelRef
    - methods/page/Ref
    - methods/page/RelRef
  returnType: string
  signatures:
    - urls.Ref PAGE PATH
    - urls.Ref PAGE OPTIONS
aliases: [/functions/ref]
---

The function takes two arguments:

1. The context of the page from which to resolve relative paths, typically the current page.
1. The [logical path](g) to the target page. A path without a leading `/` is first resolved relative to the provided context, and then relative to the rest of the site.

Alternatively, you can provide an options map instead of a path.

{{% include "_common/ref-and-relref-options.md" %}}

## Examples

### Path

The following examples illustrate how to call the `ref` function using a logical path as the second argument.

```go-html-template
{{ ref . "about" }}
{{ ref . "about#anchor" }}
{{ ref . "about.md" }}
{{ ref . "about.md#anchor" }}
{{ ref . "#anchor" }}
{{ ref . "/blog/my-post" }}
{{ ref . "/blog/my-post.md" }}
```

### Options map

The following examples illustrate how to call the `ref` function using an options map as the second argument.  Each example shows the resulting output when rendered on a page in the English version of the site.

```go-html-template
{{ $opts := dict "path" "/books/book-1" }}
{{ ref . $opts }} → https://example.org/en/books/book-1/

{{ $opts := dict "path" "/books/book-1" "lang" "de" }}
{{ ref . $opts }} → https://example.org/de/books/book-1/

{{ $opts := dict "path" "/books/book-1" "lang" "de" "outputFormat" "json" }}
{{ ref . $opts }} → https://example.org/de/books/book-1/index.json
```

{{% include "_common/ref-and-relref-error-handling.md" %}}
