# sumu · 素木

English | [中文](README.zh-CN.md)

Sumu (素木) is unlacquered wood: the grain speaks for itself.

An on-demand coding skill. When writing code, it takes the smallest complete, clear approach. When reviewing code, it looks only for complexity that doesn't pay for itself, with evidence for every finding.

## Why

There are plenty of "don't over-engineer" skills, but each covers one slice: some act before you write, some clean up the current diff, some audit existing code, and you have to remember which one to call. Sumu puts all of this behind one entry point. One name is enough.

What it cares about:

- **Simple and complete.** Build everything that was asked for. No stripped-down first version you have to argue up.
- **Deletion needs evidence.** Say what it does and what takes over once it's gone. Finding no callers is not proof it's unused.
- **Clarity over line count.** Five readable lines beat one line you have to decode.
- **No extra rituals.** No fixed reply format, no mandatory test for every piece of logic; it reuses the project's existing checks.

## Usage

```text
Use sumu to implement the export feature; keep every confirmed requirement.
Use sumu to fix this bug.
Use sumu to see what in this change can be simplified.   → read-only report
Use sumu to review the src/export module.               → read-only report with coverage
Use sumu to review the whole repo.                      → read-only report: what was examined, what wasn't
Fix 2 and 5.                                            → changes only the named items
```

Reviews only report; code changes only when the request asks for them. Reviews look at complexity alone and don't replace correctness or security review.

## Install

Copy the whole `skills/sumu` folder into your host's skills directory—for example `~/.agents/skills/` or `<repo>/.agents/skills/` for Codex CLI (verified on Codex CLI 0.166.0), or `~/.claude/skills/` for Claude Code.

No scripts, hooks or network access needed. Reviews read `references/review.md` from the same folder.

## Layout

```text
skills/sumu/
  SKILL.md              principles and routing: implement, fix and refactor follow it directly
  references/review.md  review: scope, verification, report format
evals/                  eval cases and small fixtures
```

## Status

Initial release. Trigger routing and 8×3 control-vs-sumu behavioral evals passed on Codex CLI 0.166.0 (`gpt-6.1-sol`); see [evals](evals/README.md). MIT licensed, see [LICENSE](LICENSE); acknowledgments in [NOTICE](NOTICE).
