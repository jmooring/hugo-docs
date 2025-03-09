---
_comment: Do not remove front matter.
---

## Scope

The method or function used to create the data structure determines its scope. For example, use the `Store` method on a `Page` object to create a data structure scoped to the page.

Scope|Method or function
:--|:--
page|[`PAGE.Store`][]
site|[`SITE.Store`][]
global|[`hugo.Store`][]
local|[`collections.NewScratch`][]
shortcode|[`SHORTCODE.Store`][]

[`PAGE.Store`]: /docs/reference/methods/page/store/
[`SHORTCODE.Store`]: /docs/reference/methods/shortcode/store/
[`SITE.Store`]: /docs/reference/methods/site/store/
[`collections.NewScratch`]: /docs/reference/functions/collections/newscratch/
[`hugo.Store`]: /docs/reference/functions/hugo/store/
