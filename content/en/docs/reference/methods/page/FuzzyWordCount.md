---
title: FuzzyWordCount
description: Returns the number of words in the content of the given page, rounded up to the nearest multiple of 100.
categories: []
keywords: []
params:
  functions_and_methods:
    returnType: int
    signatures: [PAGE.FuzzyWordCount]
---

```go-html-template
{{ .FuzzyWordCount }} → 200
```

To get the exact word count, use the [`WordCount`][] method.

> [!NOTE]
> For content in [CJK](g) languages, set [`hasCJKLanguage`][] to `true` in your project configuration. When enabled, Hugo applies CJK word counting rules to pages containing CJK characters. To override this behavior on a given page, set the [`isCJKLanguage`][] field in its front matter.

[`WordCount`]: /docs/reference/methods/page/wordcount/
[`hasCJKLanguage`]: /docs/reference/configuration/all/#hascjklanguage
[`isCJKLanguage`]: /docs/reference/front-matter/#iscjklanguage
