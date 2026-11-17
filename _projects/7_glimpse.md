---
layout: page
title: Glimpse
description: A browser extension for Overleaf and pdf.js that resolves in-paper citations and previews the cited paper in a floating panel.
img: assets/img/projects/glimpse.png
importance: 2
category: open-source
github: https://github.com/merfanian/glimpse
---

<div class="row justify-content-sm-center">
  <div class="col-sm-10 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/projects/glimpse.png" title="Glimpse" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

Reading a paper and running into `[12]` usually means scrolling to the bibliography, copying the title and searching for it. **Glimpse** removes those steps. Hover over or click a citation, and the referenced paper's abstract or PDF opens in a floating panel on the same page.

- Manifest V3 extension for **Chrome, Edge and Firefox**.
- Works in **Overleaf** and any **pdf.js** viewer.
- Resolves citations through **Crossref, arXiv and Semantic Scholar**.
