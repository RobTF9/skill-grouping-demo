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

To test update badges, a later commit changes two imported skills:

- `brand-voice` gets one more instruction. Its update passes the security check: **Update available**.
- `release-notes` gets a description over 1024 characters. Its update is blocked: **Update blocked**.
