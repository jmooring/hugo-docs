---
title: Build in CI/CD with Docker
description: Build your project with Hugo's official Docker image, then deploy your site to GitHub Pages or GitLab Pages.
keywords: []
---

Use these instructions to build your project with Hugo's official [Docker image][] in a [CI/CD](g) pipeline, then deploy your site to GitHub Pages or GitLab Pages. Use a similar approach with other CI/CD services that can run jobs in a container. To build your project on your computer, see [build locally with Docker][].

{{% include "/docs/_common/gitignore-public.md" %}}

## Docker image

The image includes the deploy edition of Hugo, Dart Sass, Git, Go, Node.js, and npm. Each Hugo release is published with a version tag such as `v0.170.0`. See the [tagged image versions][] for a complete list.

Each image contains a fixed version of each tool. To control the version of each tool, install the tools directly as described in the [GitHub Pages][] and [GitLab Pages][] guides instead.

The CI/CD service runs your commands directly in the container. Each workflow in this guide performs these tasks:

- Runs the container as the `root` user so that it can write to the files that the service checks out.
- Configures Git to trust the repository and to leave non-ASCII characters in file paths unquoted. Without these settings, Hugo cannot read the Git information returned by the [`GitInfo`][] method.
- Installs the Node dependencies with `npm ci`.
- Saves the Hugo cache directory between builds.
- Runs commands with `sh`. The image does not include Bash.

## Prerequisites

Complete the following tasks before continuing:

1. Create a GitHub or GitLab repository for your project.
1. Create a local Git repository for your project with a [remote][] reference to your GitHub or GitLab repository.
1. Create a Hugo project within your local Git repository and test it with the `hugo server` command.
1. Commit the changes to your local Git repository and push to your GitHub or GitLab repository.

## Procedure

Step 1
: Configure your repository to deploy with a pipeline.

  GitHub Pages
  : Visit your GitHub repository. From the main menu choose **Settings** > **Pages**, then change the **Source** to `GitHub Actions`.

  GitLab Pages
  : No configuration is required.

Step 2
: Create the pipeline configuration, adjusting the image version and time zone as needed.

  GitHub Pages
  : Create a `hugo.yaml` file in the `.github/workflows` directory.

    ```yaml {file=".github/workflows/hugo.yaml" copy=true}
    name: Build and deploy
    on:
      push:
        branches:
          - main
      workflow_dispatch:
    permissions:
      contents: read
      pages: write
      id-token: write
    concurrency:
      group: pages
      cancel-in-progress: false
    defaults:
      run:
        shell: sh
    jobs:
      build:
        runs-on: ubuntu-latest
        container:
          image: ghcr.io/gohugoio/hugo:v0.170.0
          options: --user root
        env:
          # Set the build time zone
          TZ: Europe/Oslo

          # Set the build cache directory
          HUGO_CACHEDIR: ${{ github.workspace }}/.cache/hugo
        steps:
          - name: Checkout
            uses: actions/checkout@v7
            with:
              submodules: recursive
              fetch-depth: 0
              lfs: false

          - name: Setup Pages
            id: pages
            uses: actions/configure-pages@v6

          - name: Log tool versions
            run: |
              echo "Logging tool versions..."
              command -v sass > /dev/null 2>&1 && echo "Dart Sass: $(sass --version)" || echo "Dart Sass: not installed"
              command -v go > /dev/null 2>&1 && echo "Go: $(go version)" || echo "Go: not installed"
              command -v hugo > /dev/null 2>&1 && echo "Hugo: $(hugo version)" || echo "Hugo: not installed"
              command -v node > /dev/null 2>&1 && echo "Node.js: $(node --version)" || echo "Node.js: not installed"

          - name: Configure Git
            run: |
              echo "Configuring Git..."
              git config --global core.quotepath false
              git config --global --add safe.directory '*'

          - name: Fetch full Git history
            run: |
              if [ "$(git rev-parse --is-shallow-repository)" = "true" ]; then
                echo "Fetching full Git history..."
                git fetch --unshallow
              fi

          - name: Initialize Git submodules
            run: |
              if [ -f .gitmodules ]; then
                echo "Initializing Git submodules..."
                git submodule update --init --recursive
              fi

          - name: Install Node.js dependencies
            run: |
              if [ -f package-lock.json ]; then
                echo "Installing Node.js dependencies..."
                npm ci
              fi

          - name: Cache restore
            id: cache-restore
            uses: actions/cache/restore@v6
            with:
              path: ${{ github.workspace }}/.cache/hugo
              key: hugo-${{ github.run_id }}
              restore-keys: hugo-

          - name: Build
            run: |
              echo "Building the project..."
              hugo build \
                --gc \
                --minify \
                --baseURL "${{ steps.pages.outputs.base_url }}/"

          - name: Cache save
            uses: actions/cache/save@v6
            with:
              path: ${{ github.workspace }}/.cache/hugo
              key: ${{ steps.cache-restore.outputs.cache-primary-key }}

          - name: Upload artifact
            uses: actions/upload-pages-artifact@v5
            with:
              include-hidden-files: false
              path: ./public
      deploy:
        runs-on: ubuntu-latest
        needs: build
        environment:
          name: github-pages
          url: ${{ steps.deployment.outputs.page_url }}
        steps:
          - name: Deploy to GitHub Pages
            id: deployment
            uses: actions/deploy-pages@v5
    ```

  GitLab Pages
  : Create a `.gitlab-ci.yml` file in the root of your project.

    ```yaml {file=".gitlab-ci.yml" copy=true}
    variables:
      # Set the build timezone
      TZ: Europe/Oslo

      # Set the build cache directory
      HUGO_CACHEDIR: ${CI_PROJECT_DIR}/.cache/hugo

      # Set the repository clone and fetch strategy
      GIT_DEPTH: 0
      GIT_STRATEGY: clone
      GIT_SUBMODULE_STRATEGY: recursive
    cache:
      key: ${CI_COMMIT_REF_SLUG}
      fallback_keys:
        - ${CI_DEFAULT_BRANCH}
      paths:
        - .cache/hugo
    image:
      name: ghcr.io/gohugoio/hugo:v0.170.0
      entrypoint: [""]
      docker:
        user: root
    pages:
      stage: deploy
      script:
        - chmod a+x build.sh && ./build.sh
      artifacts:
        paths:
          - public
      rules:
        - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
    ```

    Then create a `build.sh` file in the root of your project.

    ```sh {file="build.sh" copy=true}
    #!/usr/bin/env sh

    #------------------------------------------------------------------------------
    # @file
    # Builds a Hugo project hosted on GitLab Pages.
    #------------------------------------------------------------------------------

    # Exit on error, undefined variables, or pipe failures
    set -euo pipefail

    # Perform cleanup
    cleanup() {
      if [ -n "${build_temp_dir:-}" ] && [ -d "${build_temp_dir}" ]; then
        rm -rf "${build_temp_dir}"
      fi
    }

    # Register the cleanup trap
    trap cleanup EXIT INT TERM

    main() {
      # Create a temporary directory
      build_temp_dir=$(mktemp -d)

      # Install utilities
      echo "Installing utilities..."
      apk add --no-cache brotli findutils gzip > /dev/null

      # Log tool versions
      echo "Logging tool versions..."
      command -v sass > /dev/null 2>&1 && echo "Dart Sass: $(sass --version)" || echo "Dart Sass: not installed"
      command -v go > /dev/null 2>&1 && echo "Go: $(go version)" || echo "Go: not installed"
      command -v hugo > /dev/null 2>&1 && echo "Hugo: $(hugo version)" || echo "Hugo: not installed"
      command -v node > /dev/null 2>&1 && echo "Node.js: $(node --version)" || echo "Node.js: not installed"

      # Configure Git
      echo "Configuring Git..."
      git config --global core.quotepath false
      git config --global --add safe.directory '*'

      # Fetch full Git history
      if [ "$(git rev-parse --is-shallow-repository)" = "true" ]; then
        echo "Fetching full Git history..."
        git fetch --unshallow
      fi

      # Initialize Git submodules
      if [ -f .gitmodules ]; then
        echo "Initializing Git submodules..."
        git submodule update --init --recursive
      fi

      # Install Node.js dependencies
      if [ -f package-lock.json ]; then
        echo "Installing Node.js dependencies..."
        npm ci
      fi

      # Build the project
      echo "Building the project..."
      hugo build --gc --minify --baseURL "${CI_PAGES_URL}"

      # Compress published files
      echo "Compressing published files..."
      find public/ -type f -regextype posix-extended -regex '.+\.(cjs|css|html|js|json|mjs|svg|txt|xml)$' -print0 > "${build_temp_dir}/files.txt"
      xargs --null --max-procs=0 --max-args=1 brotli --quality=10 --force --keep < "${build_temp_dir}/files.txt"
      xargs --null --max-procs=0 --max-args=1 gzip -9 --force --keep < "${build_temp_dir}/files.txt"
    }

    main "$@"
    ```

Step 3
: In the project configuration file in the root of your local Git repository, set the location of the image cache to the [`cacheDir`][] as shown below.

  {{< code-toggle file=hugo copy=true >}}
  [caches.images]
  dir = ':cacheDir/images'
  {{< /code-toggle >}}

  See [configure file caches][] for more information.

Step 4
: Commit the changes to your local Git repository and push to your GitHub or GitLab repository.

Step 5
: Follow the pipeline as it builds and deploys your site.

  GitHub Pages
  : From GitHub's main menu, choose **Actions**. When the workflow has finished, click the commit message. Under the deploy step, you will see a link to your live site.

  GitLab Pages
  : From your GitLab repository, navigate to **Build** > **Pipelines**. When the pipeline has passed, your site is available at `https://<YourUsername>.gitlab.io/<your-hugo-site>/`.

In the future, whenever you push a change from your local Git repository, the pipeline will rebuild and deploy your site.

## GitLab entrypoint

GitLab expects the image's entrypoint to start a shell. The image's entrypoint runs `hugo` instead, so the `entrypoint` setting in the `.gitlab-ci.yml` file clears it. Without this setting, the job fails.

## Related resources

For more information on running pipelines in a container, consult the official documentation:

- [Running jobs in a container][] (GitHub)
- [Run your CI/CD jobs in Docker containers][] (GitLab)

[Docker image]: https://github.com/gohugoio/hugo/pkgs/container/hugo
[GitHub Pages]: /docs/guides/host-and-deploy/deploy-to-github-pages/
[GitLab Pages]: /docs/guides/host-and-deploy/deploy-to-gitlab-pages/
[Run your CI/CD jobs in Docker containers]: https://docs.gitlab.com/ci/docker/using_docker_images/
[Running jobs in a container]: https://docs.github.com/en/actions/how-tos/write-workflows/choose-where-workflows-run/run-jobs-in-a-container
[`GitInfo`]: /docs/reference/methods/page/gitinfo/
[`cacheDir`]: /docs/reference/configuration/all/#cachedir
[build locally with Docker]: /docs/guides/build-locally-with-docker/
[configure file caches]: /docs/reference/configuration/caches/
[remote]: https://git-scm.com/docs/git-remote
[tagged image versions]: https://github.com/gohugoio/hugo/pkgs/container/hugo/versions?filters%5Bversion_type%5D=tagged
