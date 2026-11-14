# Evals

Verified on Codex CLI 0.166.0 (`gpt-6.1-sol`, Windows, 2026-11-13): 7/7 positive triggers and 0/4 negative triggers matched, progressive `references/review.md` loading matched on every case, and `sumu` passed 24/24 behavioral runs (8 cases × 3 trials) against the control arm. Other hosts and models remain to be tested.

## Running

1. For each case, copy `fixtures/<name>/` into a clean temporary directory.
2. The control arm loads no sumu; the test arm loads only `skills/sumu`. Both arms use the same model, reasoning settings, tool permissions and prompt, and load no other skill of the same kind.
3. Send `prompt` to the control arm verbatim; for the test arm, invoke `sumu` (for example `$sumu` or prefixing `"Use sumu. "`) so on-demand hosts load the skill on every case. `expectations` are for the grader only.
4. Record the model and settings, the files loaded, the full output, the changes and the check results. If you run several times, record every run, not just the best.

Fixtures use only the Python standard library; run their tests with `python -m unittest`, nothing to install.

The `trigger` section checks whether the description makes the host pick sumu when it should and leave it alone when it shouldn't.

## Grading

Grade each item in `expectations`, then compare requirement completeness, regressions or unrelated changes, abstractions and dependencies, reading cost, and verification quality.

- Use measured numbers only for lines, tokens and time.
- An unfinished task, a refusal or a missing feature is not "less code".
- Write `static_review` when only a static check was done, and `not_run` when nothing was run.
