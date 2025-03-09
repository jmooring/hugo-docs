---
title: Notes
description: Some notes related to how to structure the new docs.
weight: 1
---

Track progress here:
<https://github.com/gohugoio/hugoDocs/issues/2996>

## Notes

We have a number of reference pages that include recipes (how to's) because we didn't have any place else to put them. These should be the basis for some of the how to guides. For example: math, tailwind, js build and batch. To avoid duplicating content, MOVE these detailed examples instead of COPYING them.

## URL rewrites

_internal/reverse_aliases_a.json (do not append to this)
_internal/splats.txt (do not append to this)

## Where to put stuff

Need to figure out where these go, or if they get split up, or combined.

```tree
public
├── content-management
│   ├── build-options         ----------------> guide: build-options
│   ├── comments              ----------------> guide: comments
│   ├── content-adapters      ----------------> guide: pages-from-data
│   ├── diagrams              ----------------> guide: diagrams
│   ├── image-processing      ----------------> guide: asset-pipeline-imaging
│   ├── mathematics           ----------------> guide: math-in-markdown
│   ├── menus                 --> concept: menus
│   ├── multilingual          --> concept: multilingual
│   ├── organization          --> concept: project-structure
│   ├── page-bundles          --> concept: project-structure
│   ├── page-resources        --> concept: asset-pipelines (No. I think we need a concepts/resources page instead. Asset pipelines should describe how to use resources)
│   ├── related-content       ----------------> guide: related-content
│   ├── sections              --> concept: project-structure
│   ├── taxonomies            --> concept: taxonomies
│   └── types                 --> concept: project-structure
├── getting-started
│   ├── directory-structure   --> concept: project-structure
│   ├── quick-start           ----------------> tutorials: quick-start
│   └── usage                 ----------------> tutorials: cli?
└── templates
    ├── 404
    ├── base
    ├── content-view
    ├── embedded              ----------------> guide: embedded-templates
    ├── home
    ├── menu                  ----------------> guide: menus
    ├── pagination            ---------------->  guide: pagination
    ├── partial
    ├── robots
    ├── rss
    ├── section
    ├── shortcode
    ├── single          SEE IF YOU CAN COMBINE THE REST OF THIS INTO A
    ├── sitemap         TEMPLATE TYPES PAGE
    ├── taxonomy
    └── term
```
