---
title: Configure segments
linkTitle: Segments
description: Configure segments.
categories: []
keywords: []
---

{{< new-in 0.124.0 />}}

{{< note >}}
The `segments` configuration currently only applies to partitioned rendering. While this feature controls when content is rendered, it does not affect the availability of Hugo's complete object graph (sites and pages), which remains accessible at all times.
{{< /note >}}

- Each segment has zero or more exclude filters and zero or more include filters.
- Each filter contains one or more field [glob](g) matchers.
- Matchers within a filter are combined with AND logic.
- Filters within a section (exclude or include) are combined with OR logic.

The fields that can be used in the filters are:

path
: (`string`) The page's [logical path](g).

lang
: (`string`) The [page language].

kind
: (`string`) The [kind](g) of the page.

output
: (`string`) The [output format](g) of the page.

Place broad filters, such as those for language or output format, in the excludes section. For example:

{{< code-toggle file=hugo >}}
[segments.segment1]
  [[segments.segment1.excludes]]
    lang = "n*"
  [[segments.segment1.excludes]]
    lang   = "en"
    output = "rss"
  [[segments.segment1.includes]]
    kind = "{home,term,taxonomy}"
  [[segments.segment1.includes]]
    path = "{/docs,/docs/**}"
{{< /code-toggle >}}

With the above you can render only the pages in `segment1` by configuring [renderSegments] or setting the `--renderSegments` flag:


```bash
hugo --renderSegments segment1
```

Multiple segments can be configured, and the `--renderSegments` flag can take a comma separated list of segments.

This feature supports several use cases, including:

- Splitting builds of large sites.
- Enabling faster development builds by rendering only a subset of the site.
- Partial rebuilds (for example, rendering the home page and the "news section" - hourly, and the entire site weekly).
- Rendering specific output formats (for example, JSON) for purposes like pushing to a search index.

[page language]: /methods/page/language/
[renderSegments]: /configuration/all/#rendersegments
