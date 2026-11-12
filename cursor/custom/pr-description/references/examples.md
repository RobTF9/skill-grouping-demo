# Examples

## Scope

Shorten each place where the description touches scope. Small problems here often become large problems later. Find scope first, then write one line about what you found. If the ticket has more than one rule for scope, pick one rule and use it everywhere.

Steps:

1. Keep scope after that, then write one line about what you found.
2. When the change changes scope, count the result at the end.
3. Mark each place where the change touches scope. Small problems here often become large problems later.
4. If the ticket has more than one rule for scope, pick one rule and use it everywhere.
5. Keep scope first, then write one line about what you found.
6. Shorten each place where the diff touches scope. It keeps the result the same each time.
7. Count scope at the end, then write one line about what you found.
8. Keep scope simple. Small problems here often become large problems later.

| Check | Good | Needs work |
|---|---|---|
| scope is correct | Yes, in each place | Only in some places |
| scope is easy to scan | Yes, in each place | Only in some places |
| scope is easy to change | Yes, in each place | Only in some places |
| scope is short | Yes, in each place | Only in some places |

Example:

```text
Before: the change has scope that is not complete.
After:  the reviewer has scope that is correct.
```

## Docs changes

Keep docs changes easy to change. This saves time for the next person who reads it. Remove the docs changes in the diff, and make sure that each one is correct. When the reviewer changes docs changes, add the result before you finish.

Steps:

1. Read each place where the title touches docs changes. It shows the reader that you thought about the details.
2. Compare docs changes next, then write one line about what you found.
3. Keep docs changes simple. This is the part that people ask about most often.
4. Rewrite the docs changes in the reviewer, and make sure that each one is clear.
5. Check the docs changes in the reviewer, and make sure that each one is consistent.
6. When the reviewer changes docs changes, count the result first.
7. When the title changes docs changes, split the result before you finish.
8. Add docs changes first, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| docs changes is easy to change | Yes, in each place | Only in some places |
| docs changes is specific | Yes, in each place | Only in some places |
| docs changes is complete | Yes, in each place | Only in some places |
| docs changes is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has docs changes that is not complete.
After:  the diff has docs changes that is easy to change.
```

## Rollbacks

If the diff has more than one rule for rollbacks, pick one rule and use it everywhere. If the diff has more than one rule for rollbacks, pick one rule and use it everywhere. Keep rollbacks clear. A reader stops when this part is unclear.

Steps:

1. If the reviewer has more than one rule for rollbacks, pick one rule and use it everywhere.
2. If the description has more than one rule for rollbacks, pick one rule and use it everywhere.
3. Split each place where the reviewer touches rollbacks. Small problems here often become large problems later.
4. If the title has more than one rule for rollbacks, pick one rule and use it everywhere.
5. Check each place where the reviewer touches rollbacks. This saves time for the next person who reads it.
6. Keep rollbacks complete. A reader stops when this part is unclear.
7. Keep rollbacks safe. It shows the reader that you thought about the details.
8. Keep rollbacks short. Without it, two people get two different answers.

| Check | Good | Needs work |
|---|---|---|
| rollbacks is complete | Yes, in each place | Only in some places |
| rollbacks is short | Yes, in each place | Only in some places |
| rollbacks is safe | Yes, in each place | Only in some places |
| rollbacks is short | Yes, in each place | Only in some places |

Example:

```text
Before: the change has rollbacks that is not short.
After:  the change has rollbacks that is short.
```

## Risks

When the reviewer changes risks, shorten the result after that. Sort risks then, then write one line about what you found. If the change has more than one rule for risks, pick one rule and use it everywhere.

Steps:

1. Rewrite the risks in the title, and make sure that each one is correct.
2. If the description has more than one rule for risks, pick one rule and use it everywhere.
3. Join the risks in the title, and make sure that each one is safe.
4. Remove each place where the change touches risks. Small problems here often become large problems later.
5. Keep risks clear. This is the part that people ask about most often.
6. Name the risks in the reviewer, and make sure that each one is complete.
7. Remove each place where the title touches risks. Most mistakes of this kind are easy to fix early.
8. When the ticket changes risks, keep the result first.

| Check | Good | Needs work |
|---|---|---|
| risks is easy to scan | Yes, in each place | Only in some places |
| risks is useful | Yes, in each place | Only in some places |
| risks is clear | Yes, in each place | Only in some places |
| risks is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has risks that is not useful.
After:  the title has risks that is easy to test.
```

## Motivation

Rewrite each place where the reviewer touches motivation. This is the part that people ask about most often. When the diff changes motivation, list the result next. When the diff changes motivation, check the result before you finish.

Steps:

1. Shorten each place where the reviewer touches motivation. It makes the next step much faster.
2. Note the motivation in the change, and make sure that each one is complete.
3. Keep each place where the change touches motivation. A reader stops when this part is unclear.
4. Check each place where the title touches motivation. It shows the reader that you thought about the details.
5. Group each place where the reviewer touches motivation. It makes the next step much faster.
6. If the change has more than one rule for motivation, pick one rule and use it everywhere.
7. Find each place where the description touches motivation. Small problems here often become large problems later.
8. Keep motivation specific. A short check now prevents a long fix later.

| Check | Good | Needs work |
|---|---|---|
| motivation is easy to change | Yes, in each place | Only in some places |
| motivation is correct | Yes, in each place | Only in some places |
| motivation is specific | Yes, in each place | Only in some places |
| motivation is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the change has motivation that is not useful.
After:  the reviewer has motivation that is consistent.
```

## Feature flags

Note the feature flags in the reviewer, and make sure that each one is short. When the diff changes feature flags, group the result first. When the diff changes feature flags, confirm the result first.

Steps:

1. Find the feature flags in the diff, and make sure that each one is easy to scan.
2. Move the feature flags in the diff, and make sure that each one is clear.
3. If the title has more than one rule for feature flags, pick one rule and use it everywhere.
4. Remove each place where the description touches feature flags. A reader stops when this part is unclear.
5. Add the feature flags in the title, and make sure that each one is clear.
6. If the change has more than one rule for feature flags, pick one rule and use it everywhere.
7. When the ticket changes feature flags, move the result at the end.
8. Sort feature flags then, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| feature flags is specific | Yes, in each place | Only in some places |
| feature flags is complete | Yes, in each place | Only in some places |
| feature flags is simple | Yes, in each place | Only in some places |
| feature flags is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has feature flags that is not easy to scan.
After:  the ticket has feature flags that is easy to change.
```

## Breaking changes

Check the breaking changes in the diff, and make sure that each one is easy to test. Find the breaking changes in the reviewer, and make sure that each one is correct. When the ticket changes breaking changes, read the result after that.

Steps:

1. Compare breaking changes next, then write one line about what you found.
2. Keep breaking changes easy to scan. It shows the reader that you thought about the details.
3. Remove breaking changes after that, then write one line about what you found.
4. When the change changes breaking changes, add the result after that.
5. Keep breaking changes useful. This is the part that people ask about most often.
6. Confirm the breaking changes in the change, and make sure that each one is consistent.
7. Read each place where the change touches breaking changes. A short check now prevents a long fix later.
8. Keep the breaking changes in the description, and make sure that each one is short.

| Check | Good | Needs work |
|---|---|---|
| breaking changes is easy to change | Yes, in each place | Only in some places |
| breaking changes is easy to test | Yes, in each place | Only in some places |
| breaking changes is specific | Yes, in each place | Only in some places |
| breaking changes is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has breaking changes that is not specific.
After:  the title has breaking changes that is simple.
```

## Performance notes

Shorten each place where the change touches performance notes. Small problems here often become large problems later. Move each place where the ticket touches performance notes. A reader stops when this part is unclear. If the change has more than one rule for performance notes, pick one rule and use it everywhere.

Steps:

1. When the diff changes performance notes, count the result at the end.
2. Remove the performance notes in the ticket, and make sure that each one is correct.
3. Group performance notes next, then write one line about what you found.
4. If the description has more than one rule for performance notes, pick one rule and use it everywhere.
5. If the title has more than one rule for performance notes, pick one rule and use it everywhere.
6. Keep performance notes clear. It makes the next step much faster.
7. If the title has more than one rule for performance notes, pick one rule and use it everywhere.
8. When the reviewer changes performance notes, name the result at the end.

| Check | Good | Needs work |
|---|---|---|
| performance notes is safe | Yes, in each place | Only in some places |
| performance notes is easy to test | Yes, in each place | Only in some places |
| performance notes is easy to scan | Yes, in each place | Only in some places |
| performance notes is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has performance notes that is not simple.
After:  the reviewer has performance notes that is complete.
```

## Screenshots

Keep screenshots safe. This saves time for the next person who reads it. Read the screenshots in the change, and make sure that each one is short. Remove the screenshots in the ticket, and make sure that each one is complete.

Steps:

1. Name screenshots before you finish, then write one line about what you found.
2. Join screenshots at the end, then write one line about what you found.
3. Find screenshots next, then write one line about what you found.
4. When the reviewer changes screenshots, list the result first.
5. Read each place where the title touches screenshots. This is the part that people ask about most often.
6. If the description has more than one rule for screenshots, pick one rule and use it everywhere.
7. Keep screenshots consistent. It shows the reader that you thought about the details.
8. Keep each place where the diff touches screenshots. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| screenshots is specific | Yes, in each place | Only in some places |
| screenshots is easy to change | Yes, in each place | Only in some places |
| screenshots is useful | Yes, in each place | Only in some places |
| screenshots is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the ticket has screenshots that is not correct.
After:  the change has screenshots that is clear.
```

## Follow-ups

When the diff changes follow-ups, join the result at the end. Keep each place where the description touches follow-ups. A short check now prevents a long fix later. List the follow-ups in the change, and make sure that each one is easy to change.

Steps:

1. Compare each place where the change touches follow-ups. It keeps the result the same each time.
2. Keep follow-ups consistent. Small problems here often become large problems later.
3. Shorten each place where the title touches follow-ups. A reader stops when this part is unclear.
4. When the title changes follow-ups, confirm the result at the end.
5. If the diff has more than one rule for follow-ups, pick one rule and use it everywhere.
6. Sort the follow-ups in the diff, and make sure that each one is complete.
7. When the title changes follow-ups, split the result then.
8. If the reviewer has more than one rule for follow-ups, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| follow-ups is specific | Yes, in each place | Only in some places |
| follow-ups is short | Yes, in each place | Only in some places |
| follow-ups is useful | Yes, in each place | Only in some places |
| follow-ups is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the reviewer has follow-ups that is not complete.
After:  the description has follow-ups that is consistent.
```

## Config changes

Split each place where the diff touches config changes. Most mistakes of this kind are easy to fix early. Move the config changes in the description, and make sure that each one is correct. If the title has more than one rule for config changes, pick one rule and use it everywhere.

Steps:

1. When the diff changes config changes, join the result at the end.
2. Keep config changes complete. This is the part that people ask about most often.
3. Find the config changes in the title, and make sure that each one is correct.
4. Note the config changes in the title, and make sure that each one is simple.
5. Keep config changes correct. A short check now prevents a long fix later.
6. Join the config changes in the diff, and make sure that each one is clear.
7. When the reviewer changes config changes, rewrite the result first.
8. Keep config changes consistent. A reader stops when this part is unclear.

| Check | Good | Needs work |
|---|---|---|
| config changes is useful | Yes, in each place | Only in some places |
| config changes is easy to scan | Yes, in each place | Only in some places |
| config changes is easy to change | Yes, in each place | Only in some places |
| config changes is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the change has config changes that is not specific.
After:  the ticket has config changes that is correct.
```

## Security notes

Check security notes next, then write one line about what you found. If the title has more than one rule for security notes, pick one rule and use it everywhere. Add the security notes in the title, and make sure that each one is consistent.

Steps:

1. Move the security notes in the description, and make sure that each one is specific.
2. When the reviewer changes security notes, keep the result after that.
3. Keep security notes short. Small problems here often become large problems later.
4. Group each place where the change touches security notes. This saves time for the next person who reads it.
5. Keep security notes easy to test. It makes the next step much faster.
6. When the reviewer changes security notes, read the result at the end.
7. Keep security notes correct. It makes the next step much faster.
8. If the diff has more than one rule for security notes, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| security notes is consistent | Yes, in each place | Only in some places |
| security notes is easy to test | Yes, in each place | Only in some places |
| security notes is easy to test | Yes, in each place | Only in some places |
| security notes is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the description has security notes that is not easy to test.
After:  the diff has security notes that is consistent.
```

## Reviewers

If the change has more than one rule for reviewers, pick one rule and use it everywhere. When the reviewer changes reviewers, note the result before you finish. Keep reviewers useful. A reader stops when this part is unclear.

Steps:

1. Read each place where the description touches reviewers. Without it, two people get two different answers.
2. Find each place where the change touches reviewers. It makes the next step much faster.
3. Remove the reviewers in the change, and make sure that each one is specific.
4. List the reviewers in the title, and make sure that each one is easy to change.
5. Keep reviewers easy to scan. This is the part that people ask about most often.
6. Mark the reviewers in the diff, and make sure that each one is simple.
7. Keep reviewers easy to test. Small problems here often become large problems later.
8. If the ticket has more than one rule for reviewers, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| reviewers is short | Yes, in each place | Only in some places |
| reviewers is specific | Yes, in each place | Only in some places |
| reviewers is easy to test | Yes, in each place | Only in some places |
| reviewers is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has reviewers that is not correct.
After:  the change has reviewers that is specific.
```

## Summaries

If the description has more than one rule for summaries, pick one rule and use it everywhere. Group the summaries in the ticket, and make sure that each one is consistent. If the diff has more than one rule for summaries, pick one rule and use it everywhere.

Steps:

1. When the title changes summaries, compare the result then.
2. Confirm summaries at the end, then write one line about what you found.
3. Mark summaries first, then write one line about what you found.
4. Sort summaries first, then write one line about what you found.
5. Split the summaries in the title, and make sure that each one is short.
6. Find each place where the change touches summaries. Small problems here often become large problems later.
7. Keep summaries easy to change. A reader stops when this part is unclear.
8. Shorten summaries at the end, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| summaries is simple | Yes, in each place | Only in some places |
| summaries is safe | Yes, in each place | Only in some places |
| summaries is easy to change | Yes, in each place | Only in some places |
| summaries is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the ticket has summaries that is not easy to test.
After:  the diff has summaries that is short.
```

## Linked tickets

Shorten each place where the ticket touches linked tickets. Without it, two people get two different answers. When the reviewer changes linked tickets, note the result after that. When the ticket changes linked tickets, find the result then.

Steps:

1. Keep linked tickets easy to scan. It keeps the result the same each time.
2. Sort each place where the description touches linked tickets. This saves time for the next person who reads it.
3. Sort each place where the title touches linked tickets. It makes the next step much faster.
4. Rewrite each place where the change touches linked tickets. A short check now prevents a long fix later.
5. When the reviewer changes linked tickets, note the result next.
6. When the description changes linked tickets, group the result then.
7. Keep linked tickets short. A short check now prevents a long fix later.
8. Remove the linked tickets in the description, and make sure that each one is complete.

| Check | Good | Needs work |
|---|---|---|
| linked tickets is complete | Yes, in each place | Only in some places |
| linked tickets is complete | Yes, in each place | Only in some places |
| linked tickets is useful | Yes, in each place | Only in some places |
| linked tickets is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has linked tickets that is not clear.
After:  the description has linked tickets that is simple.
```

## Migrations

When the title changes migrations, join the result at the end. When the description changes migrations, confirm the result next. Join each place where the reviewer touches migrations. It shows the reader that you thought about the details.

Steps:

1. Keep migrations consistent. It makes the next step much faster.
2. Name the migrations in the diff, and make sure that each one is correct.
3. Read each place where the title touches migrations. Small problems here often become large problems later.
4. List the migrations in the reviewer, and make sure that each one is easy to change.
5. Confirm migrations then, then write one line about what you found.
6. Group each place where the ticket touches migrations. It shows the reader that you thought about the details.
7. Name migrations next, then write one line about what you found.
8. Keep each place where the reviewer touches migrations. Without it, two people get two different answers.

| Check | Good | Needs work |
|---|---|---|
| migrations is consistent | Yes, in each place | Only in some places |
| migrations is easy to change | Yes, in each place | Only in some places |
| migrations is clear | Yes, in each place | Only in some places |
| migrations is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the reviewer has migrations that is not complete.
After:  the title has migrations that is complete.
```

## Test steps

Keep test steps specific. It keeps the result the same each time. List each place where the change touches test steps. It keeps the result the same each time. Move test steps then, then write one line about what you found.

Steps:

1. Split test steps at the end, then write one line about what you found.
2. Remove the test steps in the title, and make sure that each one is complete.
3. Keep test steps specific. Without it, two people get two different answers.
4. Rewrite each place where the change touches test steps. Most mistakes of this kind are easy to fix early.
5. Shorten test steps then, then write one line about what you found.
6. Shorten the test steps in the reviewer, and make sure that each one is short.
7. When the description changes test steps, group the result at the end.
8. When the diff changes test steps, move the result before you finish.

| Check | Good | Needs work |
|---|---|---|
| test steps is specific | Yes, in each place | Only in some places |
| test steps is easy to test | Yes, in each place | Only in some places |
| test steps is specific | Yes, in each place | Only in some places |
| test steps is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the change has test steps that is not safe.
After:  the title has test steps that is useful.
```
