---
title: Content types
description: Hugo is built around content organized in sections.
categories: []
keywords: []
aliases: [/content/types]
---

A **content type** is a way to organize your content. Hugo resolves the content type from either the `type` in front matter or, if not set, the first directory in the file path. e.g., `content/blog/my-first-event.md` will be of type `blog` if no `type` is set.

A content type is used to

- Determine how the content is rendered. See [template lookup order](/docs/reference/miscellaneous/template-lookup-order/) and [Content Views](/templates/content-view) for more.
- Determine which [archetype](/docs/concepts/archetypes/) template to use for new content.
