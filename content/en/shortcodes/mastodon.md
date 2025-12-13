---
title: Mastodon shortcode
linkTitle: Mastodon
description: Embed a Mastodon post in your content using the mastodon shortcode.
categories: []
keywords: []
---

> [!note]
> To override Hugo's embedded `mastodon` shortcode, copy the [source code][] to a file with the same name in the `layouts/_shortcodes` directory.

To display a Mastodon post with this URL:

```text
https://socel.net/@BGP/113805114250504687
```

Include this in your Markdown:

```text
{{</* mastodon url="https://socel.net/@BGP/113805114250504687" */>}}
```

Hugo renders this to:

{{< mastodon url="https://socel.net/@BGP/113805114250504687" >}}

[source code]: <{{% eturl mastodon %}}>
