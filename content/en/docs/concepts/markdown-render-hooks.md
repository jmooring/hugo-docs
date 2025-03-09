---
title: Introduction
description: An introduction to Markdown render hooks.
categories: []
keywords: [render hook]
weight: 10
---

<!-- TODO -->

When rendering Markdown to HTML, render hooks override the conversion. Each render hook is a template, with one template for each supported element type:

- [Blockquotes]
- [Code blocks]
- [Headings]
- [Images]
- [Links]
- [Passthrough elements]
- [Tables]

> [!note]
> Hugo supports multiple [content formats] including Markdown, HTML, AsciiDoc, Emacs Org Mode, Pandoc, and reStructuredText.
>
> The render hook capability is limited to Markdown. You cannot create render hooks for the other content formats.

For example, consider this Markdown:

```text
[Hugo](https://gohugo.io)

![kitten](kitten.jpg)
```

Without link or image render hooks, the example above is rendered to:

```html
<p><a href="https://gohugo.io">Hugo</a></p>
<p><img alt="kitten" src="kitten.jpg"></p>
```

By creating link and image render hooks, you can alter the conversion from Markdown to HTML. For example:

```html
<p><a href="https://gohugo.io" rel="external">Hugo</a></p>
<p><img alt="kitten" src="kitten.jpg" width="600" height="400"></p>
```

Each render hook is a template, with one template for each supported element type:

```text
layouts/
└── _default/
    └── _markup/
        ├── render-blockquote.html
        ├── render-codeblock.html
        ├── render-heading.html
        ├── render-image.html
        ├── render-link.html
        ├── render-passthrough.html
        └── render-table.html
```

The template lookup order allows you to create different render hooks for each page [type](g), [kind](g), language, and [output format](g). For example:

```text
layouts/
├── _default/
│   └── _markup/
│       ├── render-link.html
│       └── render-link.rss.xml
├── books/
│   └── _markup/
│       ├── render-link.html
│       └── render-link.rss.xml
└── films/
    └── _markup/
        ├── render-link.html
        └── render-link.rss.xml
```

The remaining pages in this section describe each type of render hook, including examples and the context received by each template.

[Blockquotes]: /docs/reference/markdown-render-hooks/blockquotes/
[Code blocks]: /docs/reference/markdown-render-hooks/code-blocks/
[content formats]: /docs/concepts/content-formats/
[Headings]: /docs/reference/markdown-render-hooks/headings/
[Images]: /docs/reference/markdown-render-hooks/images/
[Links]: /docs/reference/markdown-render-hooks/links/
[Passthrough elements]: /docs/reference/markdown-render-hooks/passthrough/
[Tables]: /docs/reference/markdown-render-hooks/tables/
