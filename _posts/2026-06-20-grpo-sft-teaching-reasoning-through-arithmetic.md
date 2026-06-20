---
layout: post
title: GRPO, SFT, and teaching reasoning through arithmetic
date: 2026-06-20
description: What GRPO and SFT can and cannot teach a 3B model about arithmetic reasoning, measured on the Countdown task.
tags: reinforcement-learning, reasoning, GRPO, SFT
categories: machine-learning
toc:
  beginning: true
---

<style>
.post-content table, article table, table { margin-left:auto; margin-right:auto; border-collapse:collapse; }
.post-content table th, .post-content table td, article table th, article table td, table th, table td { border:1px solid rgba(128,128,128,0.35); padding:6px 14px; }
.post-content table thead th, article table thead th, table thead th { border-bottom:2px solid rgba(128,128,128,0.6); }
.post-content table tbody tr:nth-child(even), article table tbody tr:nth-child(even), table tbody tr:nth-child(even) { background:rgba(128,128,128,0.08); }
</style>

<p style="text-align:left"><strong>Models and data on Hugging Face:</strong> <a href="https://huggingface.co/leon2k2k2k/qwen2.5-3b-countdown-grpo">GRPO model</a>&nbsp;&nbsp;·&nbsp;&nbsp;<a href="https://huggingface.co/leon2k2k2k/qwen2.5-3b-countdown-sft-grpo">SFT-then-GRPO model</a>&nbsp;&nbsp;·&nbsp;&nbsp;<a href="https://huggingface.co/datasets/leon2k2k2k/countdown-mult-sft">SFT dataset</a></p>

## What can the base model already do?

How can we teach a 3-billion-parameter model to reason about arithmetic? Solving these problems
takes search. You try combinations and backtrack when they miss.

We test this on Countdown, a task harder than the usual GSM8K word problems that forces exactly
that kind of search. Each problem gives you three or four numbers and a target, and you have to
write an equation that uses each number exactly once and equals the target. Some are easy and
need only addition and subtraction, for example [67, 69, 69] -> 71 with 69 + 69 - 67. Others
genuinely require a multiply or a divide, for example [48, 13, 10] -> 82 with 13 * 10 - 48, or
with four numbers [27, 39, 26, 68] -> 29 with 68 * (27 - 26) - 39.

We separate the problems along two axes: whether they have three or four input numbers, and whether they need multiplication or division (otherwise they use only addition and subtraction). That gives four types.

The base model that we start with is [Qwen2.5-3B-Base](https://huggingface.co/Qwen/Qwen2.5-3B), evaluated with no
fine-tuning of any kind. We score it on a fixed set of 300 held-out problems, 150 add/sub and
150 needs-mult, with both three- and four-number problems in each. The model is asked to reason inside `<think> </think>` tags and put its final equation
inside `<answer> </answer>` tags, like this:

```
<think> 69 + 69 = 138, and 138 - 67 = 71 </think>
<answer> 69 + 69 - 67 = 71 </answer>
```

We grade each response on two things. Format asks only whether there is a parseable equation in
the `<answer>` tags. Correctness means the equation must use each given number exactly
once and actually evaluate to the target. Note that correctness implies format. For
each problem we draw 10 samples at temperature 0.7 and report pass@k: pass@1 is a single shot,
pass@10 is whether any of the 10 tries is correct.

<div style="text-align:center;margin:1.4em 0"><img src="/assets/img/grpo/passk_base.png" alt="Base model pass@k: add/sub climbs to 54%, multiplication stays near the floor" style="max-width:540px;width:100%;height:auto;border-radius:6px"></div>

*Figure: base model (Qwen2.5-3B) pass@k (k = 1 to 10). Add/sub coverage climbs to 54%;
problems that need a multiply stay pinned near 5%.*

We see that, given enough tries, the base model solves more than half
the add/sub problems, but on the problems that need a multiply it barely leaves the floor.
Breaking it down by problem size sharpens the picture:

| cell                  | pass@1 | pass@10 |
|-----------------------|-------:|--------:|
| add/sub, 3 numbers    | 12.9% | 73.4% |
| add/sub, 4 numbers    |  3.4% | 21.4% |
| needs-mult, 3 numbers |  1.5% | 13.5% |
| needs-mult, 4 numbers |  0.0% |  0.0% |

Our goal is to teach it to reason via reinforcement learning, following the recipe behind
[DeepSeek-R1](https://arxiv.org/abs/2501.12948): GRPO with a verifiable reward. We start there.

## What does GRPO actually learn?

We follow the R1-Zero recipe, reproduced on Countdown by [TinyZero](https://github.com/Jiayi-Pan/TinyZero)
and [nano-aha-moment](https://github.com/McGill-NLP/nano-aha-moment). Here we perform RL via [GRPO](https://arxiv.org/abs/2402.03300) directly from the base model. Note that GRPO normalizes the advantage within a group of G rollouts per problem. The reward is
a script: 1.0 for a well-formed `<think> </think> <answer> </answer>`, plus 1.0 if the equation uses
each number once and equals the target. We train on one H100 with G = 4, learning rate 1e-6, KL
0.001, temperature 1.0, a 1024-token budget, for 300 iterations.

Before training, about half the base model's responses run out of tokens with no answer. A typical
one, on [28, 88, 30, 56] -> 44:

```
I start with 28. I can subtract 24 from it to get 4 ... the equation is: 28 - 24 + 4 = 44. </answer>
=====
=====      (repeats about 190 times until the token limit)
=====
```

GRPO fixes this fast: by iteration 300 it returns a well-formed answer 99% of the time (up from
47%), and the run-outs nearly vanish (39% to 4%).

### How the reasoning changes over training

The accuracy curve is steady, but the reasoning is not. Track the response length and it moves
through three phases.

<div style="text-align:center;margin:1.4em 0"><img src="/assets/img/grpo/grpo_dynamics.png" alt="GRPO training dynamics: overall pass@10 rises while mean response length falls then rises" style="max-width:540px;width:100%;height:auto;border-radius:6px"></div>

*Figure: overall pass@10 (left axis) rises while mean response length (right axis) falls to a
minimum at iteration 200, then rises again.*

We can see the changes through a specific example: [84, 32, 47] -> 69. The base rambles and fabricates,
inventing numbers it was never given:

> "...multiply 32 by 2 ... (47 - 32) / 3 = 5 ... 32 * 2 + (47 - 32) / 3 = 69"  (664 chars, wrong)

By iteration 100 it is clean, direct, and correct:

> "add 84 and 32, we get 116. Then subtract 47, we get 69. So 84 + 32 - 47 = 69."

By iteration 200, the length minimum, it has cut too far. The reasoning is choppy, and here it
lands on the wrong equation:

> "84 - 32 = 52. Then add 47 to get 99. Now subtract 32 to get 67 ... So 84 - 32 + 47 = 69."  (this equals 99, not 69)

By iteration 300 the reasoning is back, coherent and deliberate, and correct:

> "If we add 84 and 47, we get 131, which is too high. But if we subtract 47 from 84, we get 37.
> Now add 32 to 37, we get 69. So 84 - 47 + 32."

So the reasoning length actually decreases at first, as it becomes coherent, then grows longer and longer as it reasons correctly, as in the R1 paper.

We also see resemblances to the "aha moment": the model tries a combination, notices
it overshoots ("too high"), and backtracks. But the search only ever explores additions and
subtractions, never a multiply.

Splitting iteration 300 by operation and size (the same 2x2 we used for the baseline), we see a different story:

| cell                  | pass@1 | pass@10 |
|-----------------------|-------:|--------:|
| add/sub, 3 numbers    | 80.2% | 98.9% |
| add/sub, 4 numbers    | 44.1% | 85.7% |
| needs-mult, 3 numbers |  0.0% |  0.0% |
| needs-mult, 4 numbers |  0.0% |  0.0% |

Add/sub is now strong on both sizes. But multiplication problems fall completely to 0%, including the
3-number problems the base could sometimes solve (13.5% at the base). This means that GRPO stopped attempting multiplication, though the base could barely do these problems either.

<div style="text-align:center;margin:1.4em 0"><img src="/assets/img/grpo/passk_grpo.png" alt="GRPO-300 pass@k: add/sub climbs to 94%, multiplication stays at 0%" style="max-width:540px;width:100%;height:auto;border-radius:6px"></div>

*Figure: GRPO-300 pass@k by operation (k = 1 to 10). Add/sub coverage grows with more samples
(67% to 94%); multiplication stays at 0%, no matter how many tries.*

Why is it zero? The answer is simple: on problems that need a multiply, 22% of base
attempts contain a `*` or `/`, but by iteration 200 that is 0%. 
This is because the model almost never gets a correct answer on the multiplication problems, so all four rollouts in a group
earn the same near-zero reward, and the model learns nothing from those problems.

So GRPO leaves us with a model that learned to reason but lost the ability to multiply. This is the gap we address next.

## SFT: Just show it the answers

GRPO could not teach multiplication because the base almost never produces a correct one for the
reward to reinforce. So next we hand the model the answers directly: we supervised-fine-tune on
correct multiplication solutions, then evaluate the same way.


Our SFT data is 5,000 Countdown problems that genuinely *require* a multiply or divide (no add/sub
solution exists), each paired with a correct, worked solution from a brute-force solver. There is
not a single add/sub-only problem in it. Each example pairs a question (Q) with the worked
solution (A) we train the model to imitate:

```
Q: Using the numbers [48, 13, 10], create an equation that equals 82.
A: I need to make 82 from [48, 13, 10]. First, 13 * 10 = 130. Finally, 130 - 48 = 82. </think>
   <answer>((13 * 10) - 48)</answer>
```

```
Q: Using the numbers [27, 39, 26, 68], create an equation that equals 29.
A: I need to make 29 from [27, 39, 26, 68]. First, 27 - 26 = 1. Then, 68 * 1 = 68. Finally, 68 - 39 = 29. </think>
   <answer>((68 * (27 - 26)) - 39)</answer>
```

Every step is arithmetically correct. 

Here's the SFT model evaluation on the same 2x2:

| cell                  | pass@1 | pass@10 |
|-----------------------|-------:|--------:|
| add/sub, 3 numbers    |  8.6% | 19.1% |
| add/sub, 4 numbers    |  4.6% | 19.6% |
| needs-mult, 3 numbers | 23.8% | 36.5% |
| needs-mult, 4 numbers |  2.0% |  5.1% |

The model solves 36.5% of 3-number multiplications (up from 13.5% at the base) and even 5.1% of
4-number ones (up from 0%). This is the only arm in the study that teaches any non-trivial multiplication (about 11% pass@10 once degenerate solves like multiplying by 1 are removed).
But add/sub, which the data never contained, collapses from 73% to 19% on 3-number problems. The
model traded the skill it had for the one we showed it.

<div style="text-align:center;margin:1.4em 0"><img src="/assets/img/grpo/passk_base_vs_sft.png" alt="Base vs SFT pass@k on both operations: SFT gains multiplication, loses add/sub" style="max-width:540px;width:100%;height:auto;border-radius:6px"></div>

*Figure: pass@k (k = 1 to 10). Color marks the model (red base, blue SFT); marker marks the
operation (+ for add/sub, x for multiplication). SFT lifts multiplication above the base but its
add/sub collapses far below it.*


So now we have two half-models. GRPO can add and subtract but not multiply; SFT can multiply (a
little, unreliably) but has forgotten how to add. The obvious question is whether we can have both: SFT to
install multiplication, then GRPO to clean it up. That is what we try next.

## SFT then GRPO

We run the same GRPO, same reward and config, starting from the SFT checkpoint instead of the
base. GRPO does restore add/sub, from SFT's 19% back to 75% pass@10. But the multiplication is
gone, back to 0%:

| cell                  | pass@1 | pass@10 |
|-----------------------|-------:|--------:|
| add/sub, 3 numbers    | 87.0% | 89.4% |
| add/sub, 4 numbers    | 43.8% | 51.8% |
| needs-mult, 3 numbers |  0.0% |  0.0% |
| needs-mult, 4 numbers |  0.0% |  0.0% |

So stacking them gives neither half-model's strength: the multiplication SFT installed is deleted,
and the restored add/sub is worse than GRPO-alone's. 

<div style="text-align:center;margin:1.4em 0"><img src="/assets/img/grpo/passk_compare.png" alt="add/sub pass@k: GRPO-alone climbs to 94% while SFT-then-GRPO stalls at 75%" style="max-width:540px;width:100%;height:auto;border-radius:6px"></div>

*Figure: add/sub pass@k, GRPO-alone vs SFT-then-GRPO. They are tied at a single sample, but with
ten tries GRPO-alone reaches 94% while SFT-then-GRPO stalls at 75%.*

At one sample SFT-then-GRPO is nominally ahead (71% vs 67%, but this is within noise: the 95% intervals overlap). But with ten tries GRPO-alone
pulls away to 94% while SFT-then-GRPO stalls at 75%; extra sampling barely helps it.

The reason is that GRPO inherited SFT's format and never let go of it. SFT trained the model into
a rigid template, "I need to make X. First, ... Finally, ...", and GRPO leaves it completely
intact. The problem is that this template (1) makes the model output the same response each time, and (2) does not let it take a step back when a combination does not work. Here are SFT-then-GRPO's samples on [84, 32, 47] -> 69:

```
I need to make 69 from [84, 32, 47]. First, 84 - 47 = 37. Finally, 37 + 32 = 69.  ((84 - 47) + 32)
I need to make 69 from [84, 32, 47]. First, 84 - 47 = 37. Finally, 37 + 32 = 69.  ((84 - 47) + 32)
I need to make 69 from [84, 32, 47]. First, 84 - 47 = 37. Finally, 37 + 32 = 69.  ((84 - 47) + 32)
```

All ten samples are this exact string. SFT-then-GRPO produces about two distinct answers per ten
tries, whereas GRPO-alone produces four to eight.

Multiplication dies for the same reason it never appeared under GRPO-alone. SFT's
multiplication was mostly wrong arithmetic (the worked steps read fine but compute the wrong product), so it fails the verifier, and GRPO prunes whatever fails.


## Lessons

Here are the lessons:

1. **GRPO sharpens, it does not teach.** Reward can only reinforce what the model already produces,
   so GRPO amplifies the add/sub the base could already do (54% to 94%) but does not learn multiplication, dropping the base's already-near-zero rate (7 genuinely-correct samples in 1,500) to exactly 0%.
2. **Answer-only supervision is not sufficient.** SFT on correct multiplication was the only
   thing that produced any, but on this narrow, answer-only data it forgot add/sub and learned the
   *shape* of a worked multiplication, not the arithmetic. Whether richer, reasoning-trace
   supervision would do better is untested here.
3. **Formatting of the supervision dataset is very important.** A crucial flaw of our current SFT data is that it directly gives the correct combination without attempting others the way GRPO's reasoning does. A better SFT dataset would remedy this by providing a more reasoning-like training set.
4. **GRPO keeps only what survives verification.** Stacking GRPO on SFT did not combine their
   strengths. SFT's multiplication was fabricated, so GRPO pruned it back to 0%, and the rigid SFT
   template survived intact, collapsing reasoning diversity to about two distinct answers per ten
   tries.

In future work, we are going to try other methods to improve the multiplication capability of this model, including SFT on a better dataset, rejection sampling, and so on.
