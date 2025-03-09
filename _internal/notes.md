---
title: Notes
description: Some notes related to how to structure the new docs.
weight: 1
---

## Aliases

Move the content so I know it's done, then:
1. Rename the aliases field to old_aliases
2. Create a new alias field and populate it with the prior url.

E.g.,

latest_alias: /quick-reference/glossary/
old_aliases: [/getting-started/glossary/]

When I'm all done I can create a json file with the new URL as the key, and then an array of maps, one for each aliases including the old URL. Each map would have three keys: url (string) and latest and date.

## Structural ideas

Diátaxis groups things like this:

- Explanation
- How-to guides
- Tutorials
- Reference

The Good Docs Project uses these:

- Concepts
- How-to guide
- Reference
- Tutorials

## Notes

We have a number of reference pages that include recipes (how to's) because we didn't have any place else to put them. These should be the basis for some of the how to guides. For example: math, tailwind, js build and batch.

## URL rewrites

_internal/reverse_aliases_a.json (do not append to this)
_internal/splats.txt (do not append to this)

## Where to put stuff

Need to figure out where these go, or if they get split up, or combined.

```text
public
├── content-management
│   ├── archetypes          --> archetypes
│   ├── build-options       --------------------------- guide: build-options
│   ├── comments            --------------------------- guide: comments
│   ├── content-adapters    --------------------------- guide: pages-from-data
│   ├── data-sources        --> data-sources
│   ├── diagrams            --------------------------- guide: diagrams
│   ├── formats             --> content-formats
│   ├── front-matter        --> front-matter
│   ├── image-processing    --------------------- guide: asset-pipeline-imaging
│   ├── markdown-attributes --> markdown-attributes
│   ├── mathematics         --------------------------- guide: math-in-markdown
│   ├── menus               --> menus
│   ├── multilingual        --> multilingual
│   ├── organization        --> project-structure
│   ├── page-bundles        --> project-structure
│   ├── page-resources      --> asset-pipelines
│   ├── related-content     --------------------------- guide: related-content
│   ├── sections            --> project-structure
│   ├── shortcodes          --> shortcodes
│   ├── summaries           --> content-summaries
│   ├── syntax-highlighting --> syntax-highlighting
│   ├── taxonomies          --> taxonomies
│   ├── types               --> project-structure
│   └── urls                --> url-management
├── getting-started
│   ├── directory-structure --> project-structure
│   ├── external-learning-resources ---- tutorials: external-learning-resources
│   ├── quick-start -------------------- tutorials: quick-start
│   └── usage -------------------------- tutorials: command-line-interface
├── hugo-modules --> this whole section becomes one page (modules)
│   ├── introduction
│   ├── theme-components
│   └── use-modules
├── hugo-pipes  --> this whole section becomes one page (asset-pipelines)
│   ├── bundling
│   ├── fingerprint
│   ├── introduction
│   ├── js
│   ├── minification
│   ├── postcss
│   ├── postprocess
│   ├── resource-from-string
│   ├── resource-from-template
│   └── transpile-sass-to-css
└── templates
    ├── 404
    ├── base
    ├── content-view
    ├── embedded ----------------------------- guide: using-embedded-templates
    ├── home
    ├── introduction  --> move to concept (templating.md)
    ├── lookup-order  --> this is already in the reference section
    ├── menu --------------------------------- guide: menus
    ├── pagination --------------------------- guide: pagination
    ├── partial
    ├── robots
    ├── rss
    ├── section
    ├── shortcode
    ├── single          SEE IF YOU CAN COMBINE THE REST OF THIS INTO A
    ├── sitemap         TEMPLATE TYPES PAGE
    ├── taxonomy
    ├── term
    └── types
```

<!----------- use this to make sure i've got aliases  ---->
See also: <https://github.com/gohugoio/hugoDocs/issues/2996>

A check mark says that I've put in the proper alias fields, moved or created
the contents, deleted the old page if applicable, and fixed the resulting
broken links.

- [x] about/
  - [x] features
  - [x] introduction
  - [x] license
  - [x] security
- [ ] docs/
  - [ ] concepts/
    - [x] archetypes
    - [x] asset-pipelines
    - [x] content-formats
    - [x] content-summaries
    - [x] data-sources
    - [x] front-matter
    - [x] markdown-attributes
    - [ ] menus
    - [ ] modules
    - [ ] multilingual
    - [ ] project-structure
    - [x] shortcodes
    - [x] syntax-highlighting
    - [ ] taxonomies
    - [x] template-types
    - [x] templating
    - [ ] themes
    - [x] url-management
  - [x] contribute/
    - [x] development
    - [x] documentation
    - [x] themes
  - [x] glossary
  - [ ] guides/
    - [ ] asset-pipelines/
      - [ ] css
      - [ ] imaging
      - [ ] javascript
      - [ ] sass
      - [ ] tailwind
    - [ ] authors
    - [ ] build-options
    - [x] custom-shortcodes
    - [ ] comments
    - [ ] diagrams/
      - [ ] goat
      - [ ] mermaid
    - [x] embedded-shortcodes/ 
    - [ ] embedded-templates
    - [x] host-and-deploy/
    - [ ] mathematics-in-markdown
    - [ ] menus
    - [ ] multilingual-sites
    - [ ] pages-from-data
    - [ ] pagination
    - [ ] related-content
    - [ ] taxonomies
  - [x] installation/
    - [x] bsd/
    - [x] linux/
    - [x] macos/
    - [x] windows/
  - [x] reference/
    - [x] commands/
    - [x] configuration/
    - [x] functions/
    - [x] markdown-render-hooks/
    - [x] methods/
    - [x] miscellaneous/
    - [x] quick-reference/
  - [x] troubleshooting/
    - [x] audit
    - [x] deprecation
    - [x] faq
    - [x] inspection
    - [x] logging
    - [x] performance
  - [ ] tutorials/
    - [ ] quick-start
    - [ ] command-line-interface
    - [x] external-learning-resources
    - [ ] install-themes
    - [ ] override-theme-component
- [x] news/
