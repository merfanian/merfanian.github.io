---
layout: page
title: Delulu-FIM
description: The first execution-verified multilingual benchmark for detecting and mitigating code hallucinations in fill-in-the-middle completion.
img: assets/img/projects/delulu.png
importance: 2
category: research
website: https://huggingface.co/datasets/microsoft/delulu-fim-benchmark
---

<div class="row justify-content-sm-center">
  <div class="col-sm-10 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/projects/delulu.png" title="Delulu-FIM" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

Code assistants such as GitHub Copilot often complete code in **fill-in-the-middle (FIM)** mode: the model sees the code before and after the cursor and writes the missing middle. Many of their worst mistakes are _hallucinations_, meaning calls to APIs, attributes or functions that look plausible but don't exist. I built this work as a Student Researcher with Microsoft's Code&#124;AI team.

## Delulu-FIM benchmark

- The **first execution-verified, multilingual benchmark** for hallucination detection in FIM code generation.
- Every hallucinated sample is confirmed by actually running the code, not by heuristics.
- Paper: [arXiv:2605.07024](https://arxiv.org/abs/2605.07024) (preprint).
- Dataset: [microsoft/delulu-fim-benchmark](https://huggingface.co/datasets/microsoft/delulu-fim-benchmark) on Hugging Face.

## Synthetic hallucinations, real gains

<div class="row justify-content-sm-center">
  <div class="col-sm-10 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/projects/synthetic_hallucinations.png" title="Synthetic hard negatives" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

A follow-up paper uses frontier models to generate **hard negatives**: realistic but hallucinated completions. FIM models are then fine-tuned to prefer the verified answer. This improves **Qwen-7B exact match by 22%** on code-hallucination benchmarks. Preprint.

## In production

I also designed a multi-turn routing algorithm for **VS Code and GitHub CLI Auto mode**. In production, it reduced request cancellations by 9% and user dissatisfaction by 21%.
