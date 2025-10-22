---
layout: page
title: Chameleon
description: Foundation Models for Fairness-Aware Multi-Modal Data Augmentation
img: assets/img/chameleon.jpg
importance: 2
category: work
giscus_comments: true
github: https://github.com/UIC-InDeXLab/Chameleon
---

**Chameleon** is a fairness-aware data augmentation method that leverages foundation models to enhance coverage of minorities in multimodal datasets. This project addresses critical challenges in algorithmic fairness and data representation.

## Key Achievements

- **22% improvement** in model accuracy on under-represented groups on the FERETDB benchmark
- Novel approach to fairness-aware data augmentation using foundation models
- Published in **Proceedings of the VLDB Endowment** (2024)

## Technical Innovation

Chameleon employs advanced foundation models to generate synthetic data that specifically targets underrepresented groups, ensuring more balanced and fair training datasets for machine learning models.

## Research Impact

This work contributes to the growing field of responsible AI by providing practical solutions for addressing bias in training data, particularly in computer vision applications where demographic representation is crucial.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/1.jpg" title="Chameleon Framework" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/3.jpg" title="Fairness Metrics" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/5.jpg" title="Data Augmentation Pipeline" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Chameleon framework architecture, fairness evaluation metrics, and data augmentation pipeline.
</div>

## Publication Details

This research was published in the **Proceedings of the VLDB Endowment** and represents a significant contribution to the field of responsible data management and algorithmic fairness.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/6.jpg" title="Performance Results" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/11.jpg" title="Fairness Analysis" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Performance results showing improvement on underrepresented groups and detailed fairness analysis.
</div>
