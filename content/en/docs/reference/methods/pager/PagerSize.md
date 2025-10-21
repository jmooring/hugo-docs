---
title: PagerSize
description: Returns the number of pages per pager.
categories: []
keywords: []
params:
  functions_and_methods:
    returnType: int
    signatures: [PAGER.PagerSize]
---

{{< new-in 0.128.0 />}}

The number of pages per pager is determined by the optional second argument passed to the [`Paginate`][] method, falling back to the `pagerSize` as defined in your [site configuration][].

[`Paginate`]: /docs/reference/methods/page/paginate/
[site configuration]: /docs/concepts/pagination/#configuration

```go-html-template
{{ $pages := where site.RegularPages "Type" "posts" }}
{{ $paginator := .Paginate $pages }}

{{ range $paginator.Pages }}
  <h2><a href="{{ .RelPermalink }}">{{ .LinkTitle }}</a></h2>
{{ end }}

{{ with $paginator }}
  {{ .PagerSize }}
{{ end }}
```
