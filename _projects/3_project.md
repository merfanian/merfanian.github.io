---
layout: page
title: RSR
description: Efficient Binary and Ternary Matrix Multiplication for Neural Network Acceleration
img: assets/img/7.jpg
importance: 3
category: work
github: https://github.com/UIC-InDeXLab/RSR
---

**RSR** (Rapid Sparse Representation) is an efficient binary and ternary matrix multiplication method designed to accelerate model inference time in neural networks. This project focuses on optimizing computational efficiency for quantized neural networks.

## Key Achievements

- **24x speedup** compared to the standard NumPy baseline
- **2.5x improvement** on Quantized LLMs
- Published in **ICML 2025** (International Conference on Machine Learning)

## Technical Innovation

RSR implements novel algorithms for binary and ternary matrix multiplication that significantly reduce computational overhead while maintaining model accuracy. The method is particularly effective for quantized neural networks where traditional floating-point operations are replaced with more efficient binary and ternary operations.

## Performance Impact

The dramatic speedup achieved by RSR makes it particularly valuable for:
- Edge computing applications with limited computational resources
- Real-time inference scenarios requiring low latency
- Large-scale deployment of quantized neural networks

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/1.jpg" title="RSR Algorithm" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/3.jpg" title="Performance Benchmarks" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/5.jpg" title="Memory Usage" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    RSR algorithm overview, performance benchmarks showing 24x speedup, and memory usage optimization.
</div>

## Research Context

This work is part of my research on efficient AI systems and algorithmic optimization, contributing to the broader goal of making AI more accessible and deployable in resource-constrained environments.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/6.jpg" title="Speedup Comparison" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/11.jpg" title="Accuracy vs Speed" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Comprehensive speedup comparison across different models and the trade-off between accuracy and computational speed.
</div>

