---
layout: page
title: BibTeX Verifier
description: In-browser verification of BibTeX entries against CrossRef and Semantic Scholar, built to catch wrong metadata and AI-hallucinated citations.
img: assets/img/projects/bibtex_verifier.png
importance: 1
category: open-source
github: https://github.com/merfanian/Bibtex-Verifier
redirect: https://merfanian.github.io/Bibtex-Verifier/
---

**BibTeX Verifier** is a small open-source web app for checking bibliography files before submission or publication. Upload a `.bib` file or paste one from Overleaf. Each entry is matched by title against academic databases, so you can spot wrong authors, years and venues, missing DOIs, duplicates, and references that don't exist in any index.

## Highlights

- **Privacy-first:** parsing and diffing happen in the browser. Only paper titles are sent to public APIs.
- **Dual lookup:** CrossRef and Semantic Scholar, for broader coverage.
- **Practical output:** field-by-field diffs, optional auto-updates, a live BibTeX preview, and download of a corrected file.
- **100+ stars** on GitHub.

The [live demo](https://merfanian.github.io/Bibtex-Verifier/) is hosted on GitHub Pages. The MIT-licensed source is on [GitHub](https://github.com/merfanian/Bibtex-Verifier).
