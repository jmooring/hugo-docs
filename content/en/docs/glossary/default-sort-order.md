---
title: default sort order
---

The _default sort order_ for [_page collections_](g), used when no other criteria are set, follows this priority:

  1. [`weight`](/docs/concepts/front-matter/#weight) (ascending)
  1. [`date`](/docs/concepts/front-matter/#date) (descending)
  1. [`linkTitle`](/docs/concepts/front-matter/#linktitle) falling back to [`title`](/docs/concepts/front-matter/#title) (ascending)
  1. [logical path](g) (ascending)
