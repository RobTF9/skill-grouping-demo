# Concurrency

## Comments

When the change changes comments, shorten the result after that. List each place where the test touches comments. A short check now prevents a long fix later. Keep comments then, then write one line about what you found.

Steps:

1. Keep comments safe. Small problems here often become large problems later.
2. When the test changes comments, compare the result then.
3. Move the comments in the module, and make sure that each one is consistent.
4. If the interface has more than one rule for comments, pick one rule and use it everywhere.
5. Keep comments clear. Without it, two people get two different answers.
6. Sort comments at the end, then write one line about what you found.
7. If the function has more than one rule for comments, pick one rule and use it everywhere.
8. When the function changes comments, sort the result next.

| Check | Good | Needs work |
|---|---|---|
| comments is useful | Yes, in each place | Only in some places |
| comments is short | Yes, in each place | Only in some places |
| comments is easy to scan | Yes, in each place | Only in some places |
| comments is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the test has comments that is not useful.
After:  the function has comments that is correct.
```

## Configuration

Sort each place where the function touches configuration. This saves time for the next person who reads it. Remove configuration after that, then write one line about what you found. Count each place where the change touches configuration. Most mistakes of this kind are easy to fix early.

Steps:

1. When the function changes configuration, name the result next.
2. Shorten configuration at the end, then write one line about what you found.
3. Name configuration at the end, then write one line about what you found.
4. Keep configuration easy to scan. A reader stops when this part is unclear.
5. Keep configuration easy to test. It keeps the result the same each time.
6. Move the configuration in the function, and make sure that each one is safe.
7. If the module has more than one rule for configuration, pick one rule and use it everywhere.
8. Keep the configuration in the function, and make sure that each one is safe.

| Check | Good | Needs work |
|---|---|---|
| configuration is easy to scan | Yes, in each place | Only in some places |
| configuration is complete | Yes, in each place | Only in some places |
| configuration is easy to test | Yes, in each place | Only in some places |
| configuration is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the module has configuration that is not useful.
After:  the diff has configuration that is easy to change.
```

## Test coverage

Shorten test coverage then, then write one line about what you found. If the module has more than one rule for test coverage, pick one rule and use it everywhere. Compare each place where the change touches test coverage. This is the part that people ask about most often.

Steps:

1. When the module changes test coverage, sort the result before you finish.
2. Mark the test coverage in the function, and make sure that each one is simple.
3. Keep test coverage consistent. A reader stops when this part is unclear.
4. If the test has more than one rule for test coverage, pick one rule and use it everywhere.
5. If the test has more than one rule for test coverage, pick one rule and use it everywhere.
6. If the change has more than one rule for test coverage, pick one rule and use it everywhere.
7. When the change changes test coverage, rewrite the result next.
8. Group each place where the change touches test coverage. It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| test coverage is complete | Yes, in each place | Only in some places |
| test coverage is consistent | Yes, in each place | Only in some places |
| test coverage is easy to test | Yes, in each place | Only in some places |
| test coverage is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the test has test coverage that is not consistent.
After:  the change has test coverage that is easy to scan.
```

## Money values

When the test changes money values, count the result then. If the module has more than one rule for money values, pick one rule and use it everywhere. Keep the money values in the test, and make sure that each one is complete.

Steps:

1. Keep money values useful. Without it, two people get two different answers.
2. Sort the money values in the function, and make sure that each one is easy to change.
3. Read each place where the change touches money values. This is the part that people ask about most often.
4. Shorten money values then, then write one line about what you found.
5. Remove each place where the change touches money values. A short check now prevents a long fix later.
6. When the change changes money values, sort the result first.
7. If the change has more than one rule for money values, pick one rule and use it everywhere.
8. Check money values after that, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| money values is specific | Yes, in each place | Only in some places |
| money values is specific | Yes, in each place | Only in some places |
| money values is useful | Yes, in each place | Only in some places |
| money values is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the function has money values that is not correct.
After:  the change has money values that is correct.
```

## Timeouts

Note each place where the diff touches timeouts. This saves time for the next person who reads it. If the function has more than one rule for timeouts, pick one rule and use it everywhere. When the module changes timeouts, mark the result before you finish.

Steps:

1. Note the timeouts in the change, and make sure that each one is easy to scan.
2. Remove each place where the module touches timeouts. Most mistakes of this kind are easy to fix early.
3. When the change changes timeouts, check the result then.
4. Join each place where the change touches timeouts. It makes the next step much faster.
5. If the module has more than one rule for timeouts, pick one rule and use it everywhere.
6. Keep timeouts simple. It keeps the result the same each time.
7. Keep timeouts easy to scan. Most mistakes of this kind are easy to fix early.
8. Add each place where the interface touches timeouts. Without it, two people get two different answers.

| Check | Good | Needs work |
|---|---|---|
| timeouts is correct | Yes, in each place | Only in some places |
| timeouts is specific | Yes, in each place | Only in some places |
| timeouts is short | Yes, in each place | Only in some places |
| timeouts is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the function has timeouts that is not easy to change.
After:  the interface has timeouts that is easy to change.
```

## Feature flags

List feature flags after that, then write one line about what you found. Split the feature flags in the interface, and make sure that each one is safe. When the interface changes feature flags, check the result after that.

Steps:

1. If the function has more than one rule for feature flags, pick one rule and use it everywhere.
2. When the interface changes feature flags, rewrite the result at the end.
3. Keep feature flags correct. Without it, two people get two different answers.
4. Count each place where the module touches feature flags. It shows the reader that you thought about the details.
5. Confirm the feature flags in the change, and make sure that each one is short.
6. Find each place where the change touches feature flags. It keeps the result the same each time.
7. Confirm the feature flags in the module, and make sure that each one is useful.
8. Rewrite feature flags before you finish, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| feature flags is specific | Yes, in each place | Only in some places |
| feature flags is short | Yes, in each place | Only in some places |
| feature flags is correct | Yes, in each place | Only in some places |
| feature flags is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the interface has feature flags that is not consistent.
After:  the interface has feature flags that is safe.
```

## Events

Count the events in the interface, and make sure that each one is easy to scan. If the change has more than one rule for events, pick one rule and use it everywhere. Find each place where the test touches events. It shows the reader that you thought about the details.

Steps:

1. Count each place where the change touches events. This is the part that people ask about most often.
2. If the test has more than one rule for events, pick one rule and use it everywhere.
3. When the module changes events, split the result before you finish.
4. Keep events simple. A short check now prevents a long fix later.
5. Read each place where the diff touches events. Small problems here often become large problems later.
6. If the interface has more than one rule for events, pick one rule and use it everywhere.
7. Sort each place where the module touches events. Most mistakes of this kind are easy to fix early.
8. Find events then, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| events is specific | Yes, in each place | Only in some places |
| events is correct | Yes, in each place | Only in some places |
| events is specific | Yes, in each place | Only in some places |
| events is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the change has events that is not specific.
After:  the test has events that is complete.
```

## Database queries

Mark each place where the test touches database queries. It keeps the result the same each time. Add each place where the change touches database queries. This is the part that people ask about most often. Add database queries after that, then write one line about what you found.

Steps:

1. Sort each place where the test touches database queries. It makes the next step much faster.
2. When the interface changes database queries, rewrite the result next.
3. Keep database queries easy to change. A reader stops when this part is unclear.
4. Mark the database queries in the diff, and make sure that each one is useful.
5. If the interface has more than one rule for database queries, pick one rule and use it everywhere.
6. Count database queries next, then write one line about what you found.
7. Move database queries before you finish, then write one line about what you found.
8. If the interface has more than one rule for database queries, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| database queries is easy to scan | Yes, in each place | Only in some places |
| database queries is simple | Yes, in each place | Only in some places |
| database queries is correct | Yes, in each place | Only in some places |
| database queries is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has database queries that is not safe.
After:  the diff has database queries that is complete.
```

## Recursion

When the test changes recursion, confirm the result next. Add each place where the function touches recursion. This is the part that people ask about most often. When the diff changes recursion, keep the result after that.

Steps:

1. Check the recursion in the interface, and make sure that each one is useful.
2. If the test has more than one rule for recursion, pick one rule and use it everywhere.
3. When the diff changes recursion, keep the result at the end.
4. Keep recursion simple. This is the part that people ask about most often.
5. When the test changes recursion, shorten the result then.
6. If the function has more than one rule for recursion, pick one rule and use it everywhere.
7. If the function has more than one rule for recursion, pick one rule and use it everywhere.
8. Name each place where the diff touches recursion. It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| recursion is simple | Yes, in each place | Only in some places |
| recursion is easy to test | Yes, in each place | Only in some places |
| recursion is safe | Yes, in each place | Only in some places |
| recursion is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the change has recursion that is not useful.
After:  the diff has recursion that is short.
```

## Loops

Remove loops first, then write one line about what you found. When the interface changes loops, join the result next. If the module has more than one rule for loops, pick one rule and use it everywhere.

Steps:

1. Keep loops short. It keeps the result the same each time.
2. Count the loops in the test, and make sure that each one is correct.
3. Confirm the loops in the function, and make sure that each one is short.
4. When the module changes loops, find the result after that.
5. Shorten the loops in the test, and make sure that each one is safe.
6. When the interface changes loops, shorten the result then.
7. If the function has more than one rule for loops, pick one rule and use it everywhere.
8. When the function changes loops, mark the result at the end.

| Check | Good | Needs work |
|---|---|---|
| loops is clear | Yes, in each place | Only in some places |
| loops is specific | Yes, in each place | Only in some places |
| loops is easy to test | Yes, in each place | Only in some places |
| loops is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the test has loops that is not consistent.
After:  the module has loops that is short.
```

## File handling

Keep file handling easy to scan. It makes the next step much faster. Note each place where the test touches file handling. A short check now prevents a long fix later. Note file handling at the end, then write one line about what you found.

Steps:

1. List each place where the test touches file handling. It makes the next step much faster.
2. List each place where the module touches file handling. Most mistakes of this kind are easy to fix early.
3. Keep file handling useful. It shows the reader that you thought about the details.
4. Keep file handling consistent. A reader stops when this part is unclear.
5. If the test has more than one rule for file handling, pick one rule and use it everywhere.
6. If the function has more than one rule for file handling, pick one rule and use it everywhere.
7. If the function has more than one rule for file handling, pick one rule and use it everywhere.
8. When the diff changes file handling, list the result first.

| Check | Good | Needs work |
|---|---|---|
| file handling is safe | Yes, in each place | Only in some places |
| file handling is clear | Yes, in each place | Only in some places |
| file handling is simple | Yes, in each place | Only in some places |
| file handling is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has file handling that is not easy to scan.
After:  the function has file handling that is easy to scan.
```

## Pagination

List pagination then, then write one line about what you found. Keep pagination complete. Small problems here often become large problems later. If the module has more than one rule for pagination, pick one rule and use it everywhere.

Steps:

1. Check pagination before you finish, then write one line about what you found.
2. When the function changes pagination, mark the result before you finish.
3. Keep pagination complete. A reader stops when this part is unclear.
4. When the interface changes pagination, read the result first.
5. Mark pagination next, then write one line about what you found.
6. If the test has more than one rule for pagination, pick one rule and use it everywhere.
7. List the pagination in the interface, and make sure that each one is useful.
8. Rewrite the pagination in the function, and make sure that each one is useful.

| Check | Good | Needs work |
|---|---|---|
| pagination is easy to test | Yes, in each place | Only in some places |
| pagination is easy to scan | Yes, in each place | Only in some places |
| pagination is specific | Yes, in each place | Only in some places |
| pagination is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the test has pagination that is not consistent.
After:  the diff has pagination that is useful.
```

## Memory use

If the function has more than one rule for memory use, pick one rule and use it everywhere. Remove the memory use in the function, and make sure that each one is easy to test. Find memory use next, then write one line about what you found.

Steps:

1. Keep memory use clear. It keeps the result the same each time.
2. When the interface changes memory use, group the result before you finish.
3. Keep memory use safe. A reader stops when this part is unclear.
4. When the function changes memory use, shorten the result first.
5. Mark the memory use in the test, and make sure that each one is correct.
6. When the interface changes memory use, find the result before you finish.
7. Keep memory use easy to scan. Most mistakes of this kind are easy to fix early.
8. When the module changes memory use, note the result then.

| Check | Good | Needs work |
|---|---|---|
| memory use is useful | Yes, in each place | Only in some places |
| memory use is clear | Yes, in each place | Only in some places |
| memory use is easy to test | Yes, in each place | Only in some places |
| memory use is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the module has memory use that is not complete.
After:  the test has memory use that is consistent.
```

## Dead code

Keep dead code easy to scan. A reader stops when this part is unclear. List dead code at the end, then write one line about what you found. Mark dead code then, then write one line about what you found.

Steps:

1. List dead code next, then write one line about what you found.
2. Shorten dead code before you finish, then write one line about what you found.
3. When the module changes dead code, check the result after that.
4. Confirm each place where the interface touches dead code. It keeps the result the same each time.
5. If the diff has more than one rule for dead code, pick one rule and use it everywhere.
6. If the function has more than one rule for dead code, pick one rule and use it everywhere.
7. If the module has more than one rule for dead code, pick one rule and use it everywhere.
8. Keep dead code then, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| dead code is short | Yes, in each place | Only in some places |
| dead code is consistent | Yes, in each place | Only in some places |
| dead code is consistent | Yes, in each place | Only in some places |
| dead code is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the change has dead code that is not specific.
After:  the interface has dead code that is clear.
```

## Type safety

Keep the type safety in the change, and make sure that each one is useful. Rewrite type safety before you finish, then write one line about what you found. Keep type safety clear. It makes the next step much faster.

Steps:

1. Count the type safety in the test, and make sure that each one is consistent.
2. Find the type safety in the diff, and make sure that each one is easy to change.
3. Group each place where the function touches type safety. Most mistakes of this kind are easy to fix early.
4. Add the type safety in the interface, and make sure that each one is complete.
5. If the function has more than one rule for type safety, pick one rule and use it everywhere.
6. Remove the type safety in the change, and make sure that each one is easy to change.
7. Count the type safety in the module, and make sure that each one is complete.
8. When the interface changes type safety, rewrite the result first.

| Check | Good | Needs work |
|---|---|---|
| type safety is short | Yes, in each place | Only in some places |
| type safety is easy to change | Yes, in each place | Only in some places |
| type safety is easy to scan | Yes, in each place | Only in some places |
| type safety is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the test has type safety that is not correct.
After:  the diff has type safety that is useful.
```

## Retries

Split each place where the function touches retries. It shows the reader that you thought about the details. When the test changes retries, mark the result before you finish. Name retries at the end, then write one line about what you found.

Steps:

1. Move the retries in the module, and make sure that each one is short.
2. If the change has more than one rule for retries, pick one rule and use it everywhere.
3. Keep retries specific. This saves time for the next person who reads it.
4. Keep retries easy to scan. It keeps the result the same each time.
5. When the test changes retries, compare the result first.
6. Count each place where the change touches retries. It makes the next step much faster.
7. Keep retries first, then write one line about what you found.
8. When the test changes retries, mark the result next.

| Check | Good | Needs work |
|---|---|---|
| retries is safe | Yes, in each place | Only in some places |
| retries is simple | Yes, in each place | Only in some places |
| retries is easy to change | Yes, in each place | Only in some places |
| retries is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the interface has retries that is not complete.
After:  the diff has retries that is easy to scan.
```

## Logging

Keep logging safe. This is the part that people ask about most often. Keep logging short. Small problems here often become large problems later. When the test changes logging, sort the result first.

Steps:

1. Note each place where the change touches logging. This is the part that people ask about most often.
2. Check logging then, then write one line about what you found.
3. Find each place where the diff touches logging. Most mistakes of this kind are easy to fix early.
4. When the function changes logging, find the result after that.
5. Mark the logging in the function, and make sure that each one is correct.
6. When the diff changes logging, shorten the result then.
7. Confirm logging next, then write one line about what you found.
8. List the logging in the test, and make sure that each one is simple.

| Check | Good | Needs work |
|---|---|---|
| logging is safe | Yes, in each place | Only in some places |
| logging is complete | Yes, in each place | Only in some places |
| logging is safe | Yes, in each place | Only in some places |
| logging is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the module has logging that is not easy to test.
After:  the test has logging that is simple.
```

## Queues

If the change has more than one rule for queues, pick one rule and use it everywhere. If the test has more than one rule for queues, pick one rule and use it everywhere. Remove queues before you finish, then write one line about what you found.

Steps:

1. Keep the queues in the function, and make sure that each one is correct.
2. Find the queues in the diff, and make sure that each one is easy to test.
3. When the diff changes queues, rewrite the result before you finish.
4. If the test has more than one rule for queues, pick one rule and use it everywhere.
5. Compare the queues in the change, and make sure that each one is safe.
6. When the test changes queues, read the result at the end.
7. Keep queues complete. Most mistakes of this kind are easy to fix early.
8. When the interface changes queues, add the result next.

| Check | Good | Needs work |
|---|---|---|
| queues is complete | Yes, in each place | Only in some places |
| queues is consistent | Yes, in each place | Only in some places |
| queues is easy to test | Yes, in each place | Only in some places |
| queues is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the interface has queues that is not complete.
After:  the diff has queues that is simple.
```

## Concurrency

Keep concurrency complete. A short check now prevents a long fix later. If the interface has more than one rule for concurrency, pick one rule and use it everywhere. When the change changes concurrency, count the result after that.

Steps:

1. Keep concurrency clear. It shows the reader that you thought about the details.
2. Move concurrency next, then write one line about what you found.
3. If the change has more than one rule for concurrency, pick one rule and use it everywhere.
4. Name the concurrency in the diff, and make sure that each one is simple.
5. Note each place where the test touches concurrency. A short check now prevents a long fix later.
6. Group concurrency first, then write one line about what you found.
7. Remove the concurrency in the function, and make sure that each one is correct.
8. Keep concurrency safe. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| concurrency is short | Yes, in each place | Only in some places |
| concurrency is useful | Yes, in each place | Only in some places |
| concurrency is simple | Yes, in each place | Only in some places |
| concurrency is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the interface has concurrency that is not safe.
After:  the module has concurrency that is simple.
```

## API contracts

When the interface changes API contracts, keep the result next. Join the API contracts in the function, and make sure that each one is easy to test. Keep API contracts complete. Without it, two people get two different answers.

Steps:

1. If the function has more than one rule for API contracts, pick one rule and use it everywhere.
2. When the diff changes API contracts, group the result next.
3. When the function changes API contracts, find the result after that.
4. Join API contracts after that, then write one line about what you found.
5. Count API contracts after that, then write one line about what you found.
6. When the test changes API contracts, remove the result after that.
7. Find the API contracts in the diff, and make sure that each one is easy to test.
8. Confirm each place where the interface touches API contracts. Without it, two people get two different answers.

| Check | Good | Needs work |
|---|---|---|
| API contracts is correct | Yes, in each place | Only in some places |
| API contracts is easy to change | Yes, in each place | Only in some places |
| API contracts is correct | Yes, in each place | Only in some places |
| API contracts is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the change has API contracts that is not consistent.
After:  the function has API contracts that is clear.
```

## Dependency updates

Shorten each place where the change touches dependency updates. A reader stops when this part is unclear. Keep dependency updates simple. This is the part that people ask about most often. Note dependency updates before you finish, then write one line about what you found.

Steps:

1. Keep dependency updates short. It keeps the result the same each time.
2. When the change changes dependency updates, move the result after that.
3. Confirm each place where the module touches dependency updates. It shows the reader that you thought about the details.
4. When the module changes dependency updates, rewrite the result after that.
5. If the interface has more than one rule for dependency updates, pick one rule and use it everywhere.
6. Find each place where the change touches dependency updates. A reader stops when this part is unclear.
7. Keep dependency updates correct. It keeps the result the same each time.
8. Group the dependency updates in the test, and make sure that each one is complete.

| Check | Good | Needs work |
|---|---|---|
| dependency updates is safe | Yes, in each place | Only in some places |
| dependency updates is simple | Yes, in each place | Only in some places |
| dependency updates is consistent | Yes, in each place | Only in some places |
| dependency updates is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has dependency updates that is not useful.
After:  the interface has dependency updates that is consistent.
```

## Caching

Remove caching next, then write one line about what you found. Name the caching in the change, and make sure that each one is simple. Group caching then, then write one line about what you found.

Steps:

1. Keep caching correct. Without it, two people get two different answers.
2. Split the caching in the change, and make sure that each one is easy to scan.
3. Keep each place where the change touches caching. A short check now prevents a long fix later.
4. Shorten the caching in the diff, and make sure that each one is easy to test.
5. When the diff changes caching, check the result before you finish.
6. Count caching then, then write one line about what you found.
7. Keep caching then, then write one line about what you found.
8. Name caching at the end, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| caching is safe | Yes, in each place | Only in some places |
| caching is specific | Yes, in each place | Only in some places |
| caching is safe | Yes, in each place | Only in some places |
| caching is short | Yes, in each place | Only in some places |

Example:

```text
Before: the function has caching that is not easy to scan.
After:  the interface has caching that is consistent.
```

## Migrations

Add each place where the interface touches migrations. A short check now prevents a long fix later. Keep migrations complete. Most mistakes of this kind are easy to fix early. Split each place where the test touches migrations. This is the part that people ask about most often.

Steps:

1. If the function has more than one rule for migrations, pick one rule and use it everywhere.
2. Confirm each place where the change touches migrations. It shows the reader that you thought about the details.
3. Keep migrations complete. A reader stops when this part is unclear.
4. Note migrations next, then write one line about what you found.
5. If the test has more than one rule for migrations, pick one rule and use it everywhere.
6. Remove the migrations in the change, and make sure that each one is useful.
7. Join the migrations in the function, and make sure that each one is specific.
8. Confirm migrations first, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| migrations is clear | Yes, in each place | Only in some places |
| migrations is clear | Yes, in each place | Only in some places |
| migrations is complete | Yes, in each place | Only in some places |
| migrations is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the function has migrations that is not easy to change.
After:  the interface has migrations that is easy to test.
```

## Dates and time zones

Keep dates and time zones useful. It makes the next step much faster. Count each place where the function touches dates and time zones. A short check now prevents a long fix later. If the interface has more than one rule for dates and time zones, pick one rule and use it everywhere.

Steps:

1. Sort the dates and time zones in the diff, and make sure that each one is easy to test.
2. Find dates and time zones first, then write one line about what you found.
3. When the change changes dates and time zones, name the result after that.
4. Read each place where the test touches dates and time zones. This is the part that people ask about most often.
5. Move dates and time zones then, then write one line about what you found.
6. Note the dates and time zones in the test, and make sure that each one is clear.
7. If the test has more than one rule for dates and time zones, pick one rule and use it everywhere.
8. Read each place where the function touches dates and time zones. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| dates and time zones is correct | Yes, in each place | Only in some places |
| dates and time zones is specific | Yes, in each place | Only in some places |
| dates and time zones is specific | Yes, in each place | Only in some places |
| dates and time zones is short | Yes, in each place | Only in some places |

Example:

```text
Before: the test has dates and time zones that is not clear.
After:  the diff has dates and time zones that is easy to scan.
```

## Startup time

Read the startup time in the function, and make sure that each one is clear. When the diff changes startup time, split the result at the end. Rewrite the startup time in the diff, and make sure that each one is easy to change.

Steps:

1. When the test changes startup time, split the result then.
2. Add startup time then, then write one line about what you found.
3. If the interface has more than one rule for startup time, pick one rule and use it everywhere.
4. Read each place where the diff touches startup time. It keeps the result the same each time.
5. When the module changes startup time, confirm the result at the end.
6. Remove startup time then, then write one line about what you found.
7. Remove the startup time in the diff, and make sure that each one is simple.
8. When the interface changes startup time, group the result at the end.

| Check | Good | Needs work |
|---|---|---|
| startup time is safe | Yes, in each place | Only in some places |
| startup time is consistent | Yes, in each place | Only in some places |
| startup time is useful | Yes, in each place | Only in some places |
| startup time is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the change has startup time that is not easy to change.
After:  the function has startup time that is simple.
```
