---
_comment: Do not remove front matter.
---

[`time.Time`][] values are compared by the moment they represent, regardless of time zone. To compare date strings, such as [custom date parameters][] in front matter, convert them with the [`time.AsTime`][] function first.

[`time.AsTime`]: /docs/reference/functions/time/astime/
[`time.Time`]: /docs/reference/data-types/#dates-and-times
[custom date parameters]:/docs/reference/front-matter/#parameters
