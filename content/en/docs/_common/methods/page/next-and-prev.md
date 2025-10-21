---
_comment: Do not remove front matter.
---

Hugo determines the _next_ and _previous_ page by sorting the site's collection of regular pages according to this sorting hierarchy:

Field|Precedence|Sort direction
:--|:--|:--
[`weight`][]|1|descending
[`date`][]|2|descending
[`linkTitle`][]|3|descending
[`path`][]|4|descending

[`date`]: /docs/reference/methods/page/date/
[`weight`]: /docs/reference/methods/page/weight/
[`linkTitle`]: /docs/reference/methods/page/linktitle/
[`path`]: /docs/reference/methods/page/path/

The sorted page collection used to determine the _next_ and _previous_ page is independent of other page collections, which may lead to unexpected behavior.

For example, with this content structure:

```tree
content/
├── pages/
│   ├── _index.md
│   ├── page-1.md   <-- front matter: weight = 10
│   ├── page-2.md   <-- front matter: weight = 20
│   └── page-3.md   <-- front matter: weight = 30
└── _index.md
```

And these templates:

```go-html-template {file="layouts/section.html"}
{{ range .Pages.ByWeight }}
  <h2><a href="{{ .RelPermalink }}">{{ .LinkTitle }}</a></h2>
{{ end }}
```

```go-html-template {file="layouts/page.html"}
{{ with .Prev }}
  <a href="{{ .RelPermalink }}">Previous</a>
{{ end }}

{{ with .Next }}
  <a href="{{ .RelPermalink }}">Next</a>
{{ end }}
```

When you visit page-2:

- The `Prev` method points to page-3
- The `Next` method points to page-1

To reverse the meaning of _next_ and _previous_ you can change the sort direction in your [site configuration][], or use the [`Next`][] and [`Prev`][] methods on a `Pages` object for more flexibility.

[site configuration]: /docs/reference/configuration/page/
[`Next`]: /docs/reference/methods/pages/prev/
[`Prev`]: /docs/reference/methods/pages/prev/
