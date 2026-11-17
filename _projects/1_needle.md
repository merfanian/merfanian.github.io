---
layout: page
title: Needle & NeedleDB
description: A generative-AI-powered multimodal database that answers complex natural-language image queries, with up to 3× higher mAP than CLIP.
img: assets/img/projects/needle.png
importance: 1
category: research
github: https://github.com/UIC-InDeXLab/Needle
website: https://www.cs.uic.edu/~indexlab/Needle/overview.html
---

<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/projects/needle.png" title="Needle" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/needle.png" title="Needle logo" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

Text-to-image search engines built on joint embedding models such as CLIP handle short, simple queries well. They miss once a query becomes long, compositional or full of detail. **Needle** reverses the usual direction of retrieval: it uses a generative model to _imagine_ what the answer should look like, then searches the image collection with those generated "guide images".

## Highlights

- **Up to 3× higher mean average precision** than OpenAI's CLIP on complex natural-language queries.
- Combines several vision foundation models, weighting them per query, and plugs into a vector-database index.
- **NeedleDB** turns the approach into a full system for accurate and efficient image retrieval at database scale.
- Released as an open research artifact with code, models and an [interactive demo](https://www.cs.uic.edu/~indexlab/Needle/overview.html).

## Publications

- _Needle: A Generative-AI-Powered Multimodal Database for Answering Complex Natural Language Queries_. Preprint ([arXiv:2412.00639](https://arxiv.org/abs/2412.00639)).
- _NeedleDB: A Generative-AI-Based System for Accurate and Efficient Image Retrieval using Complex Natural Language Queries_. Preprint, 2026.

Part of my Ph.D. thesis, _Generative AI for Multimodal Data Management_, advised by Dr. Abolfazl Asudeh at UIC's InDeXLab.
