---
title: Syntax highlighting styles
description: Highlight code examples using one of these styles.
categories: []
keywords: [highlight]
---

## Overview

Hugo provides several methods to add syntax highlighting to code examples:

- Use the [`transform.Highlight`][] function within your templates
- Use the [`highlight`][] shortcode with any [content format](g)
- Use [fenced code blocks][] with the Markdown content format

Regardless of method, use any of the syntax highlighting styles below.

Set the default syntax highlighting style in your project configuration:

{{< code-toggle file=hugo >}}
[markup.highlight]
style = 'monokai'
{{< /code-toggle >}}

See [configure Markup](/docs/reference/configuration/markup/#highlight).

[`transform.Highlight`]: /docs/reference/functions/transform/highlight/
[`highlight`]: /docs/guides/embedded-shortcodes/highlight/
[fenced code blocks]: /docs/concepts/syntax-highlighting/#fenced-code-blocks

## Styles

This gallery demonstrates the application of each syntax highlighting style with code examples written in different programming languages.

{{% syntax-highlighting-styles %}}
