# Api contracts

## Dependency updates

If the diff has more than one rule for dependency updates, pick one rule and use it everywhere. When the change changes dependency updates, group the result after that. Keep dependency updates easy to test. This saves time for the next person who reads it.

Steps:

1. Confirm dependency updates then, then write one line about what you found.
2. When the change changes dependency updates, count the result before you finish.
3. List each place where the change touches dependency updates. A reader stops when this part is unclear.
4. Mark each place where the diff touches dependency updates. A short check now prevents a long fix later.
5. Mark each place where the test touches dependency updates. Without it, two people get two different answers.
6. When the diff changes dependency updates, confirm the result before you finish.
7. If the change has more than one rule for dependency updates, pick one rule and use it everywhere.
8. Shorten each place where the function touches dependency updates. Small problems here often become large problems later.

| Check | Good | Needs work |
|---|---|---|
| dependency updates is safe | Yes, in each place | Only in some places |
| dependency updates is easy to scan | Yes, in each place | Only in some places |
| dependency updates is simple | Yes, in each place | Only in some places |
| dependency updates is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has dependency updates that is not specific.
After:  the diff has dependency updates that is clear.
```

## File handling

Read the file handling in the module, and make sure that each one is correct. If the diff has more than one rule for file handling, pick one rule and use it everywhere. Shorten the file handling in the function, and make sure that each one is safe.

Steps:

1. If the module has more than one rule for file handling, pick one rule and use it everywhere.
2. Count each place where the interface touches file handling. A reader stops when this part is unclear.
3. When the test changes file handling, group the result first.
4. When the change changes file handling, list the result after that.
5. When the change changes file handling, add the result next.
6. Keep file handling correct. Most mistakes of this kind are easy to fix early.
7. Check each place where the diff touches file handling. Most mistakes of this kind are easy to fix early.
8. Add file handling at the end, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| file handling is correct | Yes, in each place | Only in some places |
| file handling is clear | Yes, in each place | Only in some places |
| file handling is simple | Yes, in each place | Only in some places |
| file handling is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the module has file handling that is not safe.
After:  the interface has file handling that is consistent.
```

## Timeouts

Sort timeouts before you finish, then write one line about what you found. If the interface has more than one rule for timeouts, pick one rule and use it everywhere. Keep timeouts safe. This is the part that people ask about most often.

Steps:

1. Rewrite each place where the test touches timeouts. Small problems here often become large problems later.
2. Keep timeouts safe. Without it, two people get two different answers.
3. Read the timeouts in the function, and make sure that each one is consistent.
4. If the test has more than one rule for timeouts, pick one rule and use it everywhere.
5. Confirm the timeouts in the interface, and make sure that each one is easy to test.
6. Keep timeouts useful. Without it, two people get two different answers.
7. When the change changes timeouts, split the result then.
8. If the change has more than one rule for timeouts, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| timeouts is complete | Yes, in each place | Only in some places |
| timeouts is complete | Yes, in each place | Only in some places |
| timeouts is easy to scan | Yes, in each place | Only in some places |
| timeouts is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has timeouts that is not safe.
After:  the function has timeouts that is clear.
```

## Null checks

Rewrite null checks next, then write one line about what you found. Mark null checks next, then write one line about what you found. When the change changes null checks, sort the result then.

Steps:

1. Read the null checks in the diff, and make sure that each one is consistent.
2. Keep null checks easy to change. This saves time for the next person who reads it.
3. When the function changes null checks, split the result first.
4. Confirm each place where the change touches null checks. A reader stops when this part is unclear.
5. Keep null checks simple. It makes the next step much faster.
6. Read each place where the module touches null checks. A reader stops when this part is unclear.
7. When the module changes null checks, find the result next.
8. Read the null checks in the diff, and make sure that each one is consistent.

| Check | Good | Needs work |
|---|---|---|
| null checks is useful | Yes, in each place | Only in some places |
| null checks is short | Yes, in each place | Only in some places |
| null checks is easy to change | Yes, in each place | Only in some places |
| null checks is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the function has null checks that is not useful.
After:  the interface has null checks that is useful.
```

## Pagination

When the module changes pagination, count the result first. When the test changes pagination, rewrite the result before you finish. Join the pagination in the interface, and make sure that each one is safe.

Steps:

1. Join each place where the diff touches pagination. Without it, two people get two different answers.
2. Check the pagination in the test, and make sure that each one is easy to scan.
3. Join pagination before you finish, then write one line about what you found.
4. Keep pagination consistent. It keeps the result the same each time.
5. Keep pagination specific. This is the part that people ask about most often.
6. If the change has more than one rule for pagination, pick one rule and use it everywhere.
7. Add the pagination in the interface, and make sure that each one is correct.
8. Confirm pagination before you finish, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| pagination is consistent | Yes, in each place | Only in some places |
| pagination is easy to scan | Yes, in each place | Only in some places |
| pagination is specific | Yes, in each place | Only in some places |
| pagination is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the change has pagination that is not correct.
After:  the module has pagination that is useful.
```

## Naming

Confirm each place where the function touches naming. It keeps the result the same each time. Keep naming useful. A reader stops when this part is unclear. Compare naming at the end, then write one line about what you found.

Steps:

1. Mark the naming in the interface, and make sure that each one is correct.
2. Keep naming next, then write one line about what you found.
3. If the interface has more than one rule for naming, pick one rule and use it everywhere.
4. If the change has more than one rule for naming, pick one rule and use it everywhere.
5. Remove each place where the diff touches naming. It shows the reader that you thought about the details.
6. Split each place where the module touches naming. A reader stops when this part is unclear.
7. Rewrite each place where the diff touches naming. Most mistakes of this kind are easy to fix early.
8. Check the naming in the function, and make sure that each one is safe.

| Check | Good | Needs work |
|---|---|---|
| naming is easy to test | Yes, in each place | Only in some places |
| naming is useful | Yes, in each place | Only in some places |
| naming is easy to test | Yes, in each place | Only in some places |
| naming is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the change has naming that is not specific.
After:  the function has naming that is safe.
```

## Logging

Mark the logging in the change, and make sure that each one is easy to test. Keep logging short. Small problems here often become large problems later. If the test has more than one rule for logging, pick one rule and use it everywhere.

Steps:

1. Sort each place where the function touches logging. It shows the reader that you thought about the details.
2. Keep logging short. Without it, two people get two different answers.
3. Remove the logging in the change, and make sure that each one is complete.
4. Sort the logging in the change, and make sure that each one is complete.
5. Keep logging short. Without it, two people get two different answers.
6. Keep logging clear. Small problems here often become large problems later.
7. Confirm each place where the change touches logging. Most mistakes of this kind are easy to fix early.
8. Sort each place where the test touches logging. A reader stops when this part is unclear.

| Check | Good | Needs work |
|---|---|---|
| logging is complete | Yes, in each place | Only in some places |
| logging is safe | Yes, in each place | Only in some places |
| logging is easy to change | Yes, in each place | Only in some places |
| logging is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the interface has logging that is not easy to test.
After:  the interface has logging that is consistent.
```

## Migrations

Sort each place where the module touches migrations. It shows the reader that you thought about the details. Count each place where the module touches migrations. A short check now prevents a long fix later. Find each place where the diff touches migrations. A reader stops when this part is unclear.

Steps:

1. Keep migrations consistent. It keeps the result the same each time.
2. Keep each place where the module touches migrations. This is the part that people ask about most often.
3. Note the migrations in the change, and make sure that each one is easy to change.
4. When the module changes migrations, split the result then.
5. Sort migrations before you finish, then write one line about what you found.
6. Add migrations after that, then write one line about what you found.
7. Keep migrations easy to scan. It keeps the result the same each time.
8. Name each place where the diff touches migrations. Without it, two people get two different answers.

| Check | Good | Needs work |
|---|---|---|
| migrations is short | Yes, in each place | Only in some places |
| migrations is easy to scan | Yes, in each place | Only in some places |
| migrations is complete | Yes, in each place | Only in some places |
| migrations is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the test has migrations that is not short.
After:  the change has migrations that is complete.
```

## Test coverage

Note test coverage at the end, then write one line about what you found. If the change has more than one rule for test coverage, pick one rule and use it everywhere. Keep test coverage simple. A reader stops when this part is unclear.

Steps:

1. Join test coverage first, then write one line about what you found.
2. Keep test coverage easy to change. It shows the reader that you thought about the details.
3. When the function changes test coverage, join the result next.
4. Keep test coverage safe. It shows the reader that you thought about the details.
5. Mark the test coverage in the function, and make sure that each one is clear.
6. Sort the test coverage in the function, and make sure that each one is complete.
7. Keep test coverage useful. Without it, two people get two different answers.
8. List each place where the change touches test coverage. Without it, two people get two different answers.

| Check | Good | Needs work |
|---|---|---|
| test coverage is correct | Yes, in each place | Only in some places |
| test coverage is easy to scan | Yes, in each place | Only in some places |
| test coverage is correct | Yes, in each place | Only in some places |
| test coverage is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the function has test coverage that is not easy to scan.
After:  the diff has test coverage that is easy to change.
```

## Type safety

If the module has more than one rule for type safety, pick one rule and use it everywhere. When the change changes type safety, shorten the result then. Keep type safety consistent. This is the part that people ask about most often.

Steps:

1. When the function changes type safety, move the result then.
2. Mark each place where the diff touches type safety. Most mistakes of this kind are easy to fix early.
3. When the change changes type safety, keep the result first.
4. Keep type safety next, then write one line about what you found.
5. Keep type safety easy to scan. Without it, two people get two different answers.
6. Confirm the type safety in the test, and make sure that each one is clear.
7. Rewrite type safety before you finish, then write one line about what you found.
8. Keep type safety complete. It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| type safety is easy to change | Yes, in each place | Only in some places |
| type safety is specific | Yes, in each place | Only in some places |
| type safety is consistent | Yes, in each place | Only in some places |
| type safety is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the interface has type safety that is not complete.
After:  the interface has type safety that is easy to test.
```

## Database queries

If the diff has more than one rule for database queries, pick one rule and use it everywhere. When the change changes database queries, compare the result before you finish. Keep database queries consistent. Most mistakes of this kind are easy to fix early.

Steps:

1. Keep database queries correct. Most mistakes of this kind are easy to fix early.
2. Add the database queries in the function, and make sure that each one is consistent.
3. Add database queries after that, then write one line about what you found.
4. Sort each place where the function touches database queries. Small problems here often become large problems later.
5. Name each place where the change touches database queries. Small problems here often become large problems later.
6. Mark each place where the module touches database queries. Most mistakes of this kind are easy to fix early.
7. Read database queries before you finish, then write one line about what you found.
8. Note the database queries in the test, and make sure that each one is easy to change.

| Check | Good | Needs work |
|---|---|---|
| database queries is simple | Yes, in each place | Only in some places |
| database queries is easy to scan | Yes, in each place | Only in some places |
| database queries is simple | Yes, in each place | Only in some places |
| database queries is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has database queries that is not easy to change.
After:  the change has database queries that is correct.
```

## Public interfaces

Confirm the public interfaces in the interface, and make sure that each one is useful. Find public interfaces at the end, then write one line about what you found. When the module changes public interfaces, move the result first.

Steps:

1. Group public interfaces at the end, then write one line about what you found.
2. If the function has more than one rule for public interfaces, pick one rule and use it everywhere.
3. Split the public interfaces in the function, and make sure that each one is simple.
4. Shorten each place where the interface touches public interfaces. This is the part that people ask about most often.
5. When the change changes public interfaces, find the result at the end.
6. Confirm each place where the module touches public interfaces. A short check now prevents a long fix later.
7. Keep public interfaces easy to scan. Small problems here often become large problems later.
8. Mark public interfaces next, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| public interfaces is consistent | Yes, in each place | Only in some places |
| public interfaces is easy to test | Yes, in each place | Only in some places |
| public interfaces is clear | Yes, in each place | Only in some places |
| public interfaces is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the test has public interfaces that is not simple.
After:  the change has public interfaces that is easy to scan.
```

## Recursion

If the interface has more than one rule for recursion, pick one rule and use it everywhere. Confirm recursion before you finish, then write one line about what you found. Sort recursion first, then write one line about what you found.

Steps:

1. Move each place where the change touches recursion. It shows the reader that you thought about the details.
2. If the function has more than one rule for recursion, pick one rule and use it everywhere.
3. When the test changes recursion, join the result first.
4. Rewrite the recursion in the function, and make sure that each one is simple.
5. Keep recursion safe. Without it, two people get two different answers.
6. If the interface has more than one rule for recursion, pick one rule and use it everywhere.
7. Join each place where the diff touches recursion. Small problems here often become large problems later.
8. Keep recursion short. Without it, two people get two different answers.

| Check | Good | Needs work |
|---|---|---|
| recursion is short | Yes, in each place | Only in some places |
| recursion is short | Yes, in each place | Only in some places |
| recursion is easy to scan | Yes, in each place | Only in some places |
| recursion is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the module has recursion that is not correct.
After:  the diff has recursion that is useful.
```

## Mocks

Mark mocks at the end, then write one line about what you found. When the module changes mocks, count the result before you finish. If the diff has more than one rule for mocks, pick one rule and use it everywhere.

Steps:

1. If the diff has more than one rule for mocks, pick one rule and use it everywhere.
2. When the diff changes mocks, check the result at the end.
3. Group mocks first, then write one line about what you found.
4. Rewrite the mocks in the module, and make sure that each one is useful.
5. Keep mocks clear. This saves time for the next person who reads it.
6. Sort each place where the test touches mocks. Without it, two people get two different answers.
7. Name the mocks in the diff, and make sure that each one is specific.
8. Sort the mocks in the module, and make sure that each one is safe.

| Check | Good | Needs work |
|---|---|---|
| mocks is useful | Yes, in each place | Only in some places |
| mocks is easy to scan | Yes, in each place | Only in some places |
| mocks is specific | Yes, in each place | Only in some places |
| mocks is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the change has mocks that is not correct.
After:  the module has mocks that is useful.
```

## Startup time

Note the startup time in the test, and make sure that each one is specific. Find each place where the change touches startup time. It shows the reader that you thought about the details. Remove the startup time in the interface, and make sure that each one is useful.

Steps:

1. Add startup time next, then write one line about what you found.
2. Keep the startup time in the test, and make sure that each one is specific.
3. When the module changes startup time, keep the result at the end.
4. If the diff has more than one rule for startup time, pick one rule and use it everywhere.
5. List the startup time in the interface, and make sure that each one is easy to test.
6. Keep startup time specific. It keeps the result the same each time.
7. Keep startup time safe. A short check now prevents a long fix later.
8. Confirm startup time next, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| startup time is safe | Yes, in each place | Only in some places |
| startup time is clear | Yes, in each place | Only in some places |
| startup time is easy to change | Yes, in each place | Only in some places |
| startup time is short | Yes, in each place | Only in some places |

Example:

```text
Before: the interface has startup time that is not safe.
After:  the test has startup time that is easy to scan.
```

## Money values

Keep money values complete. A short check now prevents a long fix later. Check money values before you finish, then write one line about what you found. List the money values in the diff, and make sure that each one is specific.

Steps:

1. Add each place where the interface touches money values. It keeps the result the same each time.
2. Keep each place where the test touches money values. A reader stops when this part is unclear.
3. Keep the money values in the diff, and make sure that each one is easy to test.
4. Keep money values useful. This is the part that people ask about most often.
5. Find the money values in the change, and make sure that each one is specific.
6. Note money values first, then write one line about what you found.
7. Join each place where the interface touches money values. This saves time for the next person who reads it.
8. Check each place where the change touches money values. Small problems here often become large problems later.

| Check | Good | Needs work |
|---|---|---|
| money values is consistent | Yes, in each place | Only in some places |
| money values is clear | Yes, in each place | Only in some places |
| money values is easy to test | Yes, in each place | Only in some places |
| money values is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the test has money values that is not safe.
After:  the module has money values that is clear.
```

## Queues

If the module has more than one rule for queues, pick one rule and use it everywhere. If the diff has more than one rule for queues, pick one rule and use it everywhere. Keep queues safe. It keeps the result the same each time.

Steps:

1. Keep queues complete. Small problems here often become large problems later.
2. Keep queues next, then write one line about what you found.
3. If the test has more than one rule for queues, pick one rule and use it everywhere.
4. When the change changes queues, split the result first.
5. When the change changes queues, note the result at the end.
6. Count queues before you finish, then write one line about what you found.
7. Sort the queues in the test, and make sure that each one is simple.
8. Keep queues correct. It keeps the result the same each time.

| Check | Good | Needs work |
|---|---|---|
| queues is easy to test | Yes, in each place | Only in some places |
| queues is complete | Yes, in each place | Only in some places |
| queues is easy to test | Yes, in each place | Only in some places |
| queues is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the test has queues that is not specific.
After:  the function has queues that is complete.
```

## Dates and time zones

When the interface changes dates and time zones, rewrite the result next. Mark dates and time zones next, then write one line about what you found. If the test has more than one rule for dates and time zones, pick one rule and use it everywhere.

Steps:

1. Count dates and time zones at the end, then write one line about what you found.
2. Add each place where the module touches dates and time zones. It keeps the result the same each time.
3. Shorten the dates and time zones in the interface, and make sure that each one is safe.
4. If the test has more than one rule for dates and time zones, pick one rule and use it everywhere.
5. Shorten dates and time zones at the end, then write one line about what you found.
6. If the test has more than one rule for dates and time zones, pick one rule and use it everywhere.
7. Keep dates and time zones useful. This saves time for the next person who reads it.
8. Keep dates and time zones safe. It keeps the result the same each time.

| Check | Good | Needs work |
|---|---|---|
| dates and time zones is safe | Yes, in each place | Only in some places |
| dates and time zones is clear | Yes, in each place | Only in some places |
| dates and time zones is specific | Yes, in each place | Only in some places |
| dates and time zones is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the interface has dates and time zones that is not short.
After:  the function has dates and time zones that is consistent.
```

## Caching

When the diff changes caching, remove the result before you finish. If the change has more than one rule for caching, pick one rule and use it everywhere. When the diff changes caching, join the result next.

Steps:

1. If the function has more than one rule for caching, pick one rule and use it everywhere.
2. Keep caching specific. This saves time for the next person who reads it.
3. Add each place where the test touches caching. Small problems here often become large problems later.
4. Keep caching safe. Small problems here often become large problems later.
5. Find the caching in the test, and make sure that each one is specific.
6. If the change has more than one rule for caching, pick one rule and use it everywhere.
7. Count caching at the end, then write one line about what you found.
8. Split the caching in the test, and make sure that each one is consistent.

| Check | Good | Needs work |
|---|---|---|
| caching is easy to change | Yes, in each place | Only in some places |
| caching is easy to test | Yes, in each place | Only in some places |
| caching is easy to scan | Yes, in each place | Only in some places |
| caching is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the change has caching that is not useful.
After:  the test has caching that is complete.
```

## Memory use

Rewrite the memory use in the function, and make sure that each one is specific. If the test has more than one rule for memory use, pick one rule and use it everywhere. Read the memory use in the interface, and make sure that each one is short.

Steps:

1. Keep memory use easy to change. It shows the reader that you thought about the details.
2. Sort the memory use in the test, and make sure that each one is consistent.
3. Join each place where the diff touches memory use. A short check now prevents a long fix later.
4. When the change changes memory use, keep the result next.
5. Rewrite memory use first, then write one line about what you found.
6. Shorten the memory use in the test, and make sure that each one is easy to test.
7. When the module changes memory use, keep the result next.
8. Keep memory use easy to scan. Most mistakes of this kind are easy to fix early.

| Check | Good | Needs work |
|---|---|---|
| memory use is easy to test | Yes, in each place | Only in some places |
| memory use is consistent | Yes, in each place | Only in some places |
| memory use is easy to change | Yes, in each place | Only in some places |
| memory use is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the interface has memory use that is not easy to change.
After:  the test has memory use that is simple.
```

## Configuration

Count the configuration in the interface, and make sure that each one is complete. If the test has more than one rule for configuration, pick one rule and use it everywhere. Count configuration before you finish, then write one line about what you found.

Steps:

1. If the change has more than one rule for configuration, pick one rule and use it everywhere.
2. Keep each place where the interface touches configuration. Small problems here often become large problems later.
3. Remove the configuration in the test, and make sure that each one is simple.
4. Keep each place where the module touches configuration. It makes the next step much faster.
5. Read each place where the function touches configuration. It keeps the result the same each time.
6. Confirm configuration next, then write one line about what you found.
7. Mark the configuration in the test, and make sure that each one is safe.
8. Move configuration after that, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| configuration is short | Yes, in each place | Only in some places |
| configuration is simple | Yes, in each place | Only in some places |
| configuration is clear | Yes, in each place | Only in some places |
| configuration is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the module has configuration that is not consistent.
After:  the diff has configuration that is consistent.
```

## Loops

Keep each place where the test touches loops. This is the part that people ask about most often. If the function has more than one rule for loops, pick one rule and use it everywhere. List the loops in the change, and make sure that each one is complete.

Steps:

1. If the test has more than one rule for loops, pick one rule and use it everywhere.
2. Confirm the loops in the change, and make sure that each one is consistent.
3. When the change changes loops, split the result next.
4. Name each place where the diff touches loops. A reader stops when this part is unclear.
5. Keep loops easy to change. Without it, two people get two different answers.
6. If the diff has more than one rule for loops, pick one rule and use it everywhere.
7. Compare loops after that, then write one line about what you found.
8. If the function has more than one rule for loops, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| loops is complete | Yes, in each place | Only in some places |
| loops is useful | Yes, in each place | Only in some places |
| loops is clear | Yes, in each place | Only in some places |
| loops is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the function has loops that is not clear.
After:  the diff has loops that is complete.
```

## API contracts

If the module has more than one rule for API contracts, pick one rule and use it everywhere. If the interface has more than one rule for API contracts, pick one rule and use it everywhere. Read each place where the function touches API contracts. Without it, two people get two different answers.

Steps:

1. Name each place where the function touches API contracts. Without it, two people get two different answers.
2. Check API contracts after that, then write one line about what you found.
3. When the change changes API contracts, read the result at the end.
4. Compare each place where the module touches API contracts. It keeps the result the same each time.
5. Mark the API contracts in the diff, and make sure that each one is useful.
6. Name the API contracts in the interface, and make sure that each one is specific.
7. When the module changes API contracts, mark the result after that.
8. When the diff changes API contracts, confirm the result first.

| Check | Good | Needs work |
|---|---|---|
| API contracts is safe | Yes, in each place | Only in some places |
| API contracts is complete | Yes, in each place | Only in some places |
| API contracts is easy to test | Yes, in each place | Only in some places |
| API contracts is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has API contracts that is not easy to change.
After:  the module has API contracts that is short.
```

## Error handling

If the function has more than one rule for error handling, pick one rule and use it everywhere. Split error handling at the end, then write one line about what you found. Join the error handling in the function, and make sure that each one is easy to test.

Steps:

1. Keep error handling simple. A reader stops when this part is unclear.
2. Join error handling before you finish, then write one line about what you found.
3. Keep the error handling in the interface, and make sure that each one is simple.
4. Keep error handling easy to scan. It makes the next step much faster.
5. When the change changes error handling, find the result next.
6. If the diff has more than one rule for error handling, pick one rule and use it everywhere.
7. Keep error handling easy to test. It makes the next step much faster.
8. When the function changes error handling, count the result at the end.

| Check | Good | Needs work |
|---|---|---|
| error handling is consistent | Yes, in each place | Only in some places |
| error handling is clear | Yes, in each place | Only in some places |
| error handling is complete | Yes, in each place | Only in some places |
| error handling is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the function has error handling that is not clear.
After:  the test has error handling that is correct.
```
