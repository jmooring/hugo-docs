---
title: MediaType
description: Returns the media type of the given output format.
categories: []
keywords: []
params:
  functions_and_methods:
    returnType: media.Type
    signatures: [OUTPUTFORMAT.MediaType]
---

{{% include "/docs/_common/methods/output-formats/to-use-this-method.md" %}}

## Example

```go-html-template
{{ with .Site.Home.OutputFormats.Get "rss" }}
  {{ with .MediaType }}
    {{ .Type }} → application/rss+xml
    {{ .MainType }} → application
    {{ .SubType }} → rss
    {{ .Suffixes }} → [rss]
    {{ .FirstSuffix.Suffix }} → rss
  {{ end }}
{{ end }}
```

## Methods

Use these methods on the `MediaType` object.

{{% include "/docs/_common/methods/media-type/core-methods.md" %}}
