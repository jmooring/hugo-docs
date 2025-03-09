---
title: Modules
description: Use modules to manage the content, layout, presentation, and behavior of your site.
categories: []
keywords: [module,mount]
latest_alias: /hugo-modules/
aliases: [/hugo-modules/,/hugo-modules/nodejs-dependencies/]
---

> [!NOTE]
> To work with modules you must install [Git][] and [Go][] 1.18 or later.

## Introduction

{{% glossary-term module %}}

- Modules can be imported in any combination or sequence.
- Module imports are recursive; importing Module A can trigger the import of Module B, and so on.
- Modules can provide configuration files and directories, subject to the constraints described in the [merge configuration settings][] section of the documentation.
- External directories, including those from non-Hugo projects, can be mounted to create a [unified file system](g).

## Import

To import a module, first initialize the project itself as a module. For example:

```sh
hugo mod init github.com/user/project
```

This will generate a [`go.mod`][] file in the project root.

> [!NOTE]
> The module name is a unique identifier rather than a hosting requirement. Using a name like `github.com/user/project` is a common convention but it does not mean you must use Git or host your code on GitHub. You can use any name you like if you do not plan to have others import your project as a module. For example, you could use a simple name such as `my-project` when you run the initialization command.

Then define one or more imports in your project configuration. This contrived example imports three modules, each containing custom shortcodes:

{{< code-toggle file=hugo >}}
[module]
  [[module.imports]]
    path = 'shortcodes-a'
  [[module.imports]]
    path = '/home/user/shortcodes-b'
  [[module.imports]]
    path = 'github.com/user/shortcodes-c'
{{< /code-toggle >}}

Import precedence is top-down. For example, if `shortcodes-a`, `shortcodes-b`, and `shortcodes-c` each define an `image` shortcode, the `image` shortcode from `shortcodes-a` will take effect.

> [!NOTE]
> If multiple modules contain data files or [translation tables](g) with identical paths, the data is deeply merged, following top-down precedence.

When you build your project, Hugo will:

1. Download the modules
1. Cache them for future use
1. Generate a [`go.sum`][] file in the project root

See [configuring module imports][] for details and options.

## Update

When you import a module, Hugo creates `go.mod` and `go.sum` files in your project root, storing version and checksum data. Clearing the module cache and rebuilding will re-download the originally imported module version, as specified in the `go.mod` file, ensuring consistent builds. Modules can be updated to other versions as needed.

To update a module to the latest version:

```sh
hugo mod get -u github.com/user/shortcodes-c
```

To update a module to a specific version:

```sh
hugo mod get -u github.com/user/shortcodes-c@v0.42.0
```

To update all modules to the latest version:

```sh
hugo mod get -u
```

To recursively update all modules to the latest version:

```sh
hugo mod get -u ./...
```

## Tidy

To remove unused entries from the `go.mod` and `go.sum` files:

```sh
hugo mod tidy
```

## Cache

Hugo caches modules to avoid repeated downloads during site builds. By default, these are stored in the `modules` directory within the [`cacheDir`][].

To clean the module cache for the current project:

```sh
hugo mod clean
```

To clean the module cache for all projects:

```sh
hugo mod clean --all
```

For details on cache location and eviction, see [configuring file caches][].

## Vendor

{{% glossary-term vendor %}}

Vendoring a module provides the benefits described above and allows for local inspection of its [components](g).

```sh
hugo mod vendor
```

This command creates a `_vendor` directory containing copies of all imported modules, used in subsequent builds. Note that:

- The `hugo mod vendor` command can be run from any module tree level.
- Modules within the `themes` directory are not vendored.
- The `--ignoreVendorPaths` flag allows you to exclude vendored modules matching a [glob pattern](g) from specific commands.

> [!IMPORTANT]
> Instead of modifying files directly within the `_vendor` directory, override them by creating a corresponding file with the same relative path in your project's root.

To remove the vendored modules, delete the `_vendor` directory.

## Replace

For local module development, use a `replace` directive in `go.mod` pointing to your local directory:

```text
replace github.com/user/module => /home/user/projects/module
```

With `hugo serve`r running, this change will trigger a configuration reload and add the local directory to the watch list. Alternatively, configure replacements by setting the [`replacements`][] parameter in your project configuration.

## Workspace

{{% glossary-term "workspace" %}}

Workspaces simplify local development of sites with modules. Create a `.work` file to define a workspace, and activate it via the [`workspace`][] configuration setting or the `HUGO_MODULE_WORKSPACE` environment variable.

A `.work` file example:

```text
go 1.26

use .
use ../my-hugo-module
```

Use the `use` directive to list module paths, including the main project (`.`). Start the Hugo server with the workspace enabled:

```sh
HUGO_MODULE_WORKSPACE=hugo.work hugo server --ignoreVendorPaths "**"
```

The `--ignoreVendorPaths` flag, used to ignore vendored dependencies (if applicable), enables live reloading of local edits within the workspace.

## Graph

To generate a [dependency graph](g), including vendoring, module replacement, and disabled module information, execute `hugo mod graph` within the target module directory. For example:

```sh
$ hugo mod graph

github.com/bep/my-modular-site github.com/bep/hugotestmods/mymounts@v1.2.0
github.com/bep/my-modular-site github.com/bep/hugotestmods/mypartials@v1.0.7
github.com/bep/hugotestmods/mypartials@v1.0.7 github.com/bep/hugotestmods/myassets@v1.0.4
github.com/bep/hugotestmods/mypartials@v1.0.7 github.com/bep/hugotestmods/myv2@v1.0.0
DISABLED github.com/bep/my-modular-site github.com/spf13/hyde@v0.0.0-20190427180251-e36f5799b396
github.com/bep/my-modular-site github.com/bep/hugo-fresh@v1.0.1
github.com/bep/my-modular-site in-themesdir
```

## Mounts

Imported modules automatically mount their component directories to Hugo's [unified file system](g). You can also manually mount any directory, including those from non-Hugo projects, to component directories.

See [configuring module mounts][] for details.

## Node.js dependencies

Hugo modules that need Node packages (e.g. for Tailwind CSS) can declare those dependencies in a standard `package.json` at the module root. Hugo consolidates dependencies from all modules into an [npm workspace][], so you only need a single `npm install` at the project level.

### Declaring dependencies

Each Hugo module declares its Node dependencies in a `package.json` file in its root directory, using the standard `dependencies` and `devDependencies` fields.

<!-- TODO
In the admonition below, remove the reference to v0.159.0 somewhere
after v0.174.0, 15 minor releases after the improvement.
-->

> [!NOTE]
> We improved this setup greatly in Hugo [v0.159.0](https://github.com/gohugoio/hugo/releases/tag/v0.159.0), but we kept the old `package.hugo.json` in the search path. Mostly to preserve as much backward compatibility as possible, but it may also be useful in some situations to reserve a separate set of Node dependencies for Hugo.

### Consolidating dependencies

Run [`hugo mod npm pack`][] to collect Node dependencies from all modules and write them to `packages/hugoautogen/package.json`. Hugo also adds a `workspaces` entry to your project's root `package.json` pointing to this auto-generated package.

The resulting project structure:

```tree
project/
├── package.json                      # your project's package.json (updated with workspaces entry)
├── packages/
│   └── hugoautogen/
│       ├── package.json              # auto-generated, contains consolidated module deps
│       └── hugo_packagemeta.json     # metadata and checksums for staleness detection
└── ...
```

<!-- TODO
In the admonition below, remove the reference to v0.159.0 somewhere
after v0.174.0, 15 minor releases after the improvement.
-->

> [!NOTE]
> In Hugo < v0.159.0 Hugo wrote the dependencies into your project's `package.json`, so if you have used `hugo mod npm pack` on your project using older Hugo versions, now is the time to clean up your project `package.json`: only direct Node dependencies should live in this file. All incoming dependencies from imported Hugo modules are written to `packages/hugoautogen/package.json`.

When merging, the topmost version wins, starting from the project. If a module declares `tailwindcss@4.1` but your project already has `tailwindcss@4.0`, the project version wins and the module dependency is excluded from the generated workspace package.

### Staleness detection

When Hugo detects that the npm dependency configuration has changed in one or more of the modules in use, you will get a warning in the console:

```text
WARN  npm dependencies are out of sync, please run "hugo mod npm pack" (you may also want to run "npm install" after that)
```

This ensures you don't forget to re-run `hugo mod npm pack` after updating module versions.

[Git]: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
[Go]: https://go.dev/doc/install
[`cacheDir`]: /docs/reference/configuration/all/#cachedir
[`go.mod`]: https://go.dev/ref/mod#go-mod-file
[`go.sum`]: https://go.dev/ref/mod#go-sum-files
[`hugo mod npm pack`]: /docs/reference/commands/hugo_mod_npm_pack/
[`replacements`]: /docs/reference/configuration/modules/#replacements
[`workspace`]: /docs/reference/configuration/modules/#workspace
[configuring file caches]: /docs/reference/configuration/caches/
[configuring module imports]: /docs/reference/configuration/modules/#imports
[configuring module mounts]: /docs/reference/configuration/modules/#mounts
[merge configuration settings]: /docs/reference/configuration/introduction/#merge-configuration-settings
[npm workspace]: https://docs.npmjs.com/cli/using-npm/workspaces
