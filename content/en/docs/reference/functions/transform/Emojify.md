---
title: transform.Emojify 
description: Runs a string through the Emoji emoticons processor.
categories: []
keywords: []
params:
  functions_and_methods:
    aliases: [emojify]
    returnType: template.HTML
    signatures: [transform.Emojify INPUT]
---

`emojify` runs a passed string through the Emoji emoticons processor.

See the list of [emoji shortcodes][] for available emoticons.

The `emojify` function can be called in your templates but not directly in your content files by default. For emojis in content files, set [`enableEmoji`][] to `true` in your project configuration. Then you can write emoji shorthand directly into your content files;

```text
I :heart: Hugo!
```

I :heart: Hugo!

[`enableEmoji`]: /docs/reference/configuration/all/#enableemoji
[emoji shortcodes]: /docs/reference/miscellaneous/emojis
