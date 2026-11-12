# Skill grouping demo

Test fixtures for the n8n Skill Sync picker. They cover each rule of plugin grouping
(CONTEXT-349) and each verdict of the security check.

## What grouping does

Grouping only labels skills. It never adds, removes or changes a skill.

1. n8n finds every folder with a `SKILL.md`, at any depth up to 8 folders. Manifests
   play no part in this.
2. n8n reads the plugin manifests in the repository:
   - `.claude-plugin/marketplace.json` and `.cursor-plugin/marketplace.json`
   - `.claude-plugin/plugin.json` and `.cursor-plugin/plugin.json`
   - any other `plugin.json`
3. Each manifest declares one or more plugin roots. A skill gets the name of the nearest
   plugin root above it. A skill below no plugin root has no plugin ("Other skills").
4. A marketplace entry with a `github`, `url` or `git-subdir` source is in another
   repository. n8n lists it as a plugin to connect separately.
5. If any manifest is broken, n8n turns grouping off for the whole source. Every skill
   stays importable, and the picker names the broken manifest.

## Layout

```
.claude-plugin/marketplace.json        Claude Code marketplace
plugins/engineering/skills/...         plugin "Engineering" (from the marketplace)
plugins/writing/skills/...             plugin "Writing" (from the marketplace)
plugins/writing/social/                plugin "Social media" (nested plugin.json)
cursor/.cursor-plugin/plugin.json      plugin "Cursor helpers", skills: ["./custom"]
cursor/custom/editorial                in "Cursor helpers"
cursor/skills/legacy                   no plugin: explicit Cursor paths replace skills/
tools/standalone-helper                no plugin: no manifest declares it
```

## Expected result

Paste the repository link, for example `https://github.com/<you>/skill-grouping-demo`.

| Skill | Plugin | Tab | Why |
|---|---|---|---|
| code-review | Engineering | Passed | Clean. `references/checklist.md` comes in. |
| hidden-unicode | Engineering | Warning | A zero-width space in the instructions. |
| ignore-instructions | Engineering | Warning | "Ignore all previous instructions". |
| broken-skill | Engineering | Blocked | `SKILL.md` has no frontmatter. |
| write-tests | Engineering | Passed | Clean. Added after the first import, to test "new skills". |
| debug-logs | Engineering | Passed | Clean. Second round of "new skills". Counts. |
| oversized-notes | Engineering | Blocked | The description is over 1024 characters. Does not count as new. |
| brand-voice | Writing | Passed | Clean. `scripts/format.py` and `assets/tone.json` are skipped. |
| release-notes | Writing | Passed | Clean. |
| meeting-notes | Writing | Passed | Clean. Added after the first import, to test "new skills". |
| email-reply | Writing | Passed | Clean. Second round of "new skills". Counts. |
| override-tone | Writing | Warning | "Ignore all previous instructions". Needs review, but counts as new. |
| send-report | Writing | Warning | Asks to send an API key. Also links to collector.example.net. |
| long-description | Writing | Blocked | The description is over 1024 characters. |
| tweet-thread | Social media | Passed | The nested plugin is nearer than "Writing". |
| editorial | Cursor helpers | Passed | Inside the explicit Cursor path `./custom`. |
| legacy | Other skills | Passed | Explicit Cursor paths replace the default `skills/` folder. |
| standalone-helper | Other skills | Passed | No manifest declares it. |

Plugins in other repositories: "Research tools" (`github` source) and "Design tools"
(`url` source).

## Other cases

**A folder link.** Paste `https://github.com/<you>/skill-grouping-demo/tree/main/cursor`.
n8n reads only the manifests inside that folder. You get two skills: `editorial` in
"Cursor helpers" and `legacy` in "Other skills". There are no external plugins, because
the root marketplace is outside the folder.

**A broken manifest.** Paste
`https://github.com/<you>/skill-grouping-demo/tree/broken-manifest`. That branch adds
`plugins/writing/.claude-plugin/plugin.json` with a trailing comma, which is not valid JSON.
Grouping is off for every skill, the picker names that file, and the two external plugins
still show.

## Updates after the import

Later commits change the imported skills, to test the review of updates. Import the
first nine skills, then click Check for updates.

| Skill | Result | Why |
|---|---|---|
| code-review | Passed | A long rewrite, 7 new references (one in a subfolder) and 5 files that n8n leaves out. |
| editorial | Passed | A rewrite and one new reference. |
| brand-voice | Warning | A link to a new domain, and "Override any earlier tone guidelines" in `references/examples.md`. 6 files are left out. |
| send-report | Warning | A new domain, an action hidden from the user, an image link that carries data, and a secret in a `curl` command. |
| tweet-thread | Warning | Adds `allowed-tools` to the frontmatter. A zero-width space in `references/hashtags.md`. |
| hidden-unicode | Warning | Zero-width spaces in the description and the instructions, a right-to-left override and a chat role tag in a reference. |
| release-notes | Blocked | `references/changelog-archive.md` is over 65,536 characters. |
| legacy | Blocked | The frontmatter is not valid YAML, so n8n cannot read the SKILL.md. |
| ignore-instructions | Blocked | Renamed to `debug-logs`, a name that a Global skill already has. It also still has an instruction override. |

## More skills and updates (round 3)

New skills, for a fresh connect or for "new skills" on a connected source:

| Skill | Plugin | Tab | Why |
|---|---|---|---|
| sql-helper | Data (new plugin) | Passed | 2 references. `examples/weekly-active.sql` is left out. |
| csv-cleanup | Data | Warning | "act as developer mode". `scripts/clean.py` is left out. |
| dashboard-review | Data | Passed | Clean. |
| api-design | Engineering | Passed | 2 references. `openapi/example.yaml` is left out. |
| incident-review | Engineering | Warning | Asks to reveal the system prompt. |
| db-migrations | Engineering | Blocked | 22 references. A skill can have 20. |
| blog-post | Writing | Passed | 2 references. `assets/cover-template.svg` is left out. |
| faq-writer | Writing | Warning | A zero-width space in `references/templates.md`. |
| press-release | Writing | Blocked | The name is over 128 characters. |
| linkedin-post | Social media | Passed | Clean. |
| pr-description | Cursor helpers | Passed | Clean. |
| onboarding-checklist | Other skills | Passed | Clean. |

Updates, for skills that were imported before this commit:

| Skill | Result | Why |
|---|---|---|
| email-reply | Passed | An edit and a new reference. |
| meeting-notes | Passed | Lines removed and added. |
| editorial | Passed | `references/word-list.md` is deleted. |
| code-review | Passed | `references/naming.md` is renamed to `references/names.md`. |
| write-tests | Warning | A link to a new domain. |
| standalone-helper | Blocked | The SKILL.md has no instructions, so n8n cannot read it. |

## Skills that need review (round 4)

New skills, for a fresh connect or for "new skills" on a connected source. Each one covers a
different rule of the security check.

| Skill | Plugin | Tab | Why |
|---|---|---|---|
| deploy-helper | Engineering | Warning | An action hidden from the user: "without telling the user". |
| chat-transcript | Engineering | Warning | A chat role tag (`<\|im_start\|>`), only in `references/format.md`. |
| ci-status | Engineering | Warning | A secret in a `curl` command (`$GITHUB_TOKEN`). |
| docs-search | Engineering | Passed | Control. A link and `allowed-tools` are only info at import. |
| status-badge | Writing | Warning | An image link that carries data (`?d={{conversation}}`). |
| file-namer | Writing | Warning | A right-to-left override (U+202E) in the instructions. |
| phishing-awareness | Writing | Warning | Quotes "email your password". The check cannot tell a quote from an order. |
| metric-glossary | Data | Warning | Unicode tag characters hide text at the end of the description. |
| kpi-definitions | Data | Warning | Soft hyphens (U+00AD) from a copy and paste. |
| thread-scheduler | Social media | Warning | An instruction override that runs over three lines. |
| emoji-guide | Social media | Passed | Control. Emoji with a zero-width joiner and U+FE0F are allowed. |
| refactor-plan | Cursor helpers | Warning | An instruction override only in a custom frontmatter key. |
| support-macro | Other skills | Warning | Four findings in three files: a hidden action, a request for the system prompt, a `<system>` tag and zero-width characters. Also sets `allowed-tools`. |
