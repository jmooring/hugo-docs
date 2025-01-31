---
title: Configure deployment
linkTitle: Deployment
description:  Configure deployment.
categories: []
keywords: []
---

{{< note >}}
This configuration is only relevant when running `hugo deploy`. See&nbsp;[details](/hosting-and-deployment/hugo-deploy/).
{{< /note >}}

## Top-level options

These settings control the overall behavior of the deployment process. This is the default configuration:

{{< code-toggle file=hugo >}}
[deployment]
confirm = false
dryRun = false
force = false
invalidateCDN = true
matchers = []
maxDeletes = 256
order = []
target = ''
targets = []
workers = 10
{{< /code-toggle >}}

confirm
: (`bool`) Whether to prompt for confirmation before deploying. Default is `false`.

dryRun
: (`bool`) Whether to simulate the deployment without any remote changes. Default is `false`.

force
: (`bool`) Whether to re-upload all files. Default is `false`.

invalidateCDN
: (`bool`) Whether to invalidate the CDN cache listed in the deployment target. Default is `true`.

maxDeletes
: (`int`) The maximum number of files to delete, or `-1` to disable, Default is `256`.

matchers
: (`[]*Matcher`) A slice of [matchers](#matchers).

order
: (`[]string`) A slice of regular expressions to determine the order in which to upload files, prioritized left to right.

target
: (`bool`) The target deployment [`name`](#name). Defaults to the first one.

targets
: (`[]*Matcher`) A slice of [targets](#targets).

workers
: (`int`) The number of concurrent workers to use when uploading files. Default is `10`.

## Matchers

cacheControl
: (`string`) The caching attributes to use when serving the blob.

contentEncoding
: (`string`) The encoding used for the blob's content, if any.

contentType
: (`string`) The media type of the blob being written.

force
: (`bool`) Whether matching files should be re-uploaded. Useful when
other route-determined metadata (e.g., contentType) has changed.

gzip
: (`bool`) Whether the file should be gzipped before upload. If so, the ContentEncoding field will automatically be set to "gzip". Default is `false`.

pattern
: (`string`) The regular expression to match against paths. Matching is done against paths converted to use `/` as the path separator.

## Targets

cloudFrontDistributionID
: (`string`) The CloudFront Distribution ID, applicable if you are using the Amazon Web Services (AWS) CloudFront CDN.

exclude
: (`string`)  A [`glob`](g) pattern matching files to exclude for this target.

googleCloudCDNOrigin
: (`string`) The Google Cloud project and CDN origin to invalidate when deploying this target, specified as `<project>/<origin>`.

include
: (`string`) A [`glob`](g) pattern matching files to include for this target.

name
: (`string`) An arbitrary name for this target.

stripIndexHTML
: (`bool`) If true, any local path matching `<dir>/index.html` will be mapped to the remote path `<dir>/`. This does not affect the top-level `index.html` file, since that would result in an empty path. Default is `false`.

url
: (`string`) The destination URL for deployment.
