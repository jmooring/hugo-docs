---
title: Render
description: Renders the given template with the given page as context.
categories: []
keywords: []
params:
  functions_and_methods:
    returnType: template.HTML
    signatures: [PAGE.Render NAME]
---

Typically used when ranging over a page collection, the `Render` method on a `Page` object renders the given [content view template][], passing the given page as context.

```go-html-template
{{ range site.RegularPages }}
  <h2><a href="{{ .RelPermalink }}">{{ .LinkTitle }}</a></h2>
  {{ .Render "summary" }}
{{ end }}
```

In the example above, note that the template ("summary") is identified by its file name without directory or extension.

Although similar to the [`partial`][] function, there are key differences.

`Render` method|`partial` function
:--|:--
The `Page` object is automatically passed to the given template. You cannot pass additional context.|You must specify the context, allowing you to pass a combination of objects, slices, maps, and scalars.
The path to the template is determined by the [content type](g).|You must specify the path to the template, relative to the `layouts/_partials` directory.

Consider this layout structure:

```tree
layouts/
├── books/
│   └── li.html   <-- content view
├── baseof.html
├── home.html
├── li.html       <-- content view
├── page.html
├── section.html
├── taxonomy.html
└── term.html
```

And this template:

```go-html-template
<ul>
  {{ range site.RegularPages.ByDate }}
    {{ .Render "li" }}
  {{ end }}
</ul>
```

When rendering content of type "books" the `Render` method calls:

```text
layouts/books/li.html
```

For all other content types the `Render` methods calls:

```text
layouts/li.html
```

[content view template]: /docs/concepts/template-types/#content-view
[`partial`]: /docs/reference/functions/partials/include/
