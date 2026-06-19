---
layout: about
title: about
permalink: /
# subtitle: <a href='#'>Affiliations</a>. Address. Contacts. Moto. Etc.

profile:
  align: right
  image: Leon_pic.jpg
  image_circular: false # crops the image to make it circular
  more_info: >


news: false # includes a list of news items
selected_papers: false # includes a list of papers marked as "selected={true}"
social: false # includes social icons at the bottom of the page
---

I am a researcher working on machine learning, with a focus on reasoning, interpretability, and alignment. I recently completed a PhD in mathematics at Harvard, where my research was in mathematical physics and topology. During that time, I also worked on quantitative research at a stealth high-frequency trading startup and on agentic AI systems as an engineering intern.

<p>
<a href="mailto:yuleonliu@math.harvard.edu">Email</a> &nbsp;/&nbsp;
<a href="https://github.com/leon2k2k2k">GitHub</a> &nbsp;/&nbsp;
<a href="https://scholar.google.com/citations?user=J7pQe_JdJKQC&hl=en">Google Scholar</a> &nbsp;/&nbsp;
<a href="/assets/Leon_CV/Leon_CV-26-06.pdf">CV (PDF)</a>
</p>

<br>

## Research Interests

My primary interest is building AI systems that reason well and that we can understand and trust. My work spans automated reasoning for mathematics, reinforcement learning for post-training language models, and interpretability and alignment. I am especially drawn to oversight: methods for understanding what a model is computing internally and steering its behavior toward what we intend. My background in mathematics shapes how I approach these problems.

<br>

## Projects

**Autonomous Mathematical Research Agent** &nbsp; <em>(private)</em><br>
An agent that attacks open problems in mathematics through generate-and-verify loops, with an external-LLM verification service and multi-model campaign orchestration. Produced a new result on an open Erdős problem and improvements on several others.<br>
[<a href="/erdos153_corrected.pdf">writeup</a>] [<a href="/erdos819.pdf">writeup</a>] [<a href="/erdos327.pdf">writeup</a>]

**Phase Transitions in Flow Language Models** &nbsp; <em>(research)</em><br>
With the Albergo lab at Harvard: studying a token-commitment phase transition in continuous simplex flows for text. The transition is sharp and geometric, and matches interpolant theory on a trained model.

**Parameter Golf (OpenAI Model Craft Challenge)** &nbsp; <em>(open source)</em><br>
An agent-assisted LLM training pipeline (frozen specs, autonomous GPU runs, post-run audits) that cut experiment iteration time roughly 5x. A recurrence-band mixing variant beat the then-SOTA on validation bits-per-byte by 3 sigma across 3 seeds.<br>
[<a href="https://github.com/openai/parameter-golf/pull/1779">PR #1779</a>] [<a href="https://github.com/openai/parameter-golf/pull/1801">PR #1801</a>]

**LLM Post-Training with GRPO / RLVR** &nbsp; <em>(research)</em><br>
Trained and evaluated Qwen2.5-3B on Countdown with GRPO/RLVR and built diagnostic evals. Outcome-only reward raised the addition/subtraction set from 25% to 87% but suppressed multiplication, a case of strategy narrowing rather than broad capability gain.

**Agent Skills** &nbsp; <em>(open source)</em><br>
A public toolkit of production-tested skills for AI coding agents (external-LLM review loops, proof-verification loops, paper reading, LaTeX writeups), usable across Claude Code, Codex, Gemini CLI, and Cursor.<br>
[<a href="https://github.com/leon2k2k2k/agent-skills">code</a>]

**Quant and Agentic Systems** &nbsp; <em>(industry)</em><br>
C++ orderbook and execution-backtesting infrastructure at a stealth high-frequency trading startup; and an LLM-driven C++ optimization pipeline (dependency-DAG analysis plus agentic implementation gated by tests and benchmarks, around 1.5x speedups) as an agentic engineering intern.

<br>

## Selected Publications

I have written around ten papers in mathematics; a few are below, and the full list is on the <a href="/publications/">papers</a> page.

**The Smith Fiber Sequence of Invertible Field Theories**<br>
A. Debray, S. K. Devalapurkar, C. Krulewski, <strong>Y. L. Liu</strong>, N. Pacheco-Tallaj, R. Thorngren<br>
Communications in Mathematical Physics, 2026 &nbsp; [<a href="https://arxiv.org/abs/2405.04649">arXiv</a>]

**A Long Exact Sequence in Symmetry Breaking**<br>
A. Debray, S. K. Devalapurkar, C. Krulewski, <strong>Y. L. Liu</strong>, N. Pacheco-Tallaj, R. Thorngren<br>
Journal of High Energy Physics, 2025 &nbsp; [<a href="https://arxiv.org/abs/2309.16749">arXiv</a>]

**A Braided Monoidal (∞,2)-Category of Soergel Bimodules**<br>
<strong>Y. L. Liu</strong>, A. Mazel-Gee, D. Reutter, C. Stroppel, P. Wedrich<br>
2024 (presented in an ICM plenary talk) &nbsp; [<a href="https://arxiv.org/abs/2401.02956">arXiv</a>]

**Constructing the Virasoro Groups from Differential Cohomology**<br>
A. Debray, <strong>Y. L. Liu</strong>, C. Weis<br>
International Mathematics Research Notices, 2023 &nbsp; [<a href="https://arxiv.org/abs/2112.10837">arXiv</a>]

<br>
