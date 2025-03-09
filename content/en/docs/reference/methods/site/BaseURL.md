---
title: BaseURL
description: Returns the base URL as defined in your project configuration.
categories: []
keywords: []
params:
  functions_and_methods:
    returnType: string
    signatures: [SITE.BaseURL]
---

Project configuration:

{{< code-toggle file=hugo >}}
baseURL = 'https://example.org/docs/'
{{< /code-toggle >}}

Template:

```go-html-template
{{ .Site.BaseURL }} → https://example.org/docs/
```

> [!note]
> There is almost never a good reason to use this method in your templates. Its usage tends to be fragile due to misconfiguration.
>
> Use the [`absURL`][], [`absLangURL`][], [`relURL`][], or [`relLangURL`][] functions instead.

[`absLangURL`]: /docs/reference/functions/urls/absLangURL/
[`absURL`]: /docs/reference/functions/urls/absURL/
[`relLangURL`]: /docs/reference/functions/urls/relLangURL/
[`relURL`]: /docs/reference/functions/urls/relURL/
