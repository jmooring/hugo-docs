---
title: Embedded partial templates
description: Hugo provides embedded partial templates for common use cases.
categories: []
keywords: []
weight: 170
aliases: [/templates/internal]
---

{{< newtemplatesystem >}}

## Disqus

> [!note]
> To override Hugo's embedded Disqus template, copy the [source code]({{% eturl disqus %}}) to a file with the same name in the `layouts/_partials` directory, then call it from your templates using the [`partial`] function:
>
> `{{ partial "disqus.html" . }}`

Hugo includes an embedded template for [Disqus], a popular commenting system for both static and dynamic websites. To effectively use Disqus, secure a Disqus "shortname" by [signing up] for the free service.

To include the embedded template:

```go-html-template
{{ partial "disqus.html" . }}
```

### Configuration {#configuration-disqus}

To use Hugo's Disqus template, first set up a single configuration value:

{{< code-toggle file=hugo >}}
[services.disqus]
shortname = 'your-disqus-shortname'
{{</ code-toggle >}}

Hugo's Disqus template accesses this value with:

```go-html-template
{{ .Site.Config.Services.Disqus.Shortname }}
```

You can also set the following in the front matter for a given piece of content:

- `disqus_identifier`
- `disqus_title`
- `disqus_url`

### Privacy {#privacy-disqus}

Adjust the relevant privacy settings in your site configuration.

{{< code-toggle config=privacy.disqus />}}

disable
: (`bool`) Whether to disable the template. Default is `false`.

## Google Analytics

> [!note]
> To override Hugo's embedded Google Analytics template, copy the [source code]({{% eturl google_analytics %}}) to a file with the same name in the `layouts/_partials` directory, then call it from your templates using the [`partial`] function:
>
> `{{ partial "google_analytics.html" . }}`

Hugo includes an embedded template supporting [Google Analytics 4].

To include the embedded template:

```go-html-template
{{ partial "google_analytics.html" . }}
```

### Configuration {#configuration-google-analytics}

Provide your tracking ID in your configuration file:

{{< code-toggle file=hugo >}}
[services.googleAnalytics]
id = "G-MEASUREMENT_ID"
{{</ code-toggle >}}

To use this value in your own template, access the configured ID with `{{ site.Config.Services.GoogleAnalytics.ID }}`.

### Privacy {#privacy-google-analytics}

Adjust the relevant privacy settings in your site configuration.

{{< code-toggle config=privacy.googleAnalytics />}}

disable
: (`bool`) Whether to disable the template. Default is `false`.

respectDoNotTrack
: (`bool`) Whether to respect the browser's "do not track" setting. Default is `false`.

## Open Graph

> [!note]
> To override Hugo's embedded Open Graph template, copy the [source code]({{% eturl opengraph %}}) to a file with the same name in the `layouts/_partials` directory, then call it from your templates using the [`partial`] function:
>
> `{{ partial "opengraph.html" . }}`

Hugo includes an embedded template for the [Open Graph protocol](https://ogp.me/), metadata that enables a page to become a rich object in a social graph.
This format is used for Facebook and some other sites.

To include the embedded template:

```go-html-template
{{ partial "opengraph.html" . }}
```

### Configuration {#configuration-open-graph}

Hugo's Open Graph template is configured using a mix of configuration settings and [front matter](/content-management/front-matter/) on individual pages.

{{< code-toggle file=hugo >}}
[params]
  description = 'Text about my cool site'
  images = ['site-feature-image.jpg']
  title = 'My cool site'
  [params.social]
  facebook_admin = 'jsmith'
[taxonomies]
  series = 'series'
{{</ code-toggle >}}

{{< code-toggle file=content/blog/my-post.md fm=true >}}
title = "Post title"
description = "Text about this post"
date = 2024-03-08T08:18:11-08:00
images = ["post-cover.png"]
audio = []
videos = []
series = []
tags = []
{{</ code-toggle >}}

Hugo uses the page title and description for the title and description metadata.
The first 6 URLs from the `images` array are used for image metadata.
If [page bundles](/content-management/page-bundles/) are used and the `images` array is empty or undefined, images with file names matching `*feature*`, `*cover*`, or `*thumbnail*` are used for image metadata.

Various optional metadata can also be set:

- Date, published date, and last modified data are used to set the published time metadata if specified.
- `audio` and `videos` are URL arrays like `images` for the audio and video metadata tags, respectively.
- The first 6 `tags` on the page are used for the tags metadata.
- The `series` taxonomy is used to specify related "see also" pages by placing them in the same series.

If using YouTube this will produce a og:video tag like `<meta property="og:video" content="url">`. Use the `https://youtu.be/<id>` format with YouTube videos (example: `https://youtu.be/qtIqKaDlqXo`).

## Pagination

See&nbsp;[details](/templates/pagination/).

## Schema

> [!note]
> To override Hugo's embedded Schema template, copy the [source code]({{% eturl schema %}}) to a file with the same name in the `layouts/_partials` directory, then call it from your templates using the [`partial`] function:
>
> `{{ partial "schema.html" . }}`

Hugo includes an embedded template to render [microdata] `meta` elements within the `head` element of your templates.

To include the embedded template:

```go-html-template
{{ partial "schema.html" . }}
```

## X (Twitter) Cards

> [!note]
> To override Hugo's embedded Twitter Cards template, copy the [source code]({{% eturl twitter_cards %}}) to a file with the same name in the `layouts/_partials` directory, then call it from your templates using the [`partial`] function:
>
> `{{ partial "twitter_cards.html" . }}`

Hugo includes an embedded template for [X (Twitter) Cards](https://developer.x.com/en/docs/twitter-for-websites/cards/overview/abouts-cards),
metadata used to attach rich media to Tweets linking to your site.

To include the embedded template:

```go-html-template
{{ partial "twitter_cards.html" . }}
```

### Configuration {#configuration-x-cards}

Hugo's X (Twitter) Card template is configured using a mix of configuration settings and [front-matter](/content-management/front-matter/) values on individual pages.

{{< code-toggle file=hugo >}}
[params]
  images = ["site-feature-image.jpg"]
  description = "Text about my cool site"
{{</ code-toggle >}}

{{< code-toggle file=content/blog/my-post.md fm=true >}}
title = "Post title"
description = "Text about this post"
images = ["post-cover.png"]
{{</ code-toggle >}}

If [page bundles](/content-management/page-bundles/) are used and the `images` array is empty or undefined, images with file names matching `*feature*`, `*cover*`, or `*thumbnail*` are used for image metadata.
If no image resources with those names are found, the images defined in the [site config](/configuration/) are used instead.
If no images are found at all, then an image-less Twitter `summary` card is used instead of `summary_large_image`.

Hugo uses the page title and description for the card's title and description fields. The page summary is used if no description is given.

Set the value of `twitter:site` in your site configuration:

{{< code-toggle file=hugo >}}
[params.social]
twitter = "GoHugoIO"
{{</ code-toggle >}}

NOTE: The `@` will be added for you

```html
<meta name="twitter:site" content="@GoHugoIO"/>
```

[`partial`]: /functions/partials/include/
[Disqus]: https://disqus.com
[Google Analytics 4]: https://support.google.com/analytics/answer/10089681
[microdata]: https://html.spec.whatwg.org/multipage/microdata.html#microdata
[signing up]: https://disqus.com/profile/signup/
