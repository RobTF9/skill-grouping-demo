---
name: pr-description
description: Write a pull request description from a diff.
---

# Pull request description

1. Summary: what the change does, in two sentences.

## Scope

If the title has more than one rule for scope, pick one rule and use it everywhere. Keep scope useful. Without it, two people get two different answers. If the reviewer has more than one rule for scope, pick one rule and use it everywhere.

Steps:

1. Keep the scope in the diff, and make sure that each one is complete.
2. Keep scope safe. A short check now prevents a long fix later.
3. Compare scope at the end, then write one line about what you found.
4. Count scope at the end, then write one line about what you found.
5. If the title has more than one rule for scope, pick one rule and use it everywhere.
6. Confirm each place where the reviewer touches scope. It shows the reader that you thought about the details.
7. When the change changes scope, count the result next.
8. Find each place where the change touches scope. Most mistakes of this kind are easy to fix early.

| Check | Good | Needs work |
|---|---|---|
| scope is easy to test | Yes, in each place | Only in some places |
| scope is specific | Yes, in each place | Only in some places |
| scope is safe | Yes, in each place | Only in some places |
| scope is short | Yes, in each place | Only in some places |

Example:

```text
Before: the title has scope that is not useful.
After:  the description has scope that is clear.
```

## Security notes

Rewrite security notes before you finish, then write one line about what you found. Keep security notes short. Small problems here often become large problems later. When the diff changes security notes, rewrite the result next.

Steps:

1. Confirm the security notes in the description, and make sure that each one is useful.
2. Keep security notes specific. It makes the next step much faster.
3. Find each place where the ticket touches security notes. This saves time for the next person who reads it.
4. When the diff changes security notes, split the result first.
5. When the title changes security notes, mark the result before you finish.
6. When the title changes security notes, rewrite the result before you finish.
7. Find the security notes in the change, and make sure that each one is short.
8. When the title changes security notes, keep the result next.

| Check | Good | Needs work |
|---|---|---|
| security notes is useful | Yes, in each place | Only in some places |
| security notes is easy to change | Yes, in each place | Only in some places |
| security notes is specific | Yes, in each place | Only in some places |
| security notes is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the description has security notes that is not safe.
After:  the description has security notes that is specific.
```

## Follow-ups

Compare the follow-ups in the reviewer, and make sure that each one is correct. When the diff changes follow-ups, shorten the result first. Group the follow-ups in the description, and make sure that each one is useful.

Steps:

1. Name follow-ups first, then write one line about what you found.
2. If the title has more than one rule for follow-ups, pick one rule and use it everywhere.
3. If the title has more than one rule for follow-ups, pick one rule and use it everywhere.
4. If the description has more than one rule for follow-ups, pick one rule and use it everywhere.
5. When the diff changes follow-ups, check the result after that.
6. Keep follow-ups complete. A reader stops when this part is unclear.
7. If the ticket has more than one rule for follow-ups, pick one rule and use it everywhere.
8. Read the follow-ups in the change, and make sure that each one is easy to scan.

| Check | Good | Needs work |
|---|---|---|
| follow-ups is safe | Yes, in each place | Only in some places |
| follow-ups is correct | Yes, in each place | Only in some places |
| follow-ups is safe | Yes, in each place | Only in some places |
| follow-ups is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has follow-ups that is not easy to change.
After:  the description has follow-ups that is easy to test.
```

## Performance notes

Keep performance notes specific. It shows the reader that you thought about the details. If the title has more than one rule for performance notes, pick one rule and use it everywhere. Rewrite each place where the title touches performance notes. This saves time for the next person who reads it.

Steps:

1. Add each place where the description touches performance notes. It shows the reader that you thought about the details.
2. Split performance notes first, then write one line about what you found.
3. When the description changes performance notes, remove the result then.
4. Keep performance notes complete. This is the part that people ask about most often.
5. If the title has more than one rule for performance notes, pick one rule and use it everywhere.
6. Shorten performance notes at the end, then write one line about what you found.
7. When the reviewer changes performance notes, count the result before you finish.
8. If the reviewer has more than one rule for performance notes, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| performance notes is consistent | Yes, in each place | Only in some places |
| performance notes is easy to scan | Yes, in each place | Only in some places |
| performance notes is specific | Yes, in each place | Only in some places |
| performance notes is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the description has performance notes that is not consistent.
After:  the description has performance notes that is easy to scan.
```

## Breaking changes

Mark breaking changes after that, then write one line about what you found. When the ticket changes breaking changes, read the result first. Mark each place where the diff touches breaking changes. It keeps the result the same each time.

Steps:

1. Keep breaking changes useful. A reader stops when this part is unclear.
2. Keep breaking changes useful. It makes the next step much faster.
3. Rewrite breaking changes then, then write one line about what you found.
4. When the change changes breaking changes, mark the result first.
5. Note breaking changes before you finish, then write one line about what you found.
6. Count each place where the ticket touches breaking changes. Small problems here often become large problems later.
7. Keep breaking changes clear. This is the part that people ask about most often.
8. Split the breaking changes in the reviewer, and make sure that each one is consistent.

| Check | Good | Needs work |
|---|---|---|
| breaking changes is simple | Yes, in each place | Only in some places |
| breaking changes is simple | Yes, in each place | Only in some places |
| breaking changes is useful | Yes, in each place | Only in some places |
| breaking changes is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has breaking changes that is not simple.
After:  the reviewer has breaking changes that is easy to test.
```

## Rollbacks

When the change changes rollbacks, list the result before you finish. If the diff has more than one rule for rollbacks, pick one rule and use it everywhere. Keep rollbacks complete. This saves time for the next person who reads it.

Steps:

1. Keep rollbacks complete. It makes the next step much faster.
2. Rewrite each place where the description touches rollbacks. This saves time for the next person who reads it.
3. Keep each place where the change touches rollbacks. Small problems here often become large problems later.
4. Sort each place where the description touches rollbacks. It shows the reader that you thought about the details.
5. Split each place where the reviewer touches rollbacks. It makes the next step much faster.
6. Remove the rollbacks in the title, and make sure that each one is simple.
7. Add each place where the change touches rollbacks. It makes the next step much faster.
8. List each place where the ticket touches rollbacks. This saves time for the next person who reads it.

| Check | Good | Needs work |
|---|---|---|
| rollbacks is specific | Yes, in each place | Only in some places |
| rollbacks is safe | Yes, in each place | Only in some places |
| rollbacks is safe | Yes, in each place | Only in some places |
| rollbacks is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the description has rollbacks that is not simple.
After:  the ticket has rollbacks that is specific.
```

## Risks

List risks first, then write one line about what you found. Split each place where the title touches risks. It shows the reader that you thought about the details. Keep the risks in the reviewer, and make sure that each one is easy to test.

Steps:

1. When the reviewer changes risks, shorten the result then.
2. If the change has more than one rule for risks, pick one rule and use it everywhere.
3. Read the risks in the reviewer, and make sure that each one is complete.
4. Keep risks consistent. A short check now prevents a long fix later.
5. Count the risks in the ticket, and make sure that each one is safe.
6. When the description changes risks, sort the result first.
7. Note each place where the diff touches risks. It shows the reader that you thought about the details.
8. Rewrite the risks in the title, and make sure that each one is short.

| Check | Good | Needs work |
|---|---|---|
| risks is clear | Yes, in each place | Only in some places |
| risks is simple | Yes, in each place | Only in some places |
| risks is easy to change | Yes, in each place | Only in some places |
| risks is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the title has risks that is not consistent.
After:  the diff has risks that is easy to change.
```

## Test steps

Compare the test steps in the reviewer, and make sure that each one is specific. Keep test steps short. A short check now prevents a long fix later. List test steps then, then write one line about what you found.

Steps:

1. Group each place where the diff touches test steps. It keeps the result the same each time.
2. Name test steps then, then write one line about what you found.
3. Split each place where the change touches test steps. It shows the reader that you thought about the details.
4. Name each place where the title touches test steps. Without it, two people get two different answers.
5. List each place where the reviewer touches test steps. A reader stops when this part is unclear.
6. If the diff has more than one rule for test steps, pick one rule and use it everywhere.
7. Sort test steps after that, then write one line about what you found.
8. Add the test steps in the reviewer, and make sure that each one is easy to change.

| Check | Good | Needs work |
|---|---|---|
| test steps is clear | Yes, in each place | Only in some places |
| test steps is short | Yes, in each place | Only in some places |
| test steps is correct | Yes, in each place | Only in some places |
| test steps is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the change has test steps that is not clear.
After:  the reviewer has test steps that is easy to scan.
```

## Reviewers

If the ticket has more than one rule for reviewers, pick one rule and use it everywhere. Sort each place where the change touches reviewers. A reader stops when this part is unclear. When the change changes reviewers, remove the result then.

Steps:

1. Count the reviewers in the reviewer, and make sure that each one is complete.
2. Keep reviewers correct. Without it, two people get two different answers.
3. Count reviewers next, then write one line about what you found.
4. Remove the reviewers in the ticket, and make sure that each one is correct.
5. When the diff changes reviewers, compare the result before you finish.
6. If the description has more than one rule for reviewers, pick one rule and use it everywhere.
7. Keep reviewers easy to scan. It shows the reader that you thought about the details.
8. Group the reviewers in the reviewer, and make sure that each one is useful.

| Check | Good | Needs work |
|---|---|---|
| reviewers is easy to scan | Yes, in each place | Only in some places |
| reviewers is easy to scan | Yes, in each place | Only in some places |
| reviewers is easy to test | Yes, in each place | Only in some places |
| reviewers is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the ticket has reviewers that is not simple.
After:  the title has reviewers that is easy to change.
```

## Motivation

Keep motivation safe. A reader stops when this part is unclear. Find motivation at the end, then write one line about what you found. Compare motivation first, then write one line about what you found.

Steps:

1. Find motivation next, then write one line about what you found.
2. Split the motivation in the reviewer, and make sure that each one is consistent.
3. When the description changes motivation, sort the result at the end.
4. Keep motivation specific. It keeps the result the same each time.
5. If the diff has more than one rule for motivation, pick one rule and use it everywhere.
6. Rewrite motivation next, then write one line about what you found.
7. When the reviewer changes motivation, find the result after that.
8. Remove the motivation in the description, and make sure that each one is useful.

| Check | Good | Needs work |
|---|---|---|
| motivation is specific | Yes, in each place | Only in some places |
| motivation is safe | Yes, in each place | Only in some places |
| motivation is consistent | Yes, in each place | Only in some places |
| motivation is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has motivation that is not easy to test.
After:  the change has motivation that is easy to change.
```

## Feature flags

Group each place where the ticket touches feature flags. This saves time for the next person who reads it. If the title has more than one rule for feature flags, pick one rule and use it everywhere. Find the feature flags in the change, and make sure that each one is easy to test.

Steps:

1. Group the feature flags in the description, and make sure that each one is complete.
2. Split each place where the title touches feature flags. Small problems here often become large problems later.
3. Count each place where the diff touches feature flags. A short check now prevents a long fix later.
4. If the ticket has more than one rule for feature flags, pick one rule and use it everywhere.
5. When the change changes feature flags, add the result next.
6. Split feature flags at the end, then write one line about what you found.
7. Keep feature flags simple. This saves time for the next person who reads it.
8. Sort the feature flags in the reviewer, and make sure that each one is easy to scan.

| Check | Good | Needs work |
|---|---|---|
| feature flags is clear | Yes, in each place | Only in some places |
| feature flags is easy to test | Yes, in each place | Only in some places |
| feature flags is useful | Yes, in each place | Only in some places |
| feature flags is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the ticket has feature flags that is not useful.
After:  the ticket has feature flags that is complete.
```

## Config changes

Rewrite config changes after that, then write one line about what you found. Rewrite the config changes in the reviewer, and make sure that each one is safe. Move the config changes in the description, and make sure that each one is easy to test.

Steps:

1. Keep config changes useful. A reader stops when this part is unclear.
2. List config changes after that, then write one line about what you found.
3. List the config changes in the ticket, and make sure that each one is consistent.
4. Find config changes first, then write one line about what you found.
5. If the reviewer has more than one rule for config changes, pick one rule and use it everywhere.
6. Keep config changes safe. It keeps the result the same each time.
7. If the diff has more than one rule for config changes, pick one rule and use it everywhere.
8. Name config changes before you finish, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| config changes is easy to scan | Yes, in each place | Only in some places |
| config changes is specific | Yes, in each place | Only in some places |
| config changes is useful | Yes, in each place | Only in some places |
| config changes is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has config changes that is not safe.
After:  the description has config changes that is complete.
```

## Screenshots

Sort each place where the change touches screenshots. Most mistakes of this kind are easy to fix early. Note the screenshots in the title, and make sure that each one is complete. If the description has more than one rule for screenshots, pick one rule and use it everywhere.

Steps:

1. Keep screenshots safe. Small problems here often become large problems later.
2. Keep screenshots consistent. Without it, two people get two different answers.
3. Compare the screenshots in the ticket, and make sure that each one is short.
4. If the title has more than one rule for screenshots, pick one rule and use it everywhere.
5. Keep screenshots clear. This saves time for the next person who reads it.
6. Keep screenshots safe. This saves time for the next person who reads it.
7. When the reviewer changes screenshots, compare the result next.
8. Join screenshots before you finish, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| screenshots is easy to test | Yes, in each place | Only in some places |
| screenshots is short | Yes, in each place | Only in some places |
| screenshots is useful | Yes, in each place | Only in some places |
| screenshots is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the ticket has screenshots that is not easy to change.
After:  the change has screenshots that is easy to scan.
```

## Docs changes

If the reviewer has more than one rule for docs changes, pick one rule and use it everywhere. When the description changes docs changes, check the result at the end. Remove each place where the change touches docs changes. This saves time for the next person who reads it.

Steps:

1. If the title has more than one rule for docs changes, pick one rule and use it everywhere.
2. Remove docs changes first, then write one line about what you found.
3. Group docs changes after that, then write one line about what you found.
4. When the reviewer changes docs changes, keep the result next.
5. When the change changes docs changes, group the result at the end.
6. If the diff has more than one rule for docs changes, pick one rule and use it everywhere.
7. Read the docs changes in the ticket, and make sure that each one is easy to scan.
8. Check docs changes at the end, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| docs changes is clear | Yes, in each place | Only in some places |
| docs changes is consistent | Yes, in each place | Only in some places |
| docs changes is simple | Yes, in each place | Only in some places |
| docs changes is short | Yes, in each place | Only in some places |

Example:

```text
Before: the change has docs changes that is not safe.
After:  the description has docs changes that is easy to change.
```

## Summaries

When the reviewer changes summaries, keep the result at the end. Group the summaries in the diff, and make sure that each one is short. Find the summaries in the description, and make sure that each one is complete.

Steps:

1. If the description has more than one rule for summaries, pick one rule and use it everywhere.
2. List the summaries in the reviewer, and make sure that each one is clear.
3. If the change has more than one rule for summaries, pick one rule and use it everywhere.
4. Confirm each place where the change touches summaries. This saves time for the next person who reads it.
5. Remove summaries at the end, then write one line about what you found.
6. Confirm the summaries in the reviewer, and make sure that each one is useful.
7. When the ticket changes summaries, group the result after that.
8. When the ticket changes summaries, read the result at the end.

| Check | Good | Needs work |
|---|---|---|
| summaries is specific | Yes, in each place | Only in some places |
| summaries is consistent | Yes, in each place | Only in some places |
| summaries is short | Yes, in each place | Only in some places |
| summaries is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the reviewer has summaries that is not consistent.
After:  the title has summaries that is specific.
```

## Linked tickets

Check the linked tickets in the reviewer, and make sure that each one is correct. Keep linked tickets at the end, then write one line about what you found. Keep linked tickets before you finish, then write one line about what you found.

Steps:

1. Read the linked tickets in the description, and make sure that each one is complete.
2. Keep linked tickets complete. A reader stops when this part is unclear.
3. Confirm the linked tickets in the diff, and make sure that each one is clear.
4. When the title changes linked tickets, move the result after that.
5. When the title changes linked tickets, name the result next.
6. Name each place where the change touches linked tickets. Most mistakes of this kind are easy to fix early.
7. Group linked tickets first, then write one line about what you found.
8. If the title has more than one rule for linked tickets, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| linked tickets is clear | Yes, in each place | Only in some places |
| linked tickets is useful | Yes, in each place | Only in some places |
| linked tickets is easy to scan | Yes, in each place | Only in some places |
| linked tickets is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the ticket has linked tickets that is not easy to test.
After:  the ticket has linked tickets that is short.
```

## Migrations

When the diff changes migrations, mark the result next. Split each place where the diff touches migrations. Most mistakes of this kind are easy to fix early. Keep migrations consistent. Without it, two people get two different answers.

Steps:

1. Join the migrations in the diff, and make sure that each one is specific.
2. Rewrite migrations after that, then write one line about what you found.
3. Keep migrations easy to scan. Without it, two people get two different answers.
4. Read the migrations in the diff, and make sure that each one is clear.
5. Keep migrations complete. It makes the next step much faster.
6. If the ticket has more than one rule for migrations, pick one rule and use it everywhere.
7. Group each place where the diff touches migrations. Without it, two people get two different answers.
8. When the diff changes migrations, mark the result after that.

| Check | Good | Needs work |
|---|---|---|
| migrations is clear | Yes, in each place | Only in some places |
| migrations is easy to scan | Yes, in each place | Only in some places |
| migrations is easy to scan | Yes, in each place | Only in some places |
| migrations is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the ticket has migrations that is not easy to change.
After:  the description has migrations that is correct.
```

## Screenshots (pass 2)

If the title has more than one rule for screenshots (pass 2), pick one rule and use it everywhere. Split each place where the diff touches screenshots (pass 2). It shows the reader that you thought about the details. When the description changes screenshots (pass 2), check the result first.

Steps:

1. When the diff changes screenshots (pass 2), join the result next.
2. List the screenshots (pass 2) in the reviewer, and make sure that each one is consistent.
3. Keep screenshots (pass 2) clear. Small problems here often become large problems later.
4. Confirm each place where the description touches screenshots (pass 2). It makes the next step much faster.
5. Shorten the screenshots (pass 2) in the reviewer, and make sure that each one is safe.
6. Remove the screenshots (pass 2) in the reviewer, and make sure that each one is clear.
7. Keep screenshots (pass 2) at the end, then write one line about what you found.
8. If the title has more than one rule for screenshots (pass 2), pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| screenshots (pass 2) is specific | Yes, in each place | Only in some places |
| screenshots (pass 2) is safe | Yes, in each place | Only in some places |
| screenshots (pass 2) is correct | Yes, in each place | Only in some places |
| screenshots (pass 2) is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the ticket has screenshots (pass 2) that is not consistent.
After:  the title has screenshots (pass 2) that is useful.
```

## Summaries (pass 2)

When the title changes summaries (pass 2), add the result next. Note summaries (pass 2) next, then write one line about what you found. Check summaries (pass 2) at the end, then write one line about what you found.

Steps:

1. Keep summaries (pass 2) at the end, then write one line about what you found.
2. When the description changes summaries (pass 2), read the result at the end.
3. Keep summaries (pass 2) then, then write one line about what you found.
4. If the change has more than one rule for summaries (pass 2), pick one rule and use it everywhere.
5. Name each place where the title touches summaries (pass 2). It keeps the result the same each time.
6. Count summaries (pass 2) after that, then write one line about what you found.
7. Split the summaries (pass 2) in the title, and make sure that each one is easy to test.
8. List summaries (pass 2) before you finish, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| summaries (pass 2) is short | Yes, in each place | Only in some places |
| summaries (pass 2) is short | Yes, in each place | Only in some places |
| summaries (pass 2) is specific | Yes, in each place | Only in some places |
| summaries (pass 2) is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the reviewer has summaries (pass 2) that is not clear.
After:  the title has summaries (pass 2) that is simple.
```

## Risks (pass 2)

Count risks (pass 2) next, then write one line about what you found. When the description changes risks (pass 2), group the result next. Group the risks (pass 2) in the description, and make sure that each one is safe.

Steps:

1. Compare risks (pass 2) then, then write one line about what you found.
2. When the ticket changes risks (pass 2), compare the result at the end.
3. Remove each place where the diff touches risks (pass 2). This is the part that people ask about most often.
4. Keep risks (pass 2) simple. It keeps the result the same each time.
5. If the change has more than one rule for risks (pass 2), pick one rule and use it everywhere.
6. Keep risks (pass 2) easy to test. Small problems here often become large problems later.
7. Confirm risks (pass 2) first, then write one line about what you found.
8. Mark the risks (pass 2) in the change, and make sure that each one is specific.

| Check | Good | Needs work |
|---|---|---|
| risks (pass 2) is safe | Yes, in each place | Only in some places |
| risks (pass 2) is clear | Yes, in each place | Only in some places |
| risks (pass 2) is safe | Yes, in each place | Only in some places |
| risks (pass 2) is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the reviewer has risks (pass 2) that is not clear.
After:  the ticket has risks (pass 2) that is easy to test.
```

## Reviewers (pass 2)

Name each place where the change touches reviewers (pass 2). Without it, two people get two different answers. Keep the reviewers (pass 2) in the change, and make sure that each one is useful. When the change changes reviewers (pass 2), count the result then.

Steps:

1. Keep reviewers (pass 2) correct. It makes the next step much faster.
2. If the title has more than one rule for reviewers (pass 2), pick one rule and use it everywhere.
3. Remove reviewers (pass 2) before you finish, then write one line about what you found.
4. Keep reviewers (pass 2) easy to test. Most mistakes of this kind are easy to fix early.
5. When the reviewer changes reviewers (pass 2), group the result at the end.
6. Keep reviewers (pass 2) simple. Most mistakes of this kind are easy to fix early.
7. Mark reviewers (pass 2) first, then write one line about what you found.
8. When the title changes reviewers (pass 2), read the result next.

| Check | Good | Needs work |
|---|---|---|
| reviewers (pass 2) is correct | Yes, in each place | Only in some places |
| reviewers (pass 2) is safe | Yes, in each place | Only in some places |
| reviewers (pass 2) is clear | Yes, in each place | Only in some places |
| reviewers (pass 2) is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the reviewer has reviewers (pass 2) that is not easy to scan.
After:  the description has reviewers (pass 2) that is specific.
```

## Performance notes (pass 2)

When the reviewer changes performance notes (pass 2), remove the result after that. Keep performance notes (pass 2) useful. A reader stops when this part is unclear. Keep performance notes (pass 2) easy to test. This saves time for the next person who reads it.

Steps:

1. Keep performance notes (pass 2) safe. It shows the reader that you thought about the details.
2. Shorten each place where the title touches performance notes (pass 2). This saves time for the next person who reads it.
3. Confirm performance notes (pass 2) next, then write one line about what you found.
4. Keep performance notes (pass 2) clear. Most mistakes of this kind are easy to fix early.
5. Check the performance notes (pass 2) in the ticket, and make sure that each one is easy to test.
6. When the change changes performance notes (pass 2), read the result next.
7. Keep performance notes (pass 2) easy to change. It shows the reader that you thought about the details.
8. When the diff changes performance notes (pass 2), list the result next.

| Check | Good | Needs work |
|---|---|---|
| performance notes (pass 2) is easy to test | Yes, in each place | Only in some places |
| performance notes (pass 2) is easy to test | Yes, in each place | Only in some places |
| performance notes (pass 2) is simple | Yes, in each place | Only in some places |
| performance notes (pass 2) is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the reviewer has performance notes (pass 2) that is not easy to test.
After:  the description has performance notes (pass 2) that is specific.
```

## Docs changes (pass 2)

Add each place where the title touches docs changes (pass 2). A short check now prevents a long fix later. List each place where the reviewer touches docs changes (pass 2). Most mistakes of this kind are easy to fix early. Move docs changes (pass 2) then, then write one line about what you found.

Steps:

1. If the title has more than one rule for docs changes (pass 2), pick one rule and use it everywhere.
2. When the reviewer changes docs changes (pass 2), note the result next.
3. If the ticket has more than one rule for docs changes (pass 2), pick one rule and use it everywhere.
4. If the reviewer has more than one rule for docs changes (pass 2), pick one rule and use it everywhere.
5. List each place where the title touches docs changes (pass 2). This saves time for the next person who reads it.
6. Mark each place where the title touches docs changes (pass 2). A short check now prevents a long fix later.
7. If the diff has more than one rule for docs changes (pass 2), pick one rule and use it everywhere.
8. When the description changes docs changes (pass 2), split the result then.

| Check | Good | Needs work |
|---|---|---|
| docs changes (pass 2) is easy to test | Yes, in each place | Only in some places |
| docs changes (pass 2) is clear | Yes, in each place | Only in some places |
| docs changes (pass 2) is safe | Yes, in each place | Only in some places |
| docs changes (pass 2) is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the description has docs changes (pass 2) that is not clear.
After:  the diff has docs changes (pass 2) that is easy to test.
```

## Scope (pass 2)

Count the scope (pass 2) in the title, and make sure that each one is specific. Keep scope (pass 2) short. It makes the next step much faster. Move scope (pass 2) after that, then write one line about what you found.

Steps:

1. Find the scope (pass 2) in the change, and make sure that each one is correct.
2. Remove each place where the reviewer touches scope (pass 2). A reader stops when this part is unclear.
3. Keep scope (pass 2) short. A short check now prevents a long fix later.
4. If the description has more than one rule for scope (pass 2), pick one rule and use it everywhere.
5. If the change has more than one rule for scope (pass 2), pick one rule and use it everywhere.
6. Keep scope (pass 2) specific. Without it, two people get two different answers.
7. When the ticket changes scope (pass 2), find the result at the end.
8. Confirm each place where the change touches scope (pass 2). It shows the reader that you thought about the details.

| Check | Good | Needs work |
|---|---|---|
| scope (pass 2) is clear | Yes, in each place | Only in some places |
| scope (pass 2) is short | Yes, in each place | Only in some places |
| scope (pass 2) is easy to change | Yes, in each place | Only in some places |
| scope (pass 2) is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the title has scope (pass 2) that is not specific.
After:  the title has scope (pass 2) that is easy to change.
```

## Security notes (pass 2)

Mark security notes (pass 2) then, then write one line about what you found. Keep security notes (pass 2) useful. Most mistakes of this kind are easy to fix early. If the ticket has more than one rule for security notes (pass 2), pick one rule and use it everywhere.

Steps:

1. Join the security notes (pass 2) in the description, and make sure that each one is easy to scan.
2. When the title changes security notes (pass 2), note the result then.
3. If the change has more than one rule for security notes (pass 2), pick one rule and use it everywhere.
4. Name security notes (pass 2) first, then write one line about what you found.
5. When the reviewer changes security notes (pass 2), split the result before you finish.
6. Move each place where the change touches security notes (pass 2). It keeps the result the same each time.
7. Split the security notes (pass 2) in the ticket, and make sure that each one is useful.
8. Add the security notes (pass 2) in the reviewer, and make sure that each one is easy to scan.

| Check | Good | Needs work |
|---|---|---|
| security notes (pass 2) is easy to test | Yes, in each place | Only in some places |
| security notes (pass 2) is consistent | Yes, in each place | Only in some places |
| security notes (pass 2) is useful | Yes, in each place | Only in some places |
| security notes (pass 2) is short | Yes, in each place | Only in some places |

Example:

```text
Before: the description has security notes (pass 2) that is not easy to scan.
After:  the diff has security notes (pass 2) that is useful.
```

## Linked tickets (pass 2)

If the ticket has more than one rule for linked tickets (pass 2), pick one rule and use it everywhere. Keep the linked tickets (pass 2) in the ticket, and make sure that each one is easy to scan. When the diff changes linked tickets (pass 2), remove the result next.

Steps:

1. When the description changes linked tickets (pass 2), join the result at the end.
2. If the description has more than one rule for linked tickets (pass 2), pick one rule and use it everywhere.
3. If the title has more than one rule for linked tickets (pass 2), pick one rule and use it everywhere.
4. Split each place where the diff touches linked tickets (pass 2). A short check now prevents a long fix later.
5. Keep linked tickets (pass 2) specific. A reader stops when this part is unclear.
6. When the description changes linked tickets (pass 2), compare the result next.
7. Keep linked tickets (pass 2) short. It makes the next step much faster.
8. Find each place where the title touches linked tickets (pass 2). A reader stops when this part is unclear.

| Check | Good | Needs work |
|---|---|---|
| linked tickets (pass 2) is short | Yes, in each place | Only in some places |
| linked tickets (pass 2) is easy to scan | Yes, in each place | Only in some places |
| linked tickets (pass 2) is correct | Yes, in each place | Only in some places |
| linked tickets (pass 2) is short | Yes, in each place | Only in some places |

Example:

```text
Before: the reviewer has linked tickets (pass 2) that is not correct.
After:  the diff has linked tickets (pass 2) that is specific.
```

## Config changes (pass 2)

When the change changes config changes (pass 2), name the result at the end. Remove the config changes (pass 2) in the description, and make sure that each one is easy to test. When the change changes config changes (pass 2), confirm the result before you finish.

Steps:

1. When the diff changes config changes (pass 2), remove the result next.
2. Add each place where the change touches config changes (pass 2). This is the part that people ask about most often.
3. Mark each place where the diff touches config changes (pass 2). Most mistakes of this kind are easy to fix early.
4. Move config changes (pass 2) after that, then write one line about what you found.
5. When the diff changes config changes (pass 2), read the result first.
6. Confirm config changes (pass 2) before you finish, then write one line about what you found.
7. Keep config changes (pass 2) useful. This saves time for the next person who reads it.
8. Remove each place where the diff touches config changes (pass 2). This saves time for the next person who reads it.

| Check | Good | Needs work |
|---|---|---|
| config changes (pass 2) is complete | Yes, in each place | Only in some places |
| config changes (pass 2) is easy to scan | Yes, in each place | Only in some places |
| config changes (pass 2) is easy to change | Yes, in each place | Only in some places |
| config changes (pass 2) is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the description has config changes (pass 2) that is not easy to test.
After:  the reviewer has config changes (pass 2) that is easy to scan.
```

## Breaking changes (pass 2)

When the ticket changes breaking changes (pass 2), remove the result then. Group each place where the reviewer touches breaking changes (pass 2). This saves time for the next person who reads it. Keep breaking changes (pass 2) useful. Small problems here often become large problems later.

Steps:

1. When the change changes breaking changes (pass 2), keep the result at the end.
2. Note the breaking changes (pass 2) in the diff, and make sure that each one is short.
3. If the diff has more than one rule for breaking changes (pass 2), pick one rule and use it everywhere.
4. List breaking changes (pass 2) then, then write one line about what you found.
5. Count breaking changes (pass 2) then, then write one line about what you found.
6. When the reviewer changes breaking changes (pass 2), name the result first.
7. Compare each place where the description touches breaking changes (pass 2). It shows the reader that you thought about the details.
8. Rewrite each place where the change touches breaking changes (pass 2). A short check now prevents a long fix later.

| Check | Good | Needs work |
|---|---|---|
| breaking changes (pass 2) is easy to test | Yes, in each place | Only in some places |
| breaking changes (pass 2) is useful | Yes, in each place | Only in some places |
| breaking changes (pass 2) is correct | Yes, in each place | Only in some places |
| breaking changes (pass 2) is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has breaking changes (pass 2) that is not complete.
After:  the change has breaking changes (pass 2) that is short.
```

## Motivation (pass 2)

Sort each place where the title touches motivation (pass 2). A reader stops when this part is unclear. When the reviewer changes motivation (pass 2), shorten the result next. When the ticket changes motivation (pass 2), note the result next.

Steps:

1. Add motivation (pass 2) next, then write one line about what you found.
2. Split each place where the change touches motivation (pass 2). A short check now prevents a long fix later.
3. If the diff has more than one rule for motivation (pass 2), pick one rule and use it everywhere.
4. Keep motivation (pass 2) complete. A short check now prevents a long fix later.
5. If the description has more than one rule for motivation (pass 2), pick one rule and use it everywhere.
6. When the reviewer changes motivation (pass 2), list the result at the end.
7. If the change has more than one rule for motivation (pass 2), pick one rule and use it everywhere.
8. When the change changes motivation (pass 2), rewrite the result after that.

| Check | Good | Needs work |
|---|---|---|
| motivation (pass 2) is consistent | Yes, in each place | Only in some places |
| motivation (pass 2) is correct | Yes, in each place | Only in some places |
| motivation (pass 2) is consistent | Yes, in each place | Only in some places |
| motivation (pass 2) is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the ticket has motivation (pass 2) that is not consistent.
After:  the title has motivation (pass 2) that is clear.
```

## Migrations (pass 2)

If the description has more than one rule for migrations (pass 2), pick one rule and use it everywhere. Note the migrations (pass 2) in the change, and make sure that each one is clear. If the description has more than one rule for migrations (pass 2), pick one rule and use it everywhere.

Steps:

1. Add each place where the change touches migrations (pass 2). A short check now prevents a long fix later.
2. If the reviewer has more than one rule for migrations (pass 2), pick one rule and use it everywhere.
3. Keep migrations (pass 2) useful. Without it, two people get two different answers.
4. If the description has more than one rule for migrations (pass 2), pick one rule and use it everywhere.
5. Read migrations (pass 2) next, then write one line about what you found.
6. When the reviewer changes migrations (pass 2), group the result next.
7. Move migrations (pass 2) before you finish, then write one line about what you found.
8. Keep migrations (pass 2) easy to change. This saves time for the next person who reads it.

| Check | Good | Needs work |
|---|---|---|
| migrations (pass 2) is correct | Yes, in each place | Only in some places |
| migrations (pass 2) is complete | Yes, in each place | Only in some places |
| migrations (pass 2) is consistent | Yes, in each place | Only in some places |
| migrations (pass 2) is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the ticket has migrations (pass 2) that is not simple.
After:  the diff has migrations (pass 2) that is specific.
```
