---
title: Themes
description:
categories: []
keywords: []
---

## Introduction

{{% glossary-term theme %}}

For example, this _theme_ provides all seven component types and its own configuration file:

{{< details summary="`github.com/user/hugo-theme`" >}}

```tree
hugo-theme/
├── archetypes/
│   ├── default.md
│   └── posts.md
├── assets/
│   ├── css/
│   │   └── main.css
│   └── js/
│       └── main.js
├── content/
│   ├── posts/
│   │   ├── _index.md
│   │   ├── post-1.md
│   │   └── post-2.md
│   └── _index.md
├── data/
│   ├── incoterms.yaml
│   └── naics.json
├── i18n/
│   ├── de.toml
│   └── de.toml
├── layouts/
│   ├── _default/
│   │   ├── baseof.html
│   │   ├── home.html
│   │   ├── list.html
│   │   └── single.html
│   └── _partials/
│       ├── head/
│       │   ├── css.html
│       │   └── js.html
│       ├── footer.html
│       ├── head.html
│       ├── header.html
│       ├── menu.html
│       └── terms.html
├── static/
│   └── favicon.ico
└── hugo.toml
```

{{< /details >}}

In contrast, this _module_ provides a specific feature with limited scope through templates, a translation table, and its own configuration:

{{< details summary="`github.com/user/hugo-module`" >}}

```tree
hugo-module/
├── i18n/
│   └── en.toml
├── layouts/
│   ├── _default/
│   │   ├── _markup/
│   │   │   └── render-link.backlinks.json
│   │   └── home.backlinks.json
│   └── _partials/
│       └── backlinks.html
└── hugo.toml
```

{{< /details >}}

## Contributed themes

The Hugo community has contributed a broad range of open-source themes, designed to support diverse website needs such as:

- Organizational sites (corporate, government, nonprofit, educational)
- News, event, and project websites
- Documentation platforms
- Image galleries and portfolios
- Landing pages
- Blogs (business, professional, personal)
- Resumes and CVs

Browse the theme library at [themes.gohugo.io][].

## Installation

While theme authors' instructions should always be followed, themes are generally installed in one of three ways, listed in order of preference: as a Hugo module, as a Git submodule, or by downloading and extracting an archive.

### Hugo module

> [!note]
> To work with modules you must install [Git][] and [Go][] 1.18 or later.

#### Step 1

To install a theme as a module, first initialize the project itself as a module:

```sh
hugo mod init github.com/user/project
```

#### Step 2

Define a module import in your project configuration:

{{< code-toggle file=hugo >}}
[[module.imports]]
path = 'github.com/user/hugo-theme'
{{< /code-toggle >}}

#### Step 3

Carefully follow the theme author's configuration instructions.

#### Step 4

In the future, to update the theme to its latest version:

```sh
hugo mod get -u github.com/user/hugo-theme
```

Read more about [modules][].

### Git submodule

> [!note]
> To work with Git submodules you must install [Git][].

<!-- markdownlint-disable-next-line MD024-->
#### Step 1

To install a theme as a Git submodule, first initialize a new Git repository in the current directory:

```sh
git init
```

<!-- markdownlint-disable-next-line MD024-->
#### Step 2

Add the theme as a Git submodule:

```sh
git submodule add https://github.com/user/hugo-theme themes/hugo-theme
```

<!-- markdownlint-disable-next-line MD024-->
#### Step 3

Update your project configuration:

{{< code-toggle file=hugo >}}
theme = 'hugo-theme'
{{< /code-toggle >}}

<!-- markdownlint-disable-next-line MD024-->
#### Step 4

Carefully follow the theme author's configuration instructions.

#### Step 5

In the future, to update the theme to its latest version:

```sh
git submodule update --init --recursive
```

Read more about [Git submodules][].

### Archive

While the least preferred method, themes can be installed by downloading and extracting an archive.

<!-- markdownlint-disable-next-line MD024-->
#### Step 1

Download the archive, typically a `.zip` or `.tar.gz` file available from the theme repository. For example, archives for the latest release of the Ananke theme can be found here:

<https://github.com/theNewDynamic/gohugo-theme-ananke/releases/latest>

<!-- markdownlint-disable-next-line MD024-->
#### Step 2

Extract the archive to the `themes` directory in your project root. The directory structure should look something like this:

```tree
project/
└── themes/
    └── hugo-theme/
        ├── archetypes/
        ├── assets/
        └── layouts/
```

<!-- markdownlint-disable-next-line MD024-->
#### Step 3

Update your project configuration:

{{< code-toggle file=hugo >}}
theme = 'hugo-theme'
{{< /code-toggle >}}

<!-- markdownlint-disable-next-line MD024-->
#### Step 4

In the future, to update the theme to its latest version, repeat steps 2 and 3.

## Customization

> [!important]
> Never modify a theme or module. Override its files instead.

Never modify installed themes, regardless of the installation method. Directly editing, deleting, moving, or adding files will result in lost changes upon theme updates or reinstallation. Instead, use file overrides to customize themes.

For example, in the project below we override the theme's video shortcode by creating a file with the same path relative to the project root.

```tree
project/
├── layouts/
│   └── _shortcodes/
│       └── video.html
└── themes/
    └── hugo-theme/
        └── layouts/
            └── _shortcodes/
                └── video.html
```

[Git]: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
[Git submodules]: https://git-scm.com/book/en/v2/Git-Tools-Submodules
[Go]: https://go.dev/doc/install
[modules]: /docs/concepts/modules/
[themes.gohugo.io]: https://themes.gohugo.io/
