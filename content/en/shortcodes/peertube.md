---
title: Peertube shortcode
linkTitle: Peertube
description: Embed a PeerTube video in your content using the peertube shortcode.
categories: []
keywords: []
---

> [!note]
> To override Hugo's embedded `peertube` shortcode, copy the [source code][] to a file with the same name in the `layouts/_shortcodes` directory.

## Example

To display a PeerTube video with this URL:

```text
https://toobnix.org/w/5jBegFpNbffA1nhmp32kqR
```

Include this in your Markdown:

```text
{{</* peertube url="https://toobnix.org/w/5jBegFpNbffA1nhmp32kqR" */>}}
```

Hugo renders this to:

{{< peertube url="https://toobnix.org/w/5jBegFpNbffA1nhmp32kqR" >}}

## Parameters

url
: (`string`) The URL of the PeerTube video.

start
: (`string`) The time, from the start of the video, when the player should start playing the video (e.g., `42s`, `6m7s`).

stop
: (`string`) The time, from the start of the video, when the player should stop playing the video (e.g., `42s`, `6m7s`).

loading
: (`string`) The loading attribute of the `iframe` element, either `eager` or `lazy`. Default is `eager`.

width
: (`int`) The width of the video in pixels. Responsive if `0`. Default is `0`.

allowFullScreen
: (`bool`) Whether to allow full screen playback. Default is `true`.

autoplay
: (`bool`) Whether to automatically play the video. Forces `mute` to `true`. Default is `false`.

controls
: (`bool`) Whether to display the video controls. Default is `true`.

displayLink
: (`bool`) Whether to display the video link. Default is `true`.

displayTitle
: (`bool`) Whether to display the video title. Default is `true`.

displayWarning
: (`bool`) Whether to display the privacy warning. Default is `true`.

loop
: (`bool`) Whether to indefinitely repeat the video. Default is `false`.

mute
: (`bool`) Whether to mute the video. Always `true` when `autoplay` is `true`. Default is `false`.

p2p
: (`bool`) Whether to enable peer-to-peer bandwidth sharing. Default is `true`.

[source code]: <{{% eturl param %}}>
