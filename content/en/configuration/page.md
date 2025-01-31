---
title: Configure page
linkTitle: Page
description: Configure page behavior.
categories: []
keywords: []
---

{{< new-in 0.133.0 />}}

These methods on a `Page` object navigate to the next or previous page within a page collection, relative to the current page:

- [Next](/methods/page/next/)
- [NextInSection](/methods/page/nextinsection/)
- [Prev](/methods/page/prev/)
- [PrevInSection](/methods/page/previnsection/)

Hugo determines the _next_ and _previous_ page by sorting a page collection according to this sorting hierarchy:

Field|Precedence|Sort direction
:--|:--|:--
[`weight`]|1|descending
[`date`]|2|descending
[`linkTitle`]|3|descending
[`path`]|4|descending

[`date`]: /methods/page/date/
[`weight`]: /methods/page/weight/
[`linkTitle`]: /methods/page/linktitle/
[`path`]: /methods/page/path/

The sort direction in the table above corresponds to these default site configuration values:

{{< code-toggle config=page />}}

To sort all fields in ascending order:

{{< code-toggle file=hugo >}}
[page]
  nextPrevInSectionSortOrder = 'asc'
  nextPrevSortOrder = 'asc'
{{< /code-toggle >}}

{{< note >}}
These settings do not apply to the [`Next`] or [`Prev`] methods on a `Pages` object.

[`Next`]: /methods/pages/next
[`Prev`]: /methods/pages/next
{{< /note >}}
