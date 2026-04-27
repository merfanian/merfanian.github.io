---
layout: page
title: BibTeX Verifier
description: In-browser verification of BibTeX entries against CrossRef and Semantic Scholar
importance: 1
category: fun
github: https://github.com/merfanian/Bibtex-Verifier
redirect: https://merfanian.github.io/Bibtex-Verifier/
---

**BibTeX Verifier** is a small open-source web app for checking bibliography files before submission or publication. You upload a `.bib` file or paste from Overleaf; each entry is matched by title to academic databases so you can spot wrong authors, years, venues, missing DOIs, duplicates, and references that do not exist in any index.

## Highlights

- **Privacy-first:** parsing and diffing happen in the browser; only paper titles are queried against public APIs.
- **Dual lookup:** CrossRef and Semantic Scholar for broader coverage.
- **Practical output:** field-by-field diffs, optional auto-updates, live BibTeX preview, and download of a corrected file.

The [live demo](https://merfanian.github.io/Bibtex-Verifier/) is hosted on GitHub Pages; source is MIT-licensed on [GitHub](https://github.com/merfanian/Bibtex-Verifier).
