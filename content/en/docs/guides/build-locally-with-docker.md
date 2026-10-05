---
title: Build locally with Docker
description: Build your project and run the development server on your computer with Hugo's official Docker image.
keywords: []
---

Use these instructions to build your project and run the development server on your computer with Hugo's official [Docker image][], without installing Hugo and its related tools. To build your project with a CI/CD service, see [build in CI/CD with Docker][].

## Docker image

The image includes the deploy edition of Hugo, Dart Sass, Git, Go, Node.js, and npm. Each Hugo release is published with a version tag such as `v0.170.0`, and the `latest` tag points to the most recent release. See the [tagged image versions][] for a complete list.

When the container starts, it performs these tasks:

1. If your project directory contains a `package.json` file but no `node_modules` directory, the container runs `npm i` to install the Node dependencies.
1. The container runs `hugo` with the arguments that you pass to the `docker run` command.

To replace this behavior, create a `hugo-docker-entrypoint.sh` file in the root of your project. The container runs this file instead, passing the same arguments.

> [!WARNING]
> Your computer and the container cannot share a `node_modules` directory. Some Node packages, such as those used by Tailwind CSS, install files built for a specific operating system. Packages installed on your computer do not work in the container, and packages installed in the container do not work on your computer. If the wrong packages are installed, the build fails with an error such as `Cannot find module`.

## Prerequisites

Complete the following tasks before continuing:

1. Install [Docker Desktop][] on macOS or Windows. On Linux, install either Docker Desktop or [Docker Engine][].
1. On Windows, open PowerShell. Run the commands in this guide from PowerShell, not from the Command Prompt.

## Procedure

Step 1
: Create the Hugo cache directory on your computer.

  Linux
  : ```sh {copy=true}
    mkdir -p $HOME/.cache/hugo_cache
    ```

  macOS
  : ```sh {copy=true}
    mkdir -p $HOME/Library/Caches/hugo_cache
    ```

  Windows
  : ```sh {copy=true}
    New-Item -ItemType Directory -Force -Path $Env:LocalAppData/hugo_cache
    ```

  This step is required with Docker Engine on Linux. Otherwise Docker creates the directory with `root` as the owner, and Hugo cannot write to it.

Step 2
: Change to the root of your project.

Step 3
: If your project contains a `node_modules` directory that you created on your computer, delete the directory.

  When the container starts, it installs the Node dependencies again. This installation might change the `name` field in your `package-lock.json` file. To build your project on your computer again later, delete the `node_modules` directory, then run `npm ci`.

Step 4
: Start the development server, then visit `http://localhost:1313/` in your browser. Press `Ctrl+C` to stop the server.

  Linux
  : ```sh {copy=true}
    docker run --rm -v .:/project -v $HOME/.cache/hugo_cache:/cache -p 1313:1313 ghcr.io/gohugoio/hugo:latest server --bind="0.0.0.0"
    ```

  macOS
  : ```sh {copy=true}
    docker run --rm -v .:/project -v $HOME/Library/Caches/hugo_cache:/cache -p 1313:1313 ghcr.io/gohugoio/hugo:latest server --bind="0.0.0.0"
    ```

  Windows
  : ```sh {copy=true}
    docker run --rm -v .:/project -v $Env:LocalAppData/hugo_cache:/cache -p 1313:1313 ghcr.io/gohugoio/hugo:latest server --bind="0.0.0.0"
    ```

Step 5
: Build your project. Hugo writes the build artifacts to the `public` directory.

  Linux
  : ```sh {copy=true}
    docker run --rm -v .:/project -v $HOME/.cache/hugo_cache:/cache ghcr.io/gohugoio/hugo:latest build
    ```

  macOS
  : ```sh {copy=true}
    docker run --rm -v .:/project -v $HOME/Library/Caches/hugo_cache:/cache ghcr.io/gohugoio/hugo:latest build
    ```

  Windows
  : ```sh {copy=true}
    docker run --rm -v .:/project -v $Env:LocalAppData/hugo_cache:/cache ghcr.io/gohugoio/hugo:latest build
    ```

  To pass additional flags to Hugo, such as `--minify`, add them to the end of the command.

## Command-line flags

The `docker run` command uses these flags:

`--rm`
: Removes the container when it stops.

`-v .:/project`
: Mounts your project directory to the `/project` directory in the container.

`-v <cache directory>:/cache`
: Mounts the Hugo cache directory on your computer to the `/cache` directory in the container. Hugo stores processed images, downloaded modules, and other resources in this directory, and reuses them each time you run the container.

`-p 1313:1313`
: Publishes the container's port `1313` to the same port on your computer.

The `hugo server` command uses this flag:

`--bind="0.0.0.0"`
: Accepts connections from outside the container. Without this flag, your browser cannot reach the development server.

To build your project with the same version of each tool every time, replace `latest` with a version tag such as `v0.170.0`.

[Docker Desktop]: https://docs.docker.com/desktop/
[Docker Engine]: https://docs.docker.com/engine/install/
[Docker image]: https://github.com/gohugoio/hugo/pkgs/container/hugo
[build in CI/CD with Docker]: /docs/guides/build-in-ci-cd-with-docker/
[tagged image versions]: https://github.com/gohugoio/hugo/pkgs/container/hugo/versions?filters%5Bversion_type%5D=tagged
