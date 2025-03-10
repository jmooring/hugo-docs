---
_comment: Do not remove front matter.
---

center
: (`bool`) Whether to center the diagram within the viewport, applicable only when the viewport's aspect ratio is different than that of the SVG `viewBox` attribute. When `true`, sets the `preserveAspectRatio` attribute to `xMidYMid meet`. When `false`, sets the `preserveAspectRatio` attribute to `xMinYMin meet`. Default is `false`.

darkTheme
: (`string`) The D2 theme to use if the system is in dark mode. This value is case-insensitive. See [this list] of available themes. Default is `Dark Flagship Terrastruct`.

layoutEngine
: (`string`) The D2 layout engine to use when automatically arranging diagram elements, either `dagre` or `elk`. This value is case-insensitive. Default is `dagre`. See the [D2 documentation] for details.

lightTheme
: (`string`) The D2 theme to use if the system is in light mode or has no preference. This value is case-insensitive. See [this list] of available themes. Default is `Neutral Default`.

minify
: (`bool`) Whether to minify the SVG markup. Default is `true`.

padding
: (`int`) The number of pixels with which to pad each side of the diagram. This value must be within the bounds of 0 and 1000, inclusive. Default is `0`.

salt
: (`string`) A salt value used to generate a unique ID, preventing conflicts when embedding multiple identical diagrams in the same HTML document.

scale
: (`float`) How much to reduce or enlarge the diagram. Values less than 1 reduce the diagram, while values greater than 1 enlarge the diagram. This value must be greater than 0 and less than or equal to 100. Default is `1`.

sketch
: (`bool`) Whether to render the diagram as if sketched by hand. Default is `false`.

[this list]: https://d2lang.com/tour/themes/
[D2 documentation]: https://d2lang.com/tour/layouts
