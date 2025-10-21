---
title: Configure page
linkTitle: Page
description: Configure page behavior.
categories: []
keywords: []
---

{{< new-in 0.133.0 />}}

{{% glossary-term "default sort order" %}}

Hugo uses the default sort order to determine the _next_ and _previous_ page relative to the current page when calling these methods on a `Page` object:

- [`Next`](/docs/reference/methods/page/next/) and [`Prev`](/docs/reference/methods/page/prev/)
- [`NextInSection`](/docs/reference/methods/page/nextinsection/) and [`PrevInSection`](/docs/reference/methods/page/previnsection/)

This is based on this default site configuration:

{{< code-toggle config=page />}}

To reverse the meaning of _next_ and _previous_:

{{< code-toggle file=hugo >}}
[page]
  nextPrevInSectionSortOrder = 'asc'
  nextPrevSortOrder = 'asc'
{{< /code-toggle >}}

> [!note]
> These settings do not apply to the [`Next`][] or [`Prev`][] methods on a `Pages` object.

[`Next`]: /docs/reference/methods/pages/next
[`Prev`]: /docs/reference/methods/pages/next
