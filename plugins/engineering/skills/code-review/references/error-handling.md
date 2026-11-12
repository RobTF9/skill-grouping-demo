# Error handling

## Feature flags

When the change changes feature flags, remove the result first. When the module changes feature flags, check the result before you finish. If the test has more than one rule for feature flags, pick one rule and use it everywhere.

Steps:

1. When the interface changes feature flags, split the result before you finish.
2. Count each place where the function touches feature flags. It keeps the result the same each time.
3. Keep feature flags useful. A short check now prevents a long fix later.
4. Find the feature flags in the test, and make sure that each one is safe.
5. Move each place where the function touches feature flags. A reader stops when this part is unclear.
6. Note each place where the interface touches feature flags. This is the part that people ask about most often.
7. Sort each place where the test touches feature flags. This is the part that people ask about most often.
8. Sort the feature flags in the diff, and make sure that each one is easy to scan.

| Check | Good | Needs work |
|---|---|---|
| feature flags is easy to test | Yes, in each place | Only in some places |
| feature flags is useful | Yes, in each place | Only in some places |
| feature flags is clear | Yes, in each place | Only in some places |
| feature flags is short | Yes, in each place | Only in some places |

Example:

```text
Before: the test has feature flags that is not easy to change.
After:  the test has feature flags that is simple.
```

## Logging

When the test changes logging, add the result before you finish. Keep logging complete. A short check now prevents a long fix later. Split the logging in the interface, and make sure that each one is easy to scan.

Steps:

1. When the module changes logging, mark the result before you finish.
2. Confirm the logging in the change, and make sure that each one is safe.
3. Rewrite the logging in the function, and make sure that each one is simple.
4. If the module has more than one rule for logging, pick one rule and use it everywhere.
5. Compare the logging in the function, and make sure that each one is simple.
6. When the test changes logging, mark the result after that.
7. If the module has more than one rule for logging, pick one rule and use it everywhere.
8. Mark each place where the function touches logging. This saves time for the next person who reads it.

| Check | Good | Needs work |
|---|---|---|
| logging is simple | Yes, in each place | Only in some places |
| logging is clear | Yes, in each place | Only in some places |
| logging is easy to test | Yes, in each place | Only in some places |
| logging is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the function has logging that is not easy to test.
After:  the test has logging that is safe.
```

## Type safety

Name each place where the function touches type safety. Most mistakes of this kind are easy to fix early. If the module has more than one rule for type safety, pick one rule and use it everywhere. When the interface changes type safety, compare the result then.

Steps:

1. Note each place where the test touches type safety. Most mistakes of this kind are easy to fix early.
2. Group type safety next, then write one line about what you found.
3. Add type safety after that, then write one line about what you found.
4. If the module has more than one rule for type safety, pick one rule and use it everywhere.
5. Rewrite the type safety in the diff, and make sure that each one is clear.
6. Name type safety after that, then write one line about what you found.
7. If the diff has more than one rule for type safety, pick one rule and use it everywhere.
8. Name the type safety in the change, and make sure that each one is useful.

| Check | Good | Needs work |
|---|---|---|
| type safety is clear | Yes, in each place | Only in some places |
| type safety is safe | Yes, in each place | Only in some places |
| type safety is complete | Yes, in each place | Only in some places |
| type safety is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the module has type safety that is not short.
After:  the interface has type safety that is easy to test.
```

## Retries

Check the retries in the interface, and make sure that each one is short. Move the retries in the diff, and make sure that each one is easy to scan. When the test changes retries, join the result next.

Steps:

1. Keep retries easy to test. Without it, two people get two different answers.
2. Move retries at the end, then write one line about what you found.
3. If the interface has more than one rule for retries, pick one rule and use it everywhere.
4. Sort each place where the function touches retries. Most mistakes of this kind are easy to fix early.
5. If the function has more than one rule for retries, pick one rule and use it everywhere.
6. Count retries before you finish, then write one line about what you found.
7. Keep retries specific. It keeps the result the same each time.
8. Rewrite retries then, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| retries is safe | Yes, in each place | Only in some places |
| retries is useful | Yes, in each place | Only in some places |
| retries is easy to scan | Yes, in each place | Only in some places |
| retries is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the module has retries that is not complete.
After:  the change has retries that is easy to scan.
```

## Concurrency

Keep concurrency correct. Small problems here often become large problems later. Keep concurrency correct. Most mistakes of this kind are easy to fix early. Mark concurrency first, then write one line about what you found.

Steps:

1. If the test has more than one rule for concurrency, pick one rule and use it everywhere.
2. Keep concurrency useful. Small problems here often become large problems later.
3. Keep concurrency safe. This saves time for the next person who reads it.
4. Keep concurrency easy to change. Small problems here often become large problems later.
5. Keep concurrency correct. Without it, two people get two different answers.
6. Count each place where the test touches concurrency. This saves time for the next person who reads it.
7. Keep concurrency correct. It makes the next step much faster.
8. Add concurrency next, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| concurrency is clear | Yes, in each place | Only in some places |
| concurrency is complete | Yes, in each place | Only in some places |
| concurrency is simple | Yes, in each place | Only in some places |
| concurrency is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the test has concurrency that is not specific.
After:  the module has concurrency that is specific.
```

## Recursion

Find recursion next, then write one line about what you found. Keep recursion easy to test. A short check now prevents a long fix later. Join each place where the change touches recursion. It makes the next step much faster.

Steps:

1. If the diff has more than one rule for recursion, pick one rule and use it everywhere.
2. Add each place where the module touches recursion. A reader stops when this part is unclear.
3. When the function changes recursion, mark the result next.
4. Confirm the recursion in the test, and make sure that each one is simple.
5. If the interface has more than one rule for recursion, pick one rule and use it everywhere.
6. When the test changes recursion, add the result then.
7. Keep recursion simple. This saves time for the next person who reads it.
8. Mark the recursion in the function, and make sure that each one is short.

| Check | Good | Needs work |
|---|---|---|
| recursion is easy to test | Yes, in each place | Only in some places |
| recursion is specific | Yes, in each place | Only in some places |
| recursion is safe | Yes, in each place | Only in some places |
| recursion is short | Yes, in each place | Only in some places |

Example:

```text
Before: the interface has recursion that is not safe.
After:  the change has recursion that is specific.
```

## Null checks

Mark each place where the change touches null checks. A reader stops when this part is unclear. When the test changes null checks, remove the result after that. Rewrite each place where the diff touches null checks. This is the part that people ask about most often.

Steps:

1. Keep null checks correct. It makes the next step much faster.
2. Rewrite the null checks in the diff, and make sure that each one is safe.
3. Keep null checks short. It shows the reader that you thought about the details.
4. Read the null checks in the interface, and make sure that each one is complete.
5. Keep null checks after that, then write one line about what you found.
6. Keep null checks safe. It shows the reader that you thought about the details.
7. If the change has more than one rule for null checks, pick one rule and use it everywhere.
8. Rewrite the null checks in the interface, and make sure that each one is consistent.

| Check | Good | Needs work |
|---|---|---|
| null checks is easy to change | Yes, in each place | Only in some places |
| null checks is easy to scan | Yes, in each place | Only in some places |
| null checks is easy to change | Yes, in each place | Only in some places |
| null checks is short | Yes, in each place | Only in some places |

Example:

```text
Before: the function has null checks that is not easy to change.
After:  the function has null checks that is useful.
```

## Database queries

Mark each place where the test touches database queries. It makes the next step much faster. When the function changes database queries, count the result first. When the function changes database queries, mark the result first.

Steps:

1. Keep database queries easy to test. Small problems here often become large problems later.
2. Keep database queries correct. It keeps the result the same each time.
3. Mark each place where the change touches database queries. It keeps the result the same each time.
4. Keep database queries easy to scan. A reader stops when this part is unclear.
5. If the interface has more than one rule for database queries, pick one rule and use it everywhere.
6. Move database queries before you finish, then write one line about what you found.
7. Rewrite each place where the diff touches database queries. Small problems here often become large problems later.
8. Find the database queries in the change, and make sure that each one is easy to change.

| Check | Good | Needs work |
|---|---|---|
| database queries is consistent | Yes, in each place | Only in some places |
| database queries is specific | Yes, in each place | Only in some places |
| database queries is short | Yes, in each place | Only in some places |
| database queries is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the change has database queries that is not easy to scan.
After:  the function has database queries that is simple.
```

## Public interfaces

Find public interfaces before you finish, then write one line about what you found. When the diff changes public interfaces, rewrite the result at the end. Check public interfaces first, then write one line about what you found.

Steps:

1. If the diff has more than one rule for public interfaces, pick one rule and use it everywhere.
2. Group each place where the interface touches public interfaces. A reader stops when this part is unclear.
3. Sort public interfaces then, then write one line about what you found.
4. Check public interfaces at the end, then write one line about what you found.
5. If the interface has more than one rule for public interfaces, pick one rule and use it everywhere.
6. Move public interfaces next, then write one line about what you found.
7. Keep public interfaces specific. Small problems here often become large problems later.
8. When the test changes public interfaces, find the result next.

| Check | Good | Needs work |
|---|---|---|
| public interfaces is clear | Yes, in each place | Only in some places |
| public interfaces is useful | Yes, in each place | Only in some places |
| public interfaces is correct | Yes, in each place | Only in some places |
| public interfaces is short | Yes, in each place | Only in some places |

Example:

```text
Before: the test has public interfaces that is not easy to test.
After:  the function has public interfaces that is easy to change.
```

## Pagination

Rewrite each place where the test touches pagination. A reader stops when this part is unclear. If the diff has more than one rule for pagination, pick one rule and use it everywhere. Shorten each place where the test touches pagination. A short check now prevents a long fix later.

Steps:

1. List each place where the change touches pagination. It keeps the result the same each time.
2. Keep pagination complete. This is the part that people ask about most often.
3. Shorten each place where the function touches pagination. A reader stops when this part is unclear.
4. Join each place where the interface touches pagination. This saves time for the next person who reads it.
5. Count the pagination in the test, and make sure that each one is easy to test.
6. Confirm the pagination in the test, and make sure that each one is short.
7. Note pagination next, then write one line about what you found.
8. If the function has more than one rule for pagination, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| pagination is safe | Yes, in each place | Only in some places |
| pagination is easy to change | Yes, in each place | Only in some places |
| pagination is useful | Yes, in each place | Only in some places |
| pagination is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the interface has pagination that is not useful.
After:  the module has pagination that is clear.
```

## Caching

If the diff has more than one rule for caching, pick one rule and use it everywhere. Note each place where the change touches caching. It shows the reader that you thought about the details. Shorten caching after that, then write one line about what you found.

Steps:

1. Confirm the caching in the diff, and make sure that each one is easy to scan.
2. If the function has more than one rule for caching, pick one rule and use it everywhere.
3. Keep caching short. It makes the next step much faster.
4. Keep the caching in the interface, and make sure that each one is simple.
5. Compare the caching in the test, and make sure that each one is consistent.
6. Group caching at the end, then write one line about what you found.
7. When the interface changes caching, mark the result after that.
8. When the module changes caching, count the result before you finish.

| Check | Good | Needs work |
|---|---|---|
| caching is consistent | Yes, in each place | Only in some places |
| caching is easy to test | Yes, in each place | Only in some places |
| caching is complete | Yes, in each place | Only in some places |
| caching is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the interface has caching that is not consistent.
After:  the test has caching that is specific.
```

## Migrations

Count the migrations in the module, and make sure that each one is easy to change. Find migrations at the end, then write one line about what you found. Sort each place where the module touches migrations. It keeps the result the same each time.

Steps:

1. If the test has more than one rule for migrations, pick one rule and use it everywhere.
2. When the interface changes migrations, remove the result then.
3. When the test changes migrations, name the result at the end.
4. When the test changes migrations, find the result then.
5. When the function changes migrations, read the result then.
6. Keep migrations useful. It shows the reader that you thought about the details.
7. Check the migrations in the diff, and make sure that each one is clear.
8. Split the migrations in the function, and make sure that each one is easy to test.

| Check | Good | Needs work |
|---|---|---|
| migrations is easy to scan | Yes, in each place | Only in some places |
| migrations is safe | Yes, in each place | Only in some places |
| migrations is specific | Yes, in each place | Only in some places |
| migrations is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the test has migrations that is not correct.
After:  the change has migrations that is clear.
```

## Money values

Mark money values first, then write one line about what you found. Count money values next, then write one line about what you found. Name money values first, then write one line about what you found.

Steps:

1. If the change has more than one rule for money values, pick one rule and use it everywhere.
2. When the diff changes money values, read the result before you finish.
3. Count each place where the test touches money values. Small problems here often become large problems later.
4. Join each place where the module touches money values. Small problems here often become large problems later.
5. Keep money values safe. A reader stops when this part is unclear.
6. Shorten money values at the end, then write one line about what you found.
7. When the function changes money values, remove the result before you finish.
8. Count each place where the interface touches money values. Small problems here often become large problems later.

| Check | Good | Needs work |
|---|---|---|
| money values is simple | Yes, in each place | Only in some places |
| money values is easy to change | Yes, in each place | Only in some places |
| money values is useful | Yes, in each place | Only in some places |
| money values is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the function has money values that is not clear.
After:  the interface has money values that is useful.
```

## Timeouts

Keep timeouts simple. A reader stops when this part is unclear. If the interface has more than one rule for timeouts, pick one rule and use it everywhere. Keep timeouts specific. Most mistakes of this kind are easy to fix early.

Steps:

1. Add timeouts first, then write one line about what you found.
2. When the interface changes timeouts, name the result at the end.
3. List each place where the diff touches timeouts. Small problems here often become large problems later.
4. Read timeouts next, then write one line about what you found.
5. Check the timeouts in the test, and make sure that each one is useful.
6. Keep timeouts simple. Small problems here often become large problems later.
7. Sort each place where the diff touches timeouts. This is the part that people ask about most often.
8. Read the timeouts in the diff, and make sure that each one is complete.

| Check | Good | Needs work |
|---|---|---|
| timeouts is easy to test | Yes, in each place | Only in some places |
| timeouts is complete | Yes, in each place | Only in some places |
| timeouts is short | Yes, in each place | Only in some places |
| timeouts is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the test has timeouts that is not easy to test.
After:  the module has timeouts that is simple.
```
