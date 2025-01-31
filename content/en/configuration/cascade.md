---
title: Configure cascade
linkTitle: Cascade
description: Configure cascade.
categories: []
keywords: []
---

Configure front matter values based on [logical path](g), [page kind](g), language, or [environment](g) using cascade configurations. These configurations allow setting default values without overriding existing page-level or ancestor-defined values.

For example, the following configuration:

1. Sets `params.background` to `yosemite.jpg` for all English (`lang = 'en'`) single pages (`kind = 'page'`) within the `/articles/` section
1. Sets `params.background` to `goldenbridge.jpg` for all section pages

{{< code-toggle file=hugo >}}
[[cascade]]
[cascade.params]
background = "yosemite.jpg"
[cascade._target]
path="/articles/**"
lang="en"
kind="page"
[[cascade]]
[cascade.params]
background = "goldenbridge.jpg"
[cascade._target]
kind="section"
{{</ code-toggle >}}

Target pages using any combination of the following keywords within the `_target` section:



path
: (`string`) A [glob](g) pattern matching the page's [logical path](g). For example: `{/books/**,/films/**}`.

kind
: (`string`) A [glob](g) pattern matching the [page kind](g). For example: ` {taxonomy,term}`.

environment
: (`string`) A [glob](g) pattern matching the build [environment](g). For example: `{staging,production}`.

lang
: (`string`) A [glob](g) pattern matching the page language. For example: `{en,sv}`.



{{< note >}}
Cascading behavior can also be configured within a page's front matter to, for example, propagate a value down to the descendants of a section page. See&nbsp;[details](/content-management/front-matter/#cascade-1).
{{< /note >}}
