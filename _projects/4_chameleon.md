---
layout: page
title: Chameleon
description: Foundation models for fairness-aware multimodal data augmentation, improving accuracy on under-represented groups by 22% (VLDB 2024).
img: assets/img/projects/chameleon.png
importance: 4
category: research
github: https://github.com/UIC-InDeXLab/Chameleon
---

<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/projects/chameleon.png" title="Chameleon" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/chameleon.jpg" title="Chameleon logo" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

Models trained on datasets that under-represent some demographic groups perform worst on exactly those groups. **Chameleon** finds the gaps in a dataset's coverage and uses generative foundation models to synthesise the missing images. It adds as few images as possible and makes sure each one is realistic.

## Highlights

- Improves model accuracy on under-represented groups by **22% on average** on the FERET benchmark.
- Uses a rejection-sampling quality check so that generated images match the real data distribution.
- Published in the **Proceedings of the VLDB Endowment (VLDB 2024)**.

Joint work with Prof. H. V. Jagadish and Dr. Abolfazl Asudeh.
