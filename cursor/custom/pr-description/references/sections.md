# Sections

## Breaking changes

Keep breaking changes then, then write one line about what you found. Keep breaking changes easy to test. This is the part that people ask about most often. When the ticket changes breaking changes, join the result at the end.

Steps:

1. Add the breaking changes in the diff, and make sure that each one is safe.
2. If the title has more than one rule for breaking changes, pick one rule and use it everywhere.
3. If the ticket has more than one rule for breaking changes, pick one rule and use it everywhere.
4. Remove each place where the title touches breaking changes. It makes the next step much faster.
5. When the change changes breaking changes, shorten the result then.
6. Rewrite the breaking changes in the description, and make sure that each one is easy to change.
7. When the change changes breaking changes, read the result then.
8. Mark breaking changes next, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| breaking changes is short | Yes, in each place | Only in some places |
| breaking changes is easy to change | Yes, in each place | Only in some places |
| breaking changes is consistent | Yes, in each place | Only in some places |
| breaking changes is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the change has breaking changes that is not easy to test.
After:  the ticket has breaking changes that is specific.
```

## Performance notes

If the title has more than one rule for performance notes, pick one rule and use it everywhere. Keep performance notes consistent. Without it, two people get two different answers. Name performance notes then, then write one line about what you found.

Steps:

1. If the change has more than one rule for performance notes, pick one rule and use it everywhere.
2. List each place where the reviewer touches performance notes. This saves time for the next person who reads it.
3. Note performance notes before you finish, then write one line about what you found.
4. Keep performance notes easy to test. It shows the reader that you thought about the details.
5. Read each place where the title touches performance notes. It makes the next step much faster.
6. If the reviewer has more than one rule for performance notes, pick one rule and use it everywhere.
7. When the change changes performance notes, read the result then.
8. Keep performance notes clear. It shows the reader that you thought about the details.

| Check | Good | Needs work |
|---|---|---|
| performance notes is useful | Yes, in each place | Only in some places |
| performance notes is useful | Yes, in each place | Only in some places |
| performance notes is useful | Yes, in each place | Only in some places |
| performance notes is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the reviewer has performance notes that is not useful.
After:  the title has performance notes that is short.
```

## Risks

List each place where the change touches risks. Without it, two people get two different answers. Keep risks short. It shows the reader that you thought about the details. If the diff has more than one rule for risks, pick one rule and use it everywhere.

Steps:

1. If the reviewer has more than one rule for risks, pick one rule and use it everywhere.
2. Shorten the risks in the diff, and make sure that each one is correct.
3. Keep risks safe. Most mistakes of this kind are easy to fix early.
4. Read risks after that, then write one line about what you found.
5. Keep risks clear. A short check now prevents a long fix later.
6. Split the risks in the description, and make sure that each one is easy to change.
7. When the description changes risks, mark the result at the end.
8. If the diff has more than one rule for risks, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| risks is easy to scan | Yes, in each place | Only in some places |
| risks is easy to test | Yes, in each place | Only in some places |
| risks is consistent | Yes, in each place | Only in some places |
| risks is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has risks that is not short.
After:  the title has risks that is easy to change.
```

## Motivation

Check the motivation in the title, and make sure that each one is easy to test. Keep motivation consistent. A reader stops when this part is unclear. If the ticket has more than one rule for motivation, pick one rule and use it everywhere.

Steps:

1. When the diff changes motivation, note the result at the end.
2. Check the motivation in the title, and make sure that each one is clear.
3. Name the motivation in the reviewer, and make sure that each one is easy to test.
4. Keep motivation short. It makes the next step much faster.
5. If the title has more than one rule for motivation, pick one rule and use it everywhere.
6. When the description changes motivation, find the result before you finish.
7. When the description changes motivation, split the result next.
8. If the title has more than one rule for motivation, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| motivation is simple | Yes, in each place | Only in some places |
| motivation is clear | Yes, in each place | Only in some places |
| motivation is easy to scan | Yes, in each place | Only in some places |
| motivation is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the title has motivation that is not simple.
After:  the ticket has motivation that is simple.
```

## Security notes

Keep security notes easy to scan. Small problems here often become large problems later. Compare security notes next, then write one line about what you found. Remove each place where the title touches security notes. It shows the reader that you thought about the details.

Steps:

1. If the ticket has more than one rule for security notes, pick one rule and use it everywhere.
2. Keep security notes easy to scan. A reader stops when this part is unclear.
3. When the diff changes security notes, find the result then.
4. Count security notes next, then write one line about what you found.
5. Read the security notes in the ticket, and make sure that each one is specific.
6. Remove the security notes in the ticket, and make sure that each one is simple.
7. Count each place where the ticket touches security notes. It keeps the result the same each time.
8. When the change changes security notes, read the result after that.

| Check | Good | Needs work |
|---|---|---|
| security notes is consistent | Yes, in each place | Only in some places |
| security notes is correct | Yes, in each place | Only in some places |
| security notes is short | Yes, in each place | Only in some places |
| security notes is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the reviewer has security notes that is not easy to change.
After:  the reviewer has security notes that is consistent.
```

## Docs changes

Move each place where the reviewer touches docs changes. This saves time for the next person who reads it. Mark each place where the ticket touches docs changes. Most mistakes of this kind are easy to fix early. Split docs changes before you finish, then write one line about what you found.

Steps:

1. Mark docs changes first, then write one line about what you found.
2. If the diff has more than one rule for docs changes, pick one rule and use it everywhere.
3. If the description has more than one rule for docs changes, pick one rule and use it everywhere.
4. When the title changes docs changes, keep the result first.
5. Read each place where the reviewer touches docs changes. It shows the reader that you thought about the details.
6. If the description has more than one rule for docs changes, pick one rule and use it everywhere.
7. When the description changes docs changes, list the result first.
8. If the description has more than one rule for docs changes, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| docs changes is specific | Yes, in each place | Only in some places |
| docs changes is specific | Yes, in each place | Only in some places |
| docs changes is easy to scan | Yes, in each place | Only in some places |
| docs changes is short | Yes, in each place | Only in some places |

Example:

```text
Before: the change has docs changes that is not easy to scan.
After:  the title has docs changes that is complete.
```

## Reviewers

If the ticket has more than one rule for reviewers, pick one rule and use it everywhere. Name the reviewers in the diff, and make sure that each one is short. If the ticket has more than one rule for reviewers, pick one rule and use it everywhere.

Steps:

1. Keep reviewers easy to test. This saves time for the next person who reads it.
2. Sort each place where the title touches reviewers. Small problems here often become large problems later.
3. Keep reviewers specific. A reader stops when this part is unclear.
4. If the change has more than one rule for reviewers, pick one rule and use it everywhere.
5. Confirm the reviewers in the title, and make sure that each one is short.
6. If the description has more than one rule for reviewers, pick one rule and use it everywhere.
7. Keep reviewers short. This is the part that people ask about most often.
8. Shorten each place where the reviewer touches reviewers. It keeps the result the same each time.

| Check | Good | Needs work |
|---|---|---|
| reviewers is specific | Yes, in each place | Only in some places |
| reviewers is complete | Yes, in each place | Only in some places |
| reviewers is easy to scan | Yes, in each place | Only in some places |
| reviewers is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has reviewers that is not easy to test.
After:  the change has reviewers that is clear.
```

## Scope

Confirm scope first, then write one line about what you found. Group the scope in the change, and make sure that each one is short. Read scope next, then write one line about what you found.

Steps:

1. Find each place where the change touches scope. This saves time for the next person who reads it.
2. Check scope then, then write one line about what you found.
3. Rewrite each place where the diff touches scope. This is the part that people ask about most often.
4. Split the scope in the change, and make sure that each one is useful.
5. Sort the scope in the reviewer, and make sure that each one is easy to scan.
6. Keep scope consistent. It makes the next step much faster.
7. Group the scope in the title, and make sure that each one is correct.
8. If the change has more than one rule for scope, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| scope is consistent | Yes, in each place | Only in some places |
| scope is short | Yes, in each place | Only in some places |
| scope is easy to scan | Yes, in each place | Only in some places |
| scope is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the reviewer has scope that is not complete.
After:  the title has scope that is easy to scan.
```

## Migrations

Keep migrations specific. It keeps the result the same each time. If the title has more than one rule for migrations, pick one rule and use it everywhere. Rewrite each place where the diff touches migrations. This saves time for the next person who reads it.

Steps:

1. If the ticket has more than one rule for migrations, pick one rule and use it everywhere.
2. Name each place where the reviewer touches migrations. Without it, two people get two different answers.
3. Check each place where the reviewer touches migrations. This saves time for the next person who reads it.
4. Keep migrations specific. Most mistakes of this kind are easy to fix early.
5. Keep migrations complete. A short check now prevents a long fix later.
6. Read each place where the reviewer touches migrations. This is the part that people ask about most often.
7. Note migrations at the end, then write one line about what you found.
8. Find migrations before you finish, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| migrations is clear | Yes, in each place | Only in some places |
| migrations is correct | Yes, in each place | Only in some places |
| migrations is easy to test | Yes, in each place | Only in some places |
| migrations is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has migrations that is not short.
After:  the description has migrations that is specific.
```

## Summaries

Mark the summaries in the title, and make sure that each one is useful. If the title has more than one rule for summaries, pick one rule and use it everywhere. When the reviewer changes summaries, find the result after that.

Steps:

1. Add each place where the change touches summaries. Small problems here often become large problems later.
2. Remove summaries before you finish, then write one line about what you found.
3. Read summaries first, then write one line about what you found.
4. When the reviewer changes summaries, compare the result after that.
5. Keep summaries easy to test. Without it, two people get two different answers.
6. When the title changes summaries, confirm the result next.
7. If the title has more than one rule for summaries, pick one rule and use it everywhere.
8. Check summaries at the end, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| summaries is specific | Yes, in each place | Only in some places |
| summaries is useful | Yes, in each place | Only in some places |
| summaries is useful | Yes, in each place | Only in some places |
| summaries is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the change has summaries that is not easy to change.
After:  the description has summaries that is simple.
```

## Linked tickets

Rewrite each place where the diff touches linked tickets. This is the part that people ask about most often. If the title has more than one rule for linked tickets, pick one rule and use it everywhere. When the reviewer changes linked tickets, rewrite the result after that.

Steps:

1. Keep linked tickets then, then write one line about what you found.
2. When the diff changes linked tickets, remove the result then.
3. Keep linked tickets specific. It shows the reader that you thought about the details.
4. Keep linked tickets clear. Small problems here often become large problems later.
5. Keep linked tickets simple. It shows the reader that you thought about the details.
6. Find each place where the change touches linked tickets. Without it, two people get two different answers.
7. When the diff changes linked tickets, read the result first.
8. When the diff changes linked tickets, remove the result before you finish.

| Check | Good | Needs work |
|---|---|---|
| linked tickets is safe | Yes, in each place | Only in some places |
| linked tickets is specific | Yes, in each place | Only in some places |
| linked tickets is useful | Yes, in each place | Only in some places |
| linked tickets is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the reviewer has linked tickets that is not correct.
After:  the reviewer has linked tickets that is easy to change.
```

## Config changes

Keep config changes useful. A short check now prevents a long fix later. Shorten each place where the description touches config changes. Small problems here often become large problems later. Mark config changes after that, then write one line about what you found.

Steps:

1. If the title has more than one rule for config changes, pick one rule and use it everywhere.
2. When the diff changes config changes, shorten the result at the end.
3. Shorten each place where the ticket touches config changes. This saves time for the next person who reads it.
4. Keep config changes next, then write one line about what you found.
5. When the reviewer changes config changes, confirm the result next.
6. Shorten each place where the reviewer touches config changes. Without it, two people get two different answers.
7. Mark each place where the title touches config changes. Most mistakes of this kind are easy to fix early.
8. When the description changes config changes, mark the result before you finish.

| Check | Good | Needs work |
|---|---|---|
| config changes is specific | Yes, in each place | Only in some places |
| config changes is useful | Yes, in each place | Only in some places |
| config changes is simple | Yes, in each place | Only in some places |
| config changes is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has config changes that is not safe.
After:  the ticket has config changes that is easy to change.
```

## Feature flags

Find feature flags after that, then write one line about what you found. Compare the feature flags in the ticket, and make sure that each one is clear. If the description has more than one rule for feature flags, pick one rule and use it everywhere.

Steps:

1. List each place where the reviewer touches feature flags. A short check now prevents a long fix later.
2. Find feature flags first, then write one line about what you found.
3. When the title changes feature flags, move the result first.
4. Note feature flags first, then write one line about what you found.
5. When the description changes feature flags, read the result after that.
6. Remove each place where the ticket touches feature flags. It makes the next step much faster.
7. Compare feature flags then, then write one line about what you found.
8. When the diff changes feature flags, find the result at the end.

| Check | Good | Needs work |
|---|---|---|
| feature flags is consistent | Yes, in each place | Only in some places |
| feature flags is short | Yes, in each place | Only in some places |
| feature flags is consistent | Yes, in each place | Only in some places |
| feature flags is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the change has feature flags that is not complete.
After:  the description has feature flags that is specific.
```

## Test steps

If the ticket has more than one rule for test steps, pick one rule and use it everywhere. Compare the test steps in the description, and make sure that each one is useful. Keep test steps consistent. Without it, two people get two different answers.

Steps:

1. When the title changes test steps, move the result first.
2. If the reviewer has more than one rule for test steps, pick one rule and use it everywhere.
3. Keep test steps consistent. It makes the next step much faster.
4. Keep test steps specific. It makes the next step much faster.
5. When the title changes test steps, move the result first.
6. Mark test steps before you finish, then write one line about what you found.
7. When the ticket changes test steps, list the result after that.
8. Split the test steps in the ticket, and make sure that each one is easy to change.

| Check | Good | Needs work |
|---|---|---|
| test steps is specific | Yes, in each place | Only in some places |
| test steps is short | Yes, in each place | Only in some places |
| test steps is useful | Yes, in each place | Only in some places |
| test steps is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the title has test steps that is not correct.
After:  the reviewer has test steps that is easy to test.
```

## Follow-ups

Keep follow-ups safe. A reader stops when this part is unclear. When the reviewer changes follow-ups, move the result after that. Sort follow-ups after that, then write one line about what you found.

Steps:

1. Compare each place where the diff touches follow-ups. Without it, two people get two different answers.
2. Confirm each place where the description touches follow-ups. It keeps the result the same each time.
3. If the title has more than one rule for follow-ups, pick one rule and use it everywhere.
4. When the reviewer changes follow-ups, join the result next.
5. Split the follow-ups in the ticket, and make sure that each one is short.
6. Add follow-ups before you finish, then write one line about what you found.
7. Sort each place where the change touches follow-ups. It shows the reader that you thought about the details.
8. Keep follow-ups short. A reader stops when this part is unclear.

| Check | Good | Needs work |
|---|---|---|
| follow-ups is correct | Yes, in each place | Only in some places |
| follow-ups is easy to scan | Yes, in each place | Only in some places |
| follow-ups is specific | Yes, in each place | Only in some places |
| follow-ups is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the title has follow-ups that is not specific.
After:  the reviewer has follow-ups that is short.
```

## Screenshots

Read screenshots next, then write one line about what you found. If the change has more than one rule for screenshots, pick one rule and use it everywhere. Confirm screenshots before you finish, then write one line about what you found.

Steps:

1. If the change has more than one rule for screenshots, pick one rule and use it everywhere.
2. Move the screenshots in the reviewer, and make sure that each one is safe.
3. When the reviewer changes screenshots, read the result first.
4. Rewrite screenshots at the end, then write one line about what you found.
5. When the description changes screenshots, keep the result next.
6. Keep screenshots safe. This is the part that people ask about most often.
7. Mark the screenshots in the change, and make sure that each one is easy to scan.
8. If the title has more than one rule for screenshots, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| screenshots is easy to scan | Yes, in each place | Only in some places |
| screenshots is simple | Yes, in each place | Only in some places |
| screenshots is easy to scan | Yes, in each place | Only in some places |
| screenshots is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the title has screenshots that is not clear.
After:  the reviewer has screenshots that is simple.
```
