# Sumu review

Complexity only: find structure that doesn't pay for itself and propose a simpler replacement, with evidence. Read-only by default.
The judgment comes from the tests in [SKILL.md](../SKILL.md); this file covers scope, verification and the report.

## Scope

| Request | What to review |
| --- | --- |
| Specific files | Their current content plus whatever context the evidence needs; don't pretend to have a baseline you don't |
| Staged changes | The staged diff; unstaged and untracked files don't count as reviewed |
| Uncommitted changes | Staged, unstaged and untracked, each on its own; don't miss new files |
| A commit or branch | Record the actual base and head; take the base from the request, don't assume main |
| A module or the whole repo | Map first, then dig where it matters (below) |
| No scope given | Uncommitted changes; if there are none, the last commit |

Don't switch branches, fetch, or run any Git write. Leave existing changes in the working tree alone.

Modules and repos: build a brief picture from the layout, entry points, dependency manifests, config and test organization;
cover each major module's responsibility, then dig into the places with the highest maintenance cost.
Generated files, vendored copies and historical material are read only to explain a finding, never targeted for cleanup.

## Clues

| Clue | What to establish |
| --- | --- |
| Speculative features, options, config switches | Whether a current requirement, caller or contract uses them |
| Reimplemented capability | Whether existing code, the standard library or an installed dependency covers the same semantics and edge cases |
| Wrappers, middle layers, registries that only serve each other | Whether removal loses validation, isolation, compatibility, lifecycle or readability |
| The same fact stored in several places that must stay in sync | Whether it really is one fact with one lifecycle |
| Near-copies where changing one means changing the others | Whether they truly must change together; look-alikes that evolve separately stay apart |
| One function mixing several unrelated jobs | Split by job, never by line count, and never into helpers that exist only to make it shorter |
| Comments, defensive checks, fallback chains, compatibility branches | Whether they carry needed information, protection or recovery semantics |
| New dependencies | How much real complexity they replace |

File length, caller counts and search hits help you locate; they are not findings.

## Verify: no concrete evidence, no finding

Going from "looks redundant" to "can be cut" means answering four questions:

1. What does it do now, and who depends on that?
2. Which part of its maintenance cost has no current need behind it?
3. After deleting, inlining or replacing it, what keeps the original contract?
4. Which boundaries must stay, and what existing evidence or check proves it?

Explaining why something is simpler without explaining why it is still correct is not a finding.
When a symbol has no visible references, check registration, reflection, config, serialization and framework conventions; those are callers too.
If a gap remains, list the item as open and say what evidence is missing. Don't widen the search forever to rule out hypothetical callers.
A shortcut whose comment already names its limit is a decision, not a finding, unless reality has already crossed that limit.

| Situation | Judgment |
| --- | --- |
| Two pieces of logic look alike but differ in error semantics and update cycle | Don't force them into one shared function with a pile of boolean flags |
| The project already has an equivalent parser and new code writes another | After checking format, error and performance needs, suggest reuse |
| Deep layering, but one layer isolates third-party version differences | Layer count alone doesn't justify cutting through it |
| A catch turns any exception into a default success with no recovery contract | Report the specific path where it hides errors; don't generalize to "never catch" |
| A test covers a branch, but no production use was found | The test is a clue; check the contract before calling the branch dead |
| A single-use wrapper owns transaction rollback or resource release | Keep it; if there's nothing to report, say so instead of inlining it to fill a quota |

## Report

Open with one or two sentences on what you reviewed and against which baseline.
Number findings across the whole report so the user can say "fix 2 and 5":

`1. Location: evidence. Simpler replacement. Boundaries to keep or verify.`

Example (fictional):

> 1. `src/report/NameAdapter.cs:18`: the new adapter passes its argument unchanged to the existing name normalizer,
>    and the only call path adds no validation, caching or compatibility. Have the caller use the existing function
>    and delete the adapter; keep the current case and whitespace handling and run the existing name tests.

"This class has only one caller, delete it" does not qualify: it hasn't shown the class has no needed responsibility.

- Rank by maintenance payoff, reach and the risk of the change; the biggest deletion isn't automatically first.
  Whole removable burdens and duplicated sources of truth come first; local comment cleanup comes last.
- One root cause in several places is one finding, with representative locations.
- Changes to public contracts or cross-module responsibilities go under "needs a decision", with what is gained and lost; requirements decide.
- Items lacking evidence go under "open", with what's missing.
- End with one line, `Not covered:`, naming what you didn't read or couldn't confirm. For modules and repos,
  say which parts were mapped and which were examined in depth; a sample is not a full sweep.
- Module and repo reviews list at most 20 findings; say how many smaller ones were left out.
- If nothing turns up, say so and say what you checked. Don't present estimated line savings as measured, and don't pad the list.

## Boundaries

"What can we delete?" asks for analysis, not deletion. Don't edit reviewed files, install dependencies, or run commands that write product state.
If the request explicitly includes fixes, deliver the report first, then change only the named items following SKILL.md,
and report the changes and verification separately.

This review covers complexity only. An obvious bug or security issue spotted along the way can get a one-line mention,
but "not over-engineered" does not mean correct, secure or ready to ship.
