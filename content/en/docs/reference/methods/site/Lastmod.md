---
title: Lastmod
description: Returns the last modification date of site content.
keywords: []
params:
  functions_and_methods:
    returnType: time.Time
    signatures: [SITE.Lastmod]
---

The `Lastmod` method on a `Site` object returns a [`time.Time`][] value. Use this with time [functions][] and [methods][]. For example:

```go-html-template
{{ site.Lastmod | time.Format ":date_long" }} → January 31, 2024
```

[`time.Time`]: /docs/reference/data-types/#dates-and-times
[functions]: /docs/reference/functions/time/
[methods]: /docs/reference/methods/time/
