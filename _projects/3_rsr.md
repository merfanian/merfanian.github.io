---
layout: page
title: RSR
description: Redundant Segment Reduction, a fast binary/ternary matrix multiplication algorithm (ICML 2025) with up to 24× speedup over NumPy.
img: assets/img/projects/rsr.png
importance: 3
category: research
github: https://github.com/UIC-InDeXLab/RSR
---

<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/projects/rsr.png" title="RSR" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/rsr.png" title="RSR logo" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

**RSR (Redundant Segment Reduction)** is a matrix multiplication algorithm for the matrices used in binary and ternary neural networks, such as 1.58-bit LLMs. Once a model is trained, its weights are fixed and take only a few distinct values. RSR uses this to preprocess the weight matrix once: it groups columns into segments and removes repeated work, which cuts the cost of every later matrix-vector product by a factor of `log(n)`.

## Highlights

- **Up to 24× faster** than an optimised NumPy baseline.
- **Up to 2.5× faster inference** on quantised LLMs.
- Published at **ICML 2025** ([arXiv:2411.06360](https://arxiv.org/abs/2411.06360)).
- Open-source Python and native C++ implementations. A kernel-level version is available in [RSR-core](https://github.com/UIC-InDeXLab/RSR-core).

Joint work with Mohsen Dehghankar and Dr. Abolfazl Asudeh.
