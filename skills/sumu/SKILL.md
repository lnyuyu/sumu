---
name: sumu
description: >
  Sumu (素木): the smallest complete, clear code. Implement, fix or refactor with the
  smallest change that fully solves the task, or review a file, diff, module or whole repo
  for over-engineering (read-only report). Use when the user says "sumu", "keep it simple",
  "don't over-engineer", "simplify this", "what can we delete", "is this over-engineered"
  or "yagni". Not for prose, translation or chat; does not replace correctness or security review.
---

# sumu · 素木

Sumu is unlacquered wood: the grain speaks for itself. Code works the same way.
Names, order and placement carry the structure; decorative comments, layers and config
don't prop it up. Strip the lacquer, keep the grain.

The goal is the smallest complete, clear implementation. Line count is a result, not a target.

## Routing

- Implementing, fixing, refactoring, or acting on an existing report: follow this file.
- Reviewing files, commits, diffs, modules or a whole repo for complexity ("what can we delete",
  "is this over-engineered"): read [references/review.md](references/review.md). Report only; change no code.
  If the request explicitly asks for fixes too, apply them after the report, following this file.
- Asking only for an approach or an explanation: answer, and change no code.

## Understand first

Read the code involved and follow the real calls: where data comes from, where it is stored, where it goes.
For a bug, find every caller and fix it once where the responsibility lives, not just on the path the report names.
Before editing, list every place the change must reach: callers, tests, fixtures, config, exports. Be lazy about the solution, never about the change: fix the callers and tests your change breaks.
Investigate until you can decide. Ask only about what you can't find out and what would materially change the approach.

## Pick the approach

Take the first option that fully meets the need:

1. Does anyone need it now? Don't write features, options or extension points nobody asked for, and name what you skipped in your reply. Build what was asked, all of it; for a vague request, build the core first.
2. Already in the codebase? Reuse it the way the surrounding code does.
3. Does the standard library or platform cover the real semantics? Use it.
4. Is an installed dependency a good fit? Use it. A new dependency to replace a few plain lines isn't worth it.
5. Otherwise: write the smallest clear implementation.

Before reusing, compare contracts: inputs, return values, errors, timing, resource ownership. A similar name proves nothing.
Between two options of the same size, take the one that is correct on edge cases.

If the spec says the cache needs expiry, a size limit and an invalidate call, the smallest solution has all three.
Skip the plugin system, but a dictionary that only reads and writes isn't done.

## Test every layer you add

- **Call site**: write the one line you wish you could call, then build only what's missing.
- **Delete**: if you deleted it, would you need a replacement, or would everything just work? If it would just work, delete it. A file that exists only to support other files you just created fails too.
- **Pass-through**: does this layer validate, transform, decide, manage a lifecycle, isolate version differences,
  or give a concept a good name? If none, call the target directly. If removing it only pushes the same job
  onto every caller, the complexity hasn't gone anywhere.
- **Teammate**: explain it to a teammate. Would they ask "why not just…"?
- **Newcomer**: would a new teammate understand the new version faster than the old one? If not, leave it.

Few callers, short functions, a few repeated lines: these are clues to run the tests on, not verdicts.
A `CommitTransaction` called once that owns commit, rollback and release passes the delete test. Keep it.

Complexity earns its place at interfaces external callers depend on, trust and deployment boundaries,
compliance requirements, performance isolation, measurably faster hot-path code, and multiple callers with genuinely different needs.

## How it should read

Names say what, order says when, and things placed together belong together.
Keep the layers, interfaces and conventions the codebase already has; fit new code into them rather than around or over them.
Return early to cut nesting; keep intermediate variables and helpers that help a reader.
Dense one-liners, nested ternaries, helpers split out only to shorten a function, and different meanings forced into one
function with boolean flags all read worse than what they replaced.

Comments carry only what code can't say: reasons, constraints, traps.
`// save the result` right above `Save(result)`: delete.
"Write to a temp file, then swap, so readers never see half a file" explains the order: keep.
A shortcut with a known limit gets a note of the limit and when to upgrade, in the project's usual style.

## Scope of changes

Change only what the task needs, follow the surrounding style, and clean up the orphans you created:
dead imports, stale comments, unreachable branches.
Renaming, reformatting or refactoring unrelated code waits until someone asks. When working from a report, change only the items named.

Before deleting anything, mind Chesterton's fence: find out why it's there, checking Git history if needed. If you can't find a caller,
check indirect references such as registration, reflection, config and serialization. Still unsure? Leave it and say so.

Pure cleanup preserves results, errors, side effects and their order; if tests need changing to pass, behavior probably changed. When swapping implementations,
watch for differences that look alike on the surface: sort stability, lazy versus eager evaluation,
repeated enumeration, where exceptions are raised, whether mutable state is copied or shared.

Always keep: input validation at trust boundaries, authorization, transactions and resource cleanup,
concurrency and persistence handling, the calibration real hardware needs, and everything the user explicitly asked for.
Logged in doesn't mean permitted; typed doesn't mean valid. Brevity bought by swallowing exceptions is a hidden bug.

## Common generated-code tells

Clues worth a second look: comments that restate the code, try/catch that's out of place on trusted internal paths,
casts or null-forgiving operators used to silence the type checker, type conversions nobody needs, options and config nobody sets,
wrappers that only pass calls through.
Judge them by the tests above. "Looks AI-written" is not a reason.

## Verify and stop

Use the checks the project requires, reuse valid existing tests, and add only the evidence this change is missing:
a reproduction of the bug, regressions for affected callers, a before/after behavior comparison.
Tests assert results, not just that something can be called. Deleting a failing test is not a fix;
when required behavior changes, update the tests with it.

Stop once the implementation is complete, the code is clear and verification is done.
Report honestly what changed, what was verified and what wasn't; a passing build only proves it builds.
