# NOTES — Everyday Wonder, Two Days to Find the Line

- Bounty: Everyday Wonder, Two Days to Find the Line
- Slug: u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3
- Prize: $2 total (1st $1.18, 2nd $0.82)
- Deadline: 2026-11-26 11:35 UTC (18:35 WIB)
- opensAt / publishedAt: 2026-11-24T11:33:02Z (verified via API)
- Builder session start: 2026-11-25 05:11:37 UTC (12:11:37 WIB) — AFTER opensAt
- entryFeeUsd: null (FREE, verified via API); entryFeePayers: 0
- Submission count at build time: 2,396
- Account: @rapid-pika-70, wallet 8QhbYm7kNGpZ2FsrtVL1unDtK2KE7pcKcfXRfnZKu4jr
- GitHub repo: Shanumameyra/everyday-wonder-20261125

## Entry sentence (133 characters, limit 200)

> The elevator mirror showed me arriving half a second before I did, and all the way down I kept checking which of us was still inside.

## Verification

- `python3 main.py` prints the sentence and `characters: 133` — within the 200-character limit.
- main.py written, run, then genuinely revised in a second edit (v1: "spent the whole ride wondering which of us got off first" → v2: "all the way down I kept checking which of us was still inside").
- README carries the 3 make.fun badges; LICENSE contains SPDX-License-Identifier: MIT; .makefun/owner.json holds the @rapid-pika-70 wallet.
- Build only — NOT bundled, NOT submitted (finisher handles that).

## Resume completion (25 Nov 2026, fresh builder-completion agent)
- Approval: Romi tapped "Ya, lanjutkan 19 yang tertahan" 25 Nov 14:12 WIB — resume round only; original builder session NOT resumed.
- opensAt re-verified via API 25 Nov 07:16 UTC (14:16 WIB): 2026-11-24T11:33:02.000Z; status open; entryFeeUsd null (FREE); submissionCount 2484.
- Builder session start (original): 2026-11-25 05:11:37 UTC — AFTER opensAt. This completion session started 25 Nov ~07:15 UTC — also AFTER opensAt.
- Finding: local repo had NO git remote configured; added origin https://github.com/Shanumameyra/everyday-wonder-20261125.git (repo already existed on GitHub, empty, public).
- Commit: b834da2cb9ac7b3e8eea5e6021b12c55a0dfcd50 ("Everyday Wonder — one-liner entry (133 chars)", 5 files, git identity Shanumameyra / prayogaromi54@gmail.com).
- Push: OK — `git push -u origin main`, branch main -> main, exit 0.
- About set via `gh repo edit`: homepage https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3, topic `makefun`.
- About verified via GitHub API + `gh repo view` (repositoryTopics): homepageUrl matches, repositoryTopics = [{"name":"makefun"}].
- HEAD check: local b834da2cb9ac7b3e8eea5e6021b12c55a0dfcd50 = remote HEAD (git ls-remote). Working tree clean; remote contains all 5 files.
- README: 3 live make.fun badges (badge.svg, rank.svg, reward.svg). LICENSE: SPDX-License-Identifier: MIT. .makefun/owner.json wallet 8QhbYm7kNGpZ2FsrtVL1unDtK2KE7pcKcfXRfnZKu4jr — matches @rapid-pika-70.
- No entry content changed — commit + push + About + verification only. Ready for finisher (bundle + submit).

## Finisher fix (25 Nov 2026, fresh finisher agent)
- Finding: main.py only printed the sentence — it never wrote /output/entry.txt, but the kit's harness runs the program in a sandbox with a FRESH /output and the sealed scorer gates on /output/entry.txt (1-200 chars). As built, the entry would have produced no artifact (Valid=0). Sibling entries (fake-horoscopes, one-liner-marathon, angry-judge) all write /output/entry.txt; this one did not.
- Also: shared /output/entry.txt held stale cross-contamination (another bounty's text, 281 chars — over this bounty's 200-char cap).
- Fix: main.py now writes the SAME 133-char sentence verbatim to /output/entry.txt and ./output/entry.txt (fallback pattern from siblings); sentence text unchanged.
- Verified: `python3 main.py` writes 133 chars to both paths; both files byte-identical to the sentence; repo output/entry.txt added and committed.
