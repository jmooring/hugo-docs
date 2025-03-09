---
_comment: Do not remove front matter.
---

## Scope

The method or function used to create a scratch pad determines its scope. For example, use the `Store` method on a `Page` object to create a scratch pad scoped to the page.

Scope|Method or function
:--|:--
page|[`PAGE.Store`][]
site|[`SITE.Store`][]
global|[`hugo.Store`][]
local|[`collections.NewScratch`][]
shortcode|[`SHORTCODE.Store`][]

[`page.store`]: /docs/reference/methods/page/store
[`site.store`]: /docs/reference/methods/site/store
[`hugo.store`]: /docs/reference/functions/hugo/store
[`collections.newscratch`]: /docs/reference/functions/collections/newscratch
[`shortcode.store`]: /docs/reference/methods/shortcode/store
