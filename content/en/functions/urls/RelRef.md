---
title: urls.RelRef
description: Returns the relative URL of the page with the given path, language, and output format.
categories: []
keywords: []
action:
  aliases: [relref]
  related:
    - functions/urls/Ref
    - methods/page/Ref
    - methods/page/RelRef
  returnType: string
  signatures:
    - urls.RelRef PAGE PATH
    - urls.RelRef PAGE OPTIONS
aliases: [/functions/relref]
---

The function takes two arguments:

1. The context of the page from which to resolve relative paths, typically the current page.
1. The [logical path](g) to the target page. A path without a leading `/` is first resolved relative to the provided context, and then relative to the rest of the site.

Alternatively, you can provide an options map instead of a path.

{{% include "_common/ref-and-relref-options.md" %}}

## Examples


```go-html-template
{{ relref . "about" }}
{{ relref . "about#anchor" }}
{{ relref . "about.md" }}
{{ relref . "about.md#anchor" }}
{{ relref . "#anchor" }}
{{ relref . "/blog/my-post" }}
{{ relref . "/blog/my-post.md" }}
```

The permalink returned is relative to the protocol+host portion of the baseURL specified in the site configuration. For example:

Code|baseURL|Permalink
:--|:--|:--
`{{ relref . "/about" }}`|`https://example.org/`|`/about/`
`{{ relref . "/about" }}`|`https://example.org/x/`|`/x/about/`

## Options

Instead of specifying a path, you can also provide an options map:

path
: (`string`) The path to the page, relative to the `content` directory. Required.

lang
: (`string`) The language (site) to search for the page. Default is the current language. Optional.

outputFormat
: (`string`) The output format to search for the page. Default is the current output format. Optional.

To return the relative permalink to another language version of a page:

```go-html-template
{{ relref . (dict "path" "about.md" "lang" "fr") }}
```

To return the relative permalink to another Output Format of a page:

```go-html-template
{{ relref . (dict "path" "about.md" "outputFormat" "rss") }}
```

{{% include "_common/ref-and-relref-error-handling.md" %}}
