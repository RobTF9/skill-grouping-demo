# Checklist

Use this list for every review. Tick each line in your summary comment.

- Tests cover the change, and they fail without it.
- Names say what the code does, not how it does it.
- Each new function has one job.
- Errors are handled or passed on, never swallowed.
- Inputs from users are checked before use.
- Queries use parameters.
- New endpoints check access.
- Logs carry no secrets and no personal data.
- Loops do not run a query each time.
- Lists from users have a limit.
- Public functions have a short comment that says why they exist.
- The change log names the change, when users can see it.

## More detail

## Memory use

List memory use before you finish, then write one line about what you found. Sort each place where the function touches memory use. Most mistakes of this kind are easy to fix early. Count each place where the interface touches memory use. It makes the next step much faster.

Steps:

1. Find the memory use in the test, and make sure that each one is short.
2. Compare the memory use in the test, and make sure that each one is safe.
3. When the interface changes memory use, mark the result then.
4. Add the memory use in the diff, and make sure that each one is easy to scan.
5. Split the memory use in the change, and make sure that each one is safe.
6. Group each place where the module touches memory use. It shows the reader that you thought about the details.
7. When the test changes memory use, group the result then.
8. If the diff has more than one rule for memory use, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| memory use is easy to scan | Yes, in each place | Only in some places |
| memory use is useful | Yes, in each place | Only in some places |
| memory use is easy to scan | Yes, in each place | Only in some places |
| memory use is short | Yes, in each place | Only in some places |

Example:

```text
Before: the test has memory use that is not consistent.
After:  the function has memory use that is safe.
```

## Configuration

List each place where the test touches configuration. This is the part that people ask about most often. Split each place where the interface touches configuration. This is the part that people ask about most often. Mark each place where the change touches configuration. It makes the next step much faster.

Steps:

1. Check the configuration in the function, and make sure that each one is specific.
2. If the test has more than one rule for configuration, pick one rule and use it everywhere.
3. Confirm configuration at the end, then write one line about what you found.
4. Find the configuration in the diff, and make sure that each one is complete.
5. Keep configuration easy to scan. A short check now prevents a long fix later.
6. When the module changes configuration, move the result next.
7. If the change has more than one rule for configuration, pick one rule and use it everywhere.
8. Mark configuration before you finish, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| configuration is easy to change | Yes, in each place | Only in some places |
| configuration is easy to test | Yes, in each place | Only in some places |
| configuration is easy to test | Yes, in each place | Only in some places |
| configuration is short | Yes, in each place | Only in some places |

Example:

```text
Before: the change has configuration that is not useful.
After:  the function has configuration that is easy to change.
```

## Retries

Sort retries then, then write one line about what you found. Keep retries correct. This is the part that people ask about most often. When the interface changes retries, rewrite the result before you finish.

Steps:

1. Keep each place where the module touches retries. It makes the next step much faster.
2. When the test changes retries, shorten the result before you finish.
3. Keep retries easy to scan. Most mistakes of this kind are easy to fix early.
4. Join retries then, then write one line about what you found.
5. Join the retries in the module, and make sure that each one is complete.
6. Shorten retries after that, then write one line about what you found.
7. Group each place where the interface touches retries. Most mistakes of this kind are easy to fix early.
8. Keep retries easy to change. It keeps the result the same each time.

| Check | Good | Needs work |
|---|---|---|
| retries is easy to scan | Yes, in each place | Only in some places |
| retries is easy to change | Yes, in each place | Only in some places |
| retries is easy to change | Yes, in each place | Only in some places |
| retries is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the module has retries that is not easy to test.
After:  the diff has retries that is complete.
```

## Dates and time zones

Keep dates and time zones safe. Without it, two people get two different answers. Keep each place where the module touches dates and time zones. Without it, two people get two different answers. Join dates and time zones at the end, then write one line about what you found.

Steps:

1. Keep dates and time zones easy to change. A short check now prevents a long fix later.
2. Mark each place where the interface touches dates and time zones. Small problems here often become large problems later.
3. Keep dates and time zones clear. This is the part that people ask about most often.
4. If the module has more than one rule for dates and time zones, pick one rule and use it everywhere.
5. Read dates and time zones first, then write one line about what you found.
6. When the change changes dates and time zones, find the result before you finish.
7. If the module has more than one rule for dates and time zones, pick one rule and use it everywhere.
8. Add each place where the function touches dates and time zones. Small problems here often become large problems later.

| Check | Good | Needs work |
|---|---|---|
| dates and time zones is easy to scan | Yes, in each place | Only in some places |
| dates and time zones is easy to change | Yes, in each place | Only in some places |
| dates and time zones is useful | Yes, in each place | Only in some places |
| dates and time zones is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has dates and time zones that is not useful.
After:  the module has dates and time zones that is consistent.
```

## Naming

When the test changes naming, mark the result first. When the change changes naming, mark the result after that. When the diff changes naming, rewrite the result next.

Steps:

1. When the diff changes naming, compare the result after that.
2. Check the naming in the test, and make sure that each one is safe.
3. Keep naming correct. Most mistakes of this kind are easy to fix early.
4. When the change changes naming, list the result then.
5. Confirm each place where the test touches naming. It shows the reader that you thought about the details.
6. If the diff has more than one rule for naming, pick one rule and use it everywhere.
7. If the diff has more than one rule for naming, pick one rule and use it everywhere.
8. Keep naming short. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| naming is easy to test | Yes, in each place | Only in some places |
| naming is short | Yes, in each place | Only in some places |
| naming is short | Yes, in each place | Only in some places |
| naming is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the change has naming that is not safe.
After:  the diff has naming that is specific.
```

## Test coverage

Note each place where the function touches test coverage. Without it, two people get two different answers. Keep test coverage easy to scan. It shows the reader that you thought about the details. When the test changes test coverage, list the result then.

Steps:

1. Keep test coverage easy to test. A short check now prevents a long fix later.
2. If the test has more than one rule for test coverage, pick one rule and use it everywhere.
3. Split the test coverage in the interface, and make sure that each one is consistent.
4. Remove each place where the change touches test coverage. Without it, two people get two different answers.
5. Keep test coverage safe. It keeps the result the same each time.
6. Compare test coverage first, then write one line about what you found.
7. If the module has more than one rule for test coverage, pick one rule and use it everywhere.
8. If the change has more than one rule for test coverage, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| test coverage is safe | Yes, in each place | Only in some places |
| test coverage is consistent | Yes, in each place | Only in some places |
| test coverage is simple | Yes, in each place | Only in some places |
| test coverage is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the change has test coverage that is not safe.
After:  the interface has test coverage that is consistent.
```

## Migrations

Sort the migrations in the diff, and make sure that each one is easy to scan. Sort each place where the change touches migrations. This saves time for the next person who reads it. If the change has more than one rule for migrations, pick one rule and use it everywhere.

Steps:

1. Check each place where the interface touches migrations. It makes the next step much faster.
2. Keep migrations complete. This saves time for the next person who reads it.
3. Keep migrations complete. Most mistakes of this kind are easy to fix early.
4. Keep migrations next, then write one line about what you found.
5. When the test changes migrations, list the result next.
6. Keep migrations easy to test. It makes the next step much faster.
7. When the test changes migrations, shorten the result after that.
8. When the function changes migrations, confirm the result before you finish.

| Check | Good | Needs work |
|---|---|---|
| migrations is clear | Yes, in each place | Only in some places |
| migrations is complete | Yes, in each place | Only in some places |
| migrations is correct | Yes, in each place | Only in some places |
| migrations is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the function has migrations that is not simple.
After:  the interface has migrations that is clear.
```

## Recursion

Keep recursion correct. Most mistakes of this kind are easy to fix early. When the interface changes recursion, rewrite the result first. Find the recursion in the module, and make sure that each one is specific.

Steps:

1. When the interface changes recursion, compare the result then.
2. Keep recursion complete. A reader stops when this part is unclear.
3. If the change has more than one rule for recursion, pick one rule and use it everywhere.
4. If the change has more than one rule for recursion, pick one rule and use it everywhere.
5. Read each place where the function touches recursion. It shows the reader that you thought about the details.
6. Check each place where the test touches recursion. Most mistakes of this kind are easy to fix early.
7. Keep recursion correct. Small problems here often become large problems later.
8. Keep recursion complete. It keeps the result the same each time.

| Check | Good | Needs work |
|---|---|---|
| recursion is clear | Yes, in each place | Only in some places |
| recursion is correct | Yes, in each place | Only in some places |
| recursion is useful | Yes, in each place | Only in some places |
| recursion is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the module has recursion that is not easy to test.
After:  the diff has recursion that is safe.
```

## Events

If the interface has more than one rule for events, pick one rule and use it everywhere. Split each place where the interface touches events. It makes the next step much faster. Note the events in the test, and make sure that each one is correct.

Steps:

1. Keep events consistent. Small problems here often become large problems later.
2. When the function changes events, move the result after that.
3. Read events after that, then write one line about what you found.
4. Mark the events in the module, and make sure that each one is correct.
5. Mark the events in the test, and make sure that each one is simple.
6. When the interface changes events, split the result at the end.
7. Keep the events in the interface, and make sure that each one is useful.
8. If the test has more than one rule for events, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| events is useful | Yes, in each place | Only in some places |
| events is easy to test | Yes, in each place | Only in some places |
| events is correct | Yes, in each place | Only in some places |
| events is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the test has events that is not short.
After:  the change has events that is safe.
```

## Logging

If the module has more than one rule for logging, pick one rule and use it everywhere. Find each place where the interface touches logging. A short check now prevents a long fix later. Keep logging simple. It makes the next step much faster.

Steps:

1. Sort each place where the interface touches logging. Small problems here often become large problems later.
2. Count each place where the interface touches logging. This is the part that people ask about most often.
3. Compare the logging in the diff, and make sure that each one is complete.
4. Add each place where the diff touches logging. A short check now prevents a long fix later.
5. Sort each place where the diff touches logging. A reader stops when this part is unclear.
6. Move the logging in the change, and make sure that each one is correct.
7. Rewrite each place where the module touches logging. It keeps the result the same each time.
8. Name logging before you finish, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| logging is clear | Yes, in each place | Only in some places |
| logging is easy to test | Yes, in each place | Only in some places |
| logging is safe | Yes, in each place | Only in some places |
| logging is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the module has logging that is not specific.
After:  the module has logging that is safe.
```

## Concurrency

Keep concurrency clear. Most mistakes of this kind are easy to fix early. Shorten the concurrency in the module, and make sure that each one is correct. Split concurrency then, then write one line about what you found.

Steps:

1. Count concurrency then, then write one line about what you found.
2. If the function has more than one rule for concurrency, pick one rule and use it everywhere.
3. Keep concurrency short. A short check now prevents a long fix later.
4. If the function has more than one rule for concurrency, pick one rule and use it everywhere.
5. Keep concurrency easy to scan. Small problems here often become large problems later.
6. Add each place where the module touches concurrency. Most mistakes of this kind are easy to fix early.
7. Compare each place where the module touches concurrency. This saves time for the next person who reads it.
8. Add the concurrency in the function, and make sure that each one is consistent.

| Check | Good | Needs work |
|---|---|---|
| concurrency is easy to scan | Yes, in each place | Only in some places |
| concurrency is safe | Yes, in each place | Only in some places |
| concurrency is useful | Yes, in each place | Only in some places |
| concurrency is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the function has concurrency that is not complete.
After:  the module has concurrency that is complete.
```
