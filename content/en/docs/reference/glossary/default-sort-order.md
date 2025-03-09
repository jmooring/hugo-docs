---
title: default sort order
---

The _default sort order_ for [_page collections_](g), used when no other criteria are set, follows this priority:

  1. [`weight`][] (ascending)
  1. [`date`][] (descending)
  1. [`linkTitle`][] falling back to [`title`][] (ascending)
  1. [logical path](g) (ascending)

  [`date`]: /docs/reference/front-matter/#date
  [`linkTitle`]: /docs/reference/front-matter/#linktitle
  [`title`]: /docs/reference/front-matter/#title
  [`weight`]: /docs/reference/front-matter/#weight
