---
title: WordCount
description: Returns the number of words in the content of the given page.
categories: []
keywords: []
params:
  functions_and_methods:
    returnType: int
    signatures: [PAGE.WordCount]
---

```go-html-template
{{ .WordCount }} → 103
```

To round up to the nearest multiple of 100, use the [`FuzzyWordCount`][] method.

> [!NOTE]
> For content in [CJK](g) languages, set [`hasCJKLanguage`][] to `true` in your project configuration. When enabled, Hugo applies CJK word counting rules to pages containing CJK characters. To override this behavior on a given page, set the [`isCJKLanguage`][] field in its front matter.

[`FuzzyWordCount`]: /docs/reference/methods/page/fuzzywordcount/
[`hasCJKLanguage`]: /docs/reference/configuration/all/#hascjklanguage
[`isCJKLanguage`]: /docs/reference/front-matter/#iscjklanguage
