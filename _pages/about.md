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

## Projects

{% comment %} hidden for now, restore later
**Autonomous Mathematical Research Agent** &nbsp; <em>(private)</em><br>
An agent that attacks open problems in mathematics through generate-and-verify loops, with an external-LLM verification service and multi-model campaign orchestration. Produced a new result on an open Erdős problem and improvements on several others.<br>
[<a href="/assets/pdf/erdos/erdos153.pdf">writeup</a>] [<a href="/assets/pdf/erdos/erdos819.pdf">writeup</a>] [<a href="/assets/pdf/erdos/erdos327.pdf">writeup</a>]

**Phase Transitions in Flow Language Models** &nbsp; <em>(research)</em><br>
With the Albergo lab at Harvard: studying a token-commitment phase transition in continuous simplex flows for text. The transition is sharp and geometric, and matches interpolant theory on a trained model.

**Parameter Golf (OpenAI Model Craft Challenge)** &nbsp; <em>(open source)</em><br>
An agent-assisted LLM training pipeline (frozen specs, autonomous GPU runs, post-run audits) that cut experiment iteration time roughly 5x. A recurrence-band mixing variant beat the then-SOTA on validation bits-per-byte by 3 sigma across 3 seeds.<br>
[<a href="https://github.com/openai/parameter-golf/pull/1779">PR #1779</a>] [<a href="https://github.com/openai/parameter-golf/pull/1801">PR #1801</a>]
{% endcomment %}

{% comment %} hidden from the web for now, restore later
<p style="margin-bottom: 1.2rem;">
  <strong>Autonomous Mathematical Research Agent</strong> &nbsp; <em>(research)</em><br>
  Built on Rethlas: a generate-and-verify pipeline that autonomously attacks open problems, with an external-LLM verification service, frozen-world / blind-source integrity enforcement, and multi-model campaign orchestration. Produced new bounds and partial results on several open Erdős problems (#153, #301, #327, #675(a), #819), each reviewed and cross-checked through the verification loop.<br>
  [<a href="/erdos/">Erdős writeups</a>]
</p>
{% endcomment %}

<div class="row align-items-center" style="margin-bottom: 1.2rem;">
  <div class="col-sm-4 mb-2 mb-sm-0">
    <a href="/posts/2026/grpo-sft-teaching-reasoning-through-arithmetic/"><img src="/assets/img/grpo/grpo_dynamics.png" class="img-fluid rounded z-depth-1" alt="GRPO training dynamics: accuracy up, response length down then up"></a>
  </div>
  <div class="col-sm-8">
    <strong>LLM Post-Training with GRPO and SFT | Reinforcement Learning</strong><br>
    Trained and evaluated Qwen2.5-3B on Countdown with GRPO/RLVR and SFT. GRPO raised add/subtract coverage from <strong>54% to 94%</strong> (pass@10), with reasoning length tracing a three-phase arc as responses became coherent: rambling at 580 characters, down to a terse 172, then settling at 287. SFT was then used to enhance multiplication, and an SFT-then-GRPO pipeline raised add/subtract <strong>pass@1 to 71%</strong> (more confident single-shot, though lower at pass@k). Multiplication set to 0%.<br>
    [<a href="/posts/2026/grpo-sft-teaching-reasoning-through-arithmetic/">writeup</a>] [<a href="https://huggingface.co/leon2k2k2k/qwen2.5-3b-countdown-grpo">models</a>] [<a href="https://huggingface.co/datasets/leon2k2k2k/countdown-mult-sft">data</a>]
  </div>
</div>

<div class="row align-items-center" style="margin-bottom: 1.2rem;">
  <div class="col-sm-4 mb-2 mb-sm-0">
    <a href="/posts/2026/rethlas-autonomous-erdos-pipeline/"><img src="/assets/img/rethlas/pipeline_flow.png" class="img-fluid rounded z-depth-1" alt="The pipeline, with the Rethlas generate-verify kernel boxed"></a>
  </div>
  <div class="col-sm-8">
    <strong>Autonomous Math Agent on Erdős Problems | AI for Math</strong><br>
    Built a pipeline that triages and attacks open Erdős problems at scale on top of the Rethlas generate-and-verify agent. It produced new bounds and partial results on five open problems (<strong>#153, #301, #327, #675(a), #819</strong>).<br>
    [<a href="/posts/2026/rethlas-autonomous-erdos-pipeline/">writeup</a>] [<a href="/erdos/">solutions</a>] [<a href="https://github.com/leon2k2k2k/Rethlas">repo</a>] [<a href="https://www.erdosproblems.com/forum/user/leon2k2k2k">erdosproblems.com</a>]
  </div>
</div>

<div class="row align-items-center" style="margin-bottom: 1.2rem;">
  <div class="col-sm-4 mb-2 mb-sm-0">
    <a href="/posts/2026/improving-one-small-model-depth-recurrence/"><img src="/assets/img/paramgolf/alpha_trajectory.png" class="img-fluid rounded z-depth-1" alt="Mixing coefficients converging from different initializations"></a>
  </div>
  <div class="col-sm-8">
    <strong>Parameter Golf: Depth-Recurrence in Small-Model Pretraining | pretraining</strong><br>
    Starting from a strong depth-recurrent small-model pretraining recipe, we learned the per-pass mixing coefficients in its loop band, found they converge to the same values regardless of initialization, and froze them as constants, <strong>improving validation BPB from 1.06549 to 1.06421, a roughly 3-sigma gain across 3 seeds</strong>, at zero size cost. We also audited a validation-data leak across the leaderboard and analyzed a sub-1.0-BPB scoring exploit. This was part of OpenAI's Parameter Golf, a six-week competition to build the best language model under a 16 MB, 10-minute budget; we wrote up the competition itself separately.<br>
    [<a href="/posts/2026/improving-one-small-model-depth-recurrence/">writeup</a>] [<a href="/posts/2026/parameter-golf-six-weeks-to-build-the-best-llm/">competition writeup</a>] [<a href="https://github.com/openai/parameter-golf/pull/1779">PR #1779</a>]
  </div>
</div>

{% comment %} hidden for now, restore later
**Agent Skills** &nbsp; <em>(open source)</em><br>
A public toolkit of production-tested skills for AI coding agents (external-LLM review loops, proof-verification loops, paper reading, LaTeX writeups), usable across Claude Code, Codex, Gemini CLI, and Cursor.<br>
[<a href="https://github.com/leon2k2k2k/agent-skills">code</a>]

**Quant and Agentic Systems** &nbsp; <em>(industry)</em><br>
C++ orderbook and execution-backtesting infrastructure at a stealth high-frequency trading startup; and an LLM-driven C++ optimization pipeline (dependency-DAG analysis plus agentic implementation gated by tests and benchmarks, around 1.5x speedups) as an agentic engineering intern.
{% endcomment %}

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
