---
title: Template lookup order
description: Hugo selects a page's template based on several attributes, and their combination defines the template's specificity.
keywords: []
latest_alias: /templates/lookup-order/
---

{{< newtemplatesystem >}}

## Selection logic

The following attributes influence Hugo's template selection for a page.

Page kind
: Hugo uses the [page kind](g) to determine the template base name. For page kinds offering multiple template base names, this table lists them in order of specificity.

  Page kind|Template base names
  :--|:--
  `home`|`index`,`home`,`list`
  `page`|`single`
  `section`|`section`,`list`
  `taxonomy`|`terms`,`taxonomy`,`list`
  `term`|`term`,`taxonomy`,`list`

Layout
: The value of the [`layout`][] front matter field, if any.

Output format
: An [output format](g) has both a name (e.g., `rss`) and a [media type](g) (e.g., `application/rss+xml`). The media type is associated with one or more suffixes (e.g., `xml`, `rss`). Hugo considers both the name and the _first_ suffix when selecting a template. For example, assuming there are no higher-precedence matches, Hugo will select this template for the `rss` output of a `section` page:

  ```text
  layouts/_default/section.rss.xml
  ```

  While the above is preferable for clarity and specificity, you can omit the output format for brevity:

  ```text
  layouts/_default/section.xml
  ```

Language
: Language tags in template names increase specificity. For instance, `section.fr.rss.xml` is more specific than `section.rss.xml`.

Content type
: The page's [content type](g).

Section
: The section containing the page.

> [!note]
> Hugo chooses the correct template by checking `layout` directories in your project and any imported modules, including themes, and picking the most specific one.

[`layout`]: /docs/reference/front-matter/#layout

## Target a template

You cannot change the lookup order to target a content page, but you can change a content page to target a template. Specify `type`, `layout`, or both in front matter.

Consider this content structure:

```tree
content/
├── about.md
└── contact.md
```

Files in the root of the `content` directory have a [content type](g) of `page`. To render these pages with a unique template, create a matching subdirectory:

```tree
layouts/
└── page/
    └── single.html
```

But the contact page probably has a form and requires a different template. In the front matter specify `layout`:

{{< code-toggle file=content/contact.md fm=true >}}
title = 'Contact'
layout = 'contact'
{{< /code-toggle >}}

Then create the template for the contact page:

```tree
layouts/
└── page/
    └── contact.html  <-- renders contact.md
    └── single.html   <-- renders about.md
```

As a content type, the word `page` is vague. Perhaps `miscellaneous` would be better. Add `type` to the front matter of each page:

{{< code-toggle file=content/about.md fm=true >}}
title = 'About'
type = 'miscellaneous'
{{< /code-toggle >}}

{{< code-toggle file=content/contact.md fm=true >}}
title = 'Contact'
type = 'miscellaneous'
layout = 'contact'
{{< /code-toggle >}}

Now place the layouts in the corresponding directory:

```tree
layouts/
└── miscellaneous/
    └── contact.html  <-- renders contact.md
    └── single.html   <-- renders about.md
```
