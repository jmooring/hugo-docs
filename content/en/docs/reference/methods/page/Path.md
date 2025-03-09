---
title: Path
description: Returns the logical path of the given page.
categories: []
keywords: []
params:
  functions_and_methods:
    returnType: string
    signatures: [PAGE.Path]
---

The `Path` method on a `Page` object returns the logical path of the given page, regardless of whether the page is backed by a file.

{{% glossary-term "logical path" %}}

```go-html-template
{{ .Path }} → /posts/post-1
```

The value returned by the `Path` method on a `Page` object is independent of content format, language, and URL modifiers such as the `slug` and `url` front matter fields.

## Examples

### Monolingual project

Note that the logical path is independent of content format and URL modifiers.

File path|Front matter slug|Logical path
:--|:--|:--
`content/_index.md`||`/`
`content/posts/_index.md`||`/posts`
`content/posts/post-1.md`|`foo`|`/posts/post-1`
`content/posts/post-2.html`|`bar`|`/posts/post-2`

### Multilingual site

Note that the logical path is independent of content format, language identifiers, and URL modifiers.

File path|Front matter slug|Logical path
:--|:--|:--
`content/_index.en.md`||`/`
`content/_index.de.md`||`/`
`content/posts/_index.en.md`||`/posts`
`content/posts/_index.de.md`||`/posts`
`content/posts/posts-1.en.md`|`foo`|`/posts/post-1`
`content/posts/posts-1.de.md`|`foo`|`/posts/post-1`
`content/posts/posts-2.en.html`|`bar`|`/posts/post-2`
`content/posts/posts-2.de.html`|`bar`|`/posts/post-2`

### Pages not backed by a file

The `Path` method on a `Page` object returns a value regardless of whether the page is backed by a file.

```tree
content/
└── posts/
    └── post-1.md  <-- front matter: tags = ['hugo']
```

When you build the site:

```tree
public/
├── posts/
│   ├── post-1/
│   │   └── index.html    .Page.Path = /posts/post-1
│   └── index.html        .Page.Path = /posts
├── tags/
│   ├── hugo/
│   │   └── index.html    .Page.Path = /tags/hugo
│   └── index.html        .Page.Path = /tags
└── index.html            .Page.Path = /
```

## Finding pages

These methods, functions, and shortcodes use the logical path to find the given page:

Methods|Functions|Shortcodes
:--|:--|:--
[`Site.GetPage`][]|[`urls.Ref`][]|[`ref`][]
[`Page.GetPage`][]|[`urls.RelRef`][]|[`relref`][]
[`Page.Ref`][]|&nbsp;|&nbsp;
[`Page.RelRef`][]|&nbsp;|&nbsp;
[`Shortcode.Ref`][]|&nbsp;|&nbsp;
[`Shortcode.RelRef`][]|&nbsp;|&nbsp;

> [!NOTE]
> Specify the logical path when using any of these methods, functions, or shortcodes. If you include a file extension or language identifier, Hugo will strip these values before finding the page in the logical tree.

## Logical tree

Just as file paths form a file tree, logical paths form a logical tree.

A file tree:

```tree
content/
└── s1/
    ├── p1/
    │   └── index.md
    └── p2.md
```

The same content represented as a logical tree:

```tree
content/
└── s1/
    ├── p1
    └── p2
```

A key difference between these trees is the relative path from p1 to p2:

- In the file tree, the relative path from p1 to p2 is `../p2.md`
- In the logical tree, the relative path is `p2`

> [!NOTE]
> Remember to use the logical path when using any of the methods, functions, or shortcodes listed in the previous section. If you include a file extension or language identifier, Hugo will strip these values before finding the page in the logical tree.

[`Page.GetPage`]: /docs/reference/methods/page/getpage/
[`Page.Ref`]: /docs/reference/methods/page/ref/
[`Page.RelRef`]: /docs/reference/methods/page/relref/
[`Shortcode.Ref`]: /docs/reference/methods/shortcode/ref/
[`Shortcode.RelRef`]: /docs/reference/methods/shortcode/relref/
[`Site.GetPage`]: /docs/reference/methods/site/getpage/
[`ref`]: /docs/guides/embedded-shortcodes/ref/
[`relref`]: /docs/guides/embedded-shortcodes/relref/
[`urls.Ref`]: /docs/reference/functions/urls/ref/
[`urls.RelRef`]: /docs/reference/functions/urls/relref/
