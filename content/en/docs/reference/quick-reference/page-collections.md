---
title: Page collections
description: A quick reference guide to Hugo's page collections.
categories: []
keywords: []
latest_alias: /quick-reference/page-collections/
---

## Page

Use these `Page` methods when rendering lists on [section pages](g), [taxonomy pages](g), [term pages](g), and the home page.

{{% render-list-of-pages-in-section path=/docs/reference/methods/page filter=methods_page_page_collections filterType=include titlePrefix=PAGE. %}}

## Site

Use these `Site` methods when rendering lists on any page.

{{% render-list-of-pages-in-section path=/docs/reference/methods/site filter=methods_site_page_collections filterType=include titlePrefix=SITE. %}}

## Filter

Use the [`where`][] function to filter page collections.

## Sort

{{% glossary-term "default sort order" %}}

Use these methods to sort page collections by different criteria.

{{% render-list-of-pages-in-section path=/docs/reference/methods/pages filter=methods_pages_sort filterType=include titlePrefix=. titlePrefix=PAGES. %}}

## Group

Use these methods to group page collections.

{{% render-list-of-pages-in-section path=/docs/reference/methods/pages filter=methods_pages_group filterType=include titlePrefix=. titlePrefix=PAGES. %}}

[`where`]: /docs/reference/functions/collections/where/
