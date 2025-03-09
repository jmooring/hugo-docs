---
title: Unified file system
description: Access any of the seven component types through Hugo's unified file system.
categories: []
keywords: [module,mount]
---

## Introduction

{{% glossary-term "unified file system" %}}

Component type|Component directory
:--|:--
archetypes|`archetypes`
assets|`assets`
content|`content`
data|`data`
templates|`layouts`
translation tables|`i18n`
static files|`static`

## Precedence

Consider a project with an imported module and a mounted directory:

```tree
project/
└── layouts/
    └── _shortcodes/
        └── audio.html/
module/
└── layouts/
    └── _shortcodes/
        ├── audio.html/
        └── image.html/
mount/
└── layouts/
    └── _shortcodes/
        ├── audio.html/
        ├── image.html/
        └── video.html/
```

Hugo merges the `layouts` directories with top-down precedence, resulting in a unified `layouts/shortcodes` directory containing three files:

- `audio.html` is sourced from the project
- `image.html` is sourced from the module
- `video.html` is sourced from the mount

## Merge strategy

Hugo merges component directories differently based on the component type.

Component type|Component directory|Merge strategy
:--|:--|:--
archetypes|`archetypes`|file level
assets|`assets`|file level
content|`content`|file level
data|`data`|deep merge based on object key
templates|`layouts`|file level
translation tables|`i18n`|deep merge based on object key
static files|`static`|file level

In all cases the merge precedence is top-down.

## Directory mounts

Mounting an arbitrary directory to one of Hugo's seven component directories offers powerful capabilities, such as:

- Sharing files across multiple projects without duplication.
- Importing assets from Node.js packages as global resources.
- Bridging content translation gaps by mapping content directories between languages.

See [configure modules](/docs/reference/configuration/modules/#mounts) for details.
