---
title: Configure content types
linkTitle: Content types
description: Configure content types.
categories: []
keywords: []
---

<!-- TODO jmooring flesh this out -->
{{< code-toggle config=contentTypes />}}

[content format](g)

{{% glossary-term "content format" %}}

For example:

{{< code-toggle file=hugo >}}
{
  "contentTypes": {
    "text/markdown": {}
  }
}
{{< /code-toggle >}}

Refer to the [content format classification table] to determine the media type.

[content format classification table]: /content-management/formats/#classification
