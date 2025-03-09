---
title: Unified file system
description: Access any of the seven component types through Hugo's unified file system.
categories: []
keywords: [module,mount]
---

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

Consider a project with an imported module and a mounted arbitrary directory:

```text
project/
└── layouts/
    └── shortcodes/
        └── audio.html/
module/
└── layouts/
    └── shortcodes/
        ├── audio.html/
        └── image.html/
mount/
└── layouts/
    └── shortcodes/
        ├── audio.html/
        ├── image.html/
        └── video.html/
```

Hugo merges the `layouts` directories with top-down precedence, resulting in a unified directory containing three files:

- `audio.html` is sourced from the project
- `image.html` is sourced from the module
- `video.html` is sourced from the mount

Mounting an arbitrary directory to one of Hugo's seven component directories offers powerful capabilities, such as:

- Sharing files across multiple projects without duplication.
- Importing assets from Node.js packages as global resources.
- Bridging content translation gaps by mapping content directories between languages.

See [configuring module mounts] for details.

[configuring module mounts]: /docs/reference/configuration/modules/#mounts
