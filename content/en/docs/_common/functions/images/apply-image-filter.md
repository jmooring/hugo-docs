---
_comment: Do not remove front matter.
---

Apply the filter using the [`images.Filter`][] function:

[`images.Filter`]: /docs/reference/functions/images/filter/

```go-html-template
{{ with resources.Get "images/original.jpg" }}
  {{ with . | images.Filter $filter }}
    <img src="{{ .RelPermalink }}" width="{{ .Width }}" height="{{ .Height }}" alt="">
  {{ end }}
{{ end }}
```

You can also apply the filter using the [`Filter`][] method on a `Resource` object:

[`Filter`]: /docs/reference/methods/resource/filter/

```go-html-template
{{ with resources.Get "images/original.jpg" }}
  {{ with .Filter $filter }}
    <img src="{{ .RelPermalink }}" width="{{ .Width }}" height="{{ .Height }}" alt="">
  {{ end }}
{{ end }}
```
