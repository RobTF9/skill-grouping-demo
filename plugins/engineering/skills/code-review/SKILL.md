---
name: code-review
description: Review a pull request for correctness, safety, speed and readability.
---

# Code review

Read the whole diff before you write a comment. List bugs first, then risks, then readability issues. Keep each comment short and say why it matters.

## Error handling

When the diff changes error handling, mark the result after that. Keep error handling then, then write one line about what you found. Note each place where the diff touches error handling. A short check now prevents a long fix later.

Steps:

1. Count each place where the diff touches error handling. It keeps the result the same each time.
2. When the change changes error handling, note the result before you finish.
3. When the module changes error handling, list the result after that.
4. Count each place where the module touches error handling. This is the part that people ask about most often.
5. If the change has more than one rule for error handling, pick one rule and use it everywhere.
6. If the diff has more than one rule for error handling, pick one rule and use it everywhere.
7. Keep error handling specific. It shows the reader that you thought about the details.
8. If the change has more than one rule for error handling, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| error handling is correct | Yes, in each place | Only in some places |
| error handling is consistent | Yes, in each place | Only in some places |
| error handling is specific | Yes, in each place | Only in some places |
| error handling is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has error handling that is not specific.
After:  the module has error handling that is specific.
```

## Events

Sort events first, then write one line about what you found. Keep events useful. A short check now prevents a long fix later. Count events first, then write one line about what you found.

Steps:

1. Keep events safe. It shows the reader that you thought about the details.
2. Count events before you finish, then write one line about what you found.
3. If the function has more than one rule for events, pick one rule and use it everywhere.
4. Confirm each place where the test touches events. This is the part that people ask about most often.
5. Keep events at the end, then write one line about what you found.
6. Keep events clear. Small problems here often become large problems later.
7. If the function has more than one rule for events, pick one rule and use it everywhere.
8. Keep events short. Most mistakes of this kind are easy to fix early.

| Check | Good | Needs work |
|---|---|---|
| events is easy to change | Yes, in each place | Only in some places |
| events is easy to test | Yes, in each place | Only in some places |
| events is easy to test | Yes, in each place | Only in some places |
| events is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the interface has events that is not correct.
After:  the diff has events that is easy to scan.
```

## Money values

When the module changes money values, name the result first. Name each place where the change touches money values. This saves time for the next person who reads it. When the diff changes money values, shorten the result before you finish.

Steps:

1. Split the money values in the function, and make sure that each one is specific.
2. Split each place where the module touches money values. This saves time for the next person who reads it.
3. Keep money values safe. Small problems here often become large problems later.
4. If the change has more than one rule for money values, pick one rule and use it everywhere.
5. Keep money values correct. It shows the reader that you thought about the details.
6. Keep the money values in the test, and make sure that each one is complete.
7. Remove the money values in the test, and make sure that each one is consistent.
8. Shorten money values first, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| money values is consistent | Yes, in each place | Only in some places |
| money values is consistent | Yes, in each place | Only in some places |
| money values is safe | Yes, in each place | Only in some places |
| money values is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the function has money values that is not consistent.
After:  the function has money values that is useful.
```

## Mocks

Keep the mocks in the module, and make sure that each one is easy to scan. Keep mocks specific. It keeps the result the same each time. Move the mocks in the module, and make sure that each one is easy to scan.

Steps:

1. When the module changes mocks, join the result before you finish.
2. Add each place where the change touches mocks. It keeps the result the same each time.
3. Join each place where the module touches mocks. This saves time for the next person who reads it.
4. List the mocks in the function, and make sure that each one is simple.
5. If the change has more than one rule for mocks, pick one rule and use it everywhere.
6. Find each place where the function touches mocks. A short check now prevents a long fix later.
7. Keep mocks easy to test. This saves time for the next person who reads it.
8. When the change changes mocks, keep the result first.

| Check | Good | Needs work |
|---|---|---|
| mocks is clear | Yes, in each place | Only in some places |
| mocks is easy to scan | Yes, in each place | Only in some places |
| mocks is safe | Yes, in each place | Only in some places |
| mocks is short | Yes, in each place | Only in some places |

Example:

```text
Before: the test has mocks that is not consistent.
After:  the change has mocks that is short.
```

## Logging

Check each place where the change touches logging. Small problems here often become large problems later. If the diff has more than one rule for logging, pick one rule and use it everywhere. List the logging in the diff, and make sure that each one is short.

Steps:

1. Rewrite the logging in the test, and make sure that each one is safe.
2. If the test has more than one rule for logging, pick one rule and use it everywhere.
3. Count logging before you finish, then write one line about what you found.
4. When the change changes logging, join the result next.
5. Keep logging easy to test. A reader stops when this part is unclear.
6. When the function changes logging, rewrite the result next.
7. When the interface changes logging, remove the result then.
8. Shorten logging first, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| logging is easy to test | Yes, in each place | Only in some places |
| logging is consistent | Yes, in each place | Only in some places |
| logging is easy to scan | Yes, in each place | Only in some places |
| logging is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the interface has logging that is not easy to test.
After:  the module has logging that is correct.
```

## Comments

Shorten comments first, then write one line about what you found. Keep comments useful. A reader stops when this part is unclear. Remove the comments in the test, and make sure that each one is simple.

Steps:

1. Add the comments in the function, and make sure that each one is easy to scan.
2. Read the comments in the diff, and make sure that each one is safe.
3. If the diff has more than one rule for comments, pick one rule and use it everywhere.
4. If the diff has more than one rule for comments, pick one rule and use it everywhere.
5. Name comments next, then write one line about what you found.
6. List comments then, then write one line about what you found.
7. Mark comments then, then write one line about what you found.
8. Sort the comments in the change, and make sure that each one is specific.

| Check | Good | Needs work |
|---|---|---|
| comments is safe | Yes, in each place | Only in some places |
| comments is correct | Yes, in each place | Only in some places |
| comments is easy to test | Yes, in each place | Only in some places |
| comments is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has comments that is not easy to change.
After:  the interface has comments that is consistent.
```

## File handling

Name file handling at the end, then write one line about what you found. Find the file handling in the diff, and make sure that each one is consistent. Add each place where the change touches file handling. A reader stops when this part is unclear.

Steps:

1. Keep file handling specific. It shows the reader that you thought about the details.
2. Add each place where the module touches file handling. Small problems here often become large problems later.
3. When the diff changes file handling, move the result after that.
4. Keep file handling consistent. This is the part that people ask about most often.
5. If the test has more than one rule for file handling, pick one rule and use it everywhere.
6. When the function changes file handling, add the result then.
7. When the test changes file handling, note the result next.
8. When the interface changes file handling, rewrite the result before you finish.

| Check | Good | Needs work |
|---|---|---|
| file handling is safe | Yes, in each place | Only in some places |
| file handling is clear | Yes, in each place | Only in some places |
| file handling is correct | Yes, in each place | Only in some places |
| file handling is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the change has file handling that is not easy to change.
After:  the change has file handling that is specific.
```

## API contracts

Note API contracts at the end, then write one line about what you found. Compare API contracts at the end, then write one line about what you found. Join API contracts at the end, then write one line about what you found.

Steps:

1. If the diff has more than one rule for API contracts, pick one rule and use it everywhere.
2. Mark each place where the module touches API contracts. Without it, two people get two different answers.
3. If the interface has more than one rule for API contracts, pick one rule and use it everywhere.
4. Keep API contracts useful. A reader stops when this part is unclear.
5. When the function changes API contracts, group the result after that.
6. When the interface changes API contracts, compare the result at the end.
7. Confirm the API contracts in the change, and make sure that each one is safe.
8. Compare each place where the function touches API contracts. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| API contracts is easy to change | Yes, in each place | Only in some places |
| API contracts is consistent | Yes, in each place | Only in some places |
| API contracts is safe | Yes, in each place | Only in some places |
| API contracts is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the test has API contracts that is not consistent.
After:  the interface has API contracts that is correct.
```

## Dates and time zones

Add the dates and time zones in the test, and make sure that each one is correct. Compare the dates and time zones in the module, and make sure that each one is consistent. Group each place where the change touches dates and time zones. A reader stops when this part is unclear.

Steps:

1. If the module has more than one rule for dates and time zones, pick one rule and use it everywhere.
2. Keep dates and time zones easy to scan. It makes the next step much faster.
3. Compare dates and time zones next, then write one line about what you found.
4. Sort dates and time zones then, then write one line about what you found.
5. Join the dates and time zones in the diff, and make sure that each one is clear.
6. When the diff changes dates and time zones, remove the result next.
7. Add each place where the change touches dates and time zones. A reader stops when this part is unclear.
8. Note the dates and time zones in the module, and make sure that each one is simple.

| Check | Good | Needs work |
|---|---|---|
| dates and time zones is correct | Yes, in each place | Only in some places |
| dates and time zones is specific | Yes, in each place | Only in some places |
| dates and time zones is clear | Yes, in each place | Only in some places |
| dates and time zones is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the function has dates and time zones that is not clear.
After:  the diff has dates and time zones that is consistent.
```

## Null checks

Keep null checks clear. Most mistakes of this kind are easy to fix early. When the function changes null checks, find the result first. If the change has more than one rule for null checks, pick one rule and use it everywhere.

Steps:

1. Keep null checks safe. Most mistakes of this kind are easy to fix early.
2. Group the null checks in the interface, and make sure that each one is correct.
3. List each place where the interface touches null checks. Small problems here often become large problems later.
4. If the interface has more than one rule for null checks, pick one rule and use it everywhere.
5. Keep null checks complete. A reader stops when this part is unclear.
6. Mark the null checks in the function, and make sure that each one is useful.
7. When the test changes null checks, rewrite the result at the end.
8. Read each place where the function touches null checks. A short check now prevents a long fix later.

| Check | Good | Needs work |
|---|---|---|
| null checks is easy to change | Yes, in each place | Only in some places |
| null checks is clear | Yes, in each place | Only in some places |
| null checks is specific | Yes, in each place | Only in some places |
| null checks is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the function has null checks that is not easy to test.
After:  the function has null checks that is specific.
```

## Dependency updates

If the diff has more than one rule for dependency updates, pick one rule and use it everywhere. If the function has more than one rule for dependency updates, pick one rule and use it everywhere. Split each place where the test touches dependency updates. Without it, two people get two different answers.

Steps:

1. Confirm dependency updates before you finish, then write one line about what you found.
2. Read dependency updates after that, then write one line about what you found.
3. Keep the dependency updates in the test, and make sure that each one is clear.
4. Note each place where the module touches dependency updates. Most mistakes of this kind are easy to fix early.
5. Check dependency updates at the end, then write one line about what you found.
6. Keep dependency updates consistent. This is the part that people ask about most often.
7. When the test changes dependency updates, check the result after that.
8. Count the dependency updates in the interface, and make sure that each one is complete.

| Check | Good | Needs work |
|---|---|---|
| dependency updates is easy to change | Yes, in each place | Only in some places |
| dependency updates is useful | Yes, in each place | Only in some places |
| dependency updates is correct | Yes, in each place | Only in some places |
| dependency updates is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has dependency updates that is not easy to scan.
After:  the test has dependency updates that is clear.
```

## Dead code

Find the dead code in the diff, and make sure that each one is correct. Rewrite the dead code in the interface, and make sure that each one is correct. Read dead code first, then write one line about what you found.

Steps:

1. When the function changes dead code, check the result after that.
2. Name each place where the module touches dead code. A reader stops when this part is unclear.
3. Keep dead code complete. It makes the next step much faster.
4. Move dead code before you finish, then write one line about what you found.
5. When the function changes dead code, add the result then.
6. If the interface has more than one rule for dead code, pick one rule and use it everywhere.
7. If the test has more than one rule for dead code, pick one rule and use it everywhere.
8. Split each place where the change touches dead code. A short check now prevents a long fix later.

| Check | Good | Needs work |
|---|---|---|
| dead code is easy to change | Yes, in each place | Only in some places |
| dead code is easy to change | Yes, in each place | Only in some places |
| dead code is safe | Yes, in each place | Only in some places |
| dead code is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the test has dead code that is not short.
After:  the change has dead code that is simple.
```

## Recursion

Sort each place where the module touches recursion. This saves time for the next person who reads it. If the module has more than one rule for recursion, pick one rule and use it everywhere. When the function changes recursion, rewrite the result after that.

Steps:

1. If the interface has more than one rule for recursion, pick one rule and use it everywhere.
2. When the module changes recursion, join the result next.
3. When the change changes recursion, rewrite the result then.
4. If the change has more than one rule for recursion, pick one rule and use it everywhere.
5. When the module changes recursion, remove the result at the end.
6. Keep recursion clear. A reader stops when this part is unclear.
7. When the function changes recursion, group the result before you finish.
8. Confirm the recursion in the module, and make sure that each one is easy to test.

| Check | Good | Needs work |
|---|---|---|
| recursion is useful | Yes, in each place | Only in some places |
| recursion is safe | Yes, in each place | Only in some places |
| recursion is complete | Yes, in each place | Only in some places |
| recursion is short | Yes, in each place | Only in some places |

Example:

```text
Before: the function has recursion that is not easy to test.
After:  the diff has recursion that is complete.
```

## Feature flags

If the interface has more than one rule for feature flags, pick one rule and use it everywhere. Keep feature flags easy to test. Small problems here often become large problems later. If the diff has more than one rule for feature flags, pick one rule and use it everywhere.

Steps:

1. Rewrite feature flags next, then write one line about what you found.
2. If the test has more than one rule for feature flags, pick one rule and use it everywhere.
3. When the diff changes feature flags, remove the result at the end.
4. Keep feature flags specific. It shows the reader that you thought about the details.
5. When the change changes feature flags, count the result next.
6. Group feature flags after that, then write one line about what you found.
7. Name each place where the module touches feature flags. Without it, two people get two different answers.
8. Keep feature flags safe. It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| feature flags is simple | Yes, in each place | Only in some places |
| feature flags is easy to test | Yes, in each place | Only in some places |
| feature flags is consistent | Yes, in each place | Only in some places |
| feature flags is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the function has feature flags that is not easy to test.
After:  the function has feature flags that is useful.
```

## Test coverage

When the change changes test coverage, confirm the result then. Group each place where the function touches test coverage. Small problems here often become large problems later. If the change has more than one rule for test coverage, pick one rule and use it everywhere.

Steps:

1. Keep test coverage short. It shows the reader that you thought about the details.
2. Keep each place where the function touches test coverage. Without it, two people get two different answers.
3. Remove test coverage at the end, then write one line about what you found.
4. If the interface has more than one rule for test coverage, pick one rule and use it everywhere.
5. Add the test coverage in the function, and make sure that each one is simple.
6. Keep test coverage easy to change. A reader stops when this part is unclear.
7. Name each place where the function touches test coverage. Small problems here often become large problems later.
8. When the module changes test coverage, remove the result next.

| Check | Good | Needs work |
|---|---|---|
| test coverage is clear | Yes, in each place | Only in some places |
| test coverage is simple | Yes, in each place | Only in some places |
| test coverage is safe | Yes, in each place | Only in some places |
| test coverage is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the test has test coverage that is not safe.
After:  the diff has test coverage that is easy to change.
```

## Database queries

If the change has more than one rule for database queries, pick one rule and use it everywhere. Keep database queries correct. This saves time for the next person who reads it. If the diff has more than one rule for database queries, pick one rule and use it everywhere.

Steps:

1. Read each place where the interface touches database queries. It makes the next step much faster.
2. Move the database queries in the change, and make sure that each one is useful.
3. Split database queries then, then write one line about what you found.
4. Find the database queries in the change, and make sure that each one is correct.
5. Add each place where the module touches database queries. A reader stops when this part is unclear.
6. When the module changes database queries, list the result then.
7. Keep database queries simple. It keeps the result the same each time.
8. If the test has more than one rule for database queries, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| database queries is easy to test | Yes, in each place | Only in some places |
| database queries is short | Yes, in each place | Only in some places |
| database queries is easy to scan | Yes, in each place | Only in some places |
| database queries is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the change has database queries that is not easy to test.
After:  the module has database queries that is simple.
```

## Timeouts

When the interface changes timeouts, remove the result after that. When the test changes timeouts, name the result next. Keep timeouts safe. This is the part that people ask about most often.

Steps:

1. Check each place where the change touches timeouts. This saves time for the next person who reads it.
2. Keep the timeouts in the test, and make sure that each one is specific.
3. Keep timeouts consistent. This is the part that people ask about most often.
4. Read each place where the diff touches timeouts. It makes the next step much faster.
5. If the test has more than one rule for timeouts, pick one rule and use it everywhere.
6. Confirm timeouts then, then write one line about what you found.
7. When the change changes timeouts, read the result before you finish.
8. If the module has more than one rule for timeouts, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| timeouts is simple | Yes, in each place | Only in some places |
| timeouts is correct | Yes, in each place | Only in some places |
| timeouts is short | Yes, in each place | Only in some places |
| timeouts is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the change has timeouts that is not clear.
After:  the interface has timeouts that is easy to test.
```

## Startup time

When the change changes startup time, group the result next. Check the startup time in the diff, and make sure that each one is specific. Compare startup time first, then write one line about what you found.

Steps:

1. Keep each place where the change touches startup time. A reader stops when this part is unclear.
2. List each place where the function touches startup time. It shows the reader that you thought about the details.
3. Note the startup time in the diff, and make sure that each one is simple.
4. When the function changes startup time, shorten the result after that.
5. If the test has more than one rule for startup time, pick one rule and use it everywhere.
6. Remove the startup time in the diff, and make sure that each one is easy to change.
7. If the function has more than one rule for startup time, pick one rule and use it everywhere.
8. Keep startup time specific. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| startup time is specific | Yes, in each place | Only in some places |
| startup time is short | Yes, in each place | Only in some places |
| startup time is simple | Yes, in each place | Only in some places |
| startup time is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the module has startup time that is not consistent.
After:  the change has startup time that is correct.
```

## Retries

Join retries at the end, then write one line about what you found. Find retries after that, then write one line about what you found. When the test changes retries, shorten the result first.

Steps:

1. Confirm the retries in the module, and make sure that each one is safe.
2. Move each place where the module touches retries. Small problems here often become large problems later.
3. If the test has more than one rule for retries, pick one rule and use it everywhere.
4. If the function has more than one rule for retries, pick one rule and use it everywhere.
5. Split retries before you finish, then write one line about what you found.
6. If the module has more than one rule for retries, pick one rule and use it everywhere.
7. Keep retries consistent. Without it, two people get two different answers.
8. If the change has more than one rule for retries, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| retries is easy to change | Yes, in each place | Only in some places |
| retries is complete | Yes, in each place | Only in some places |
| retries is safe | Yes, in each place | Only in some places |
| retries is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the test has retries that is not easy to test.
After:  the interface has retries that is consistent.
```

## Type safety

Split each place where the module touches type safety. It makes the next step much faster. Name each place where the module touches type safety. Small problems here often become large problems later. If the diff has more than one rule for type safety, pick one rule and use it everywhere.

Steps:

1. Confirm each place where the module touches type safety. Most mistakes of this kind are easy to fix early.
2. Move each place where the change touches type safety. This saves time for the next person who reads it.
3. Rewrite type safety at the end, then write one line about what you found.
4. Keep type safety after that, then write one line about what you found.
5. Keep type safety complete. Small problems here often become large problems later.
6. When the test changes type safety, check the result then.
7. Keep type safety specific. A short check now prevents a long fix later.
8. If the module has more than one rule for type safety, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| type safety is clear | Yes, in each place | Only in some places |
| type safety is correct | Yes, in each place | Only in some places |
| type safety is easy to test | Yes, in each place | Only in some places |
| type safety is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the function has type safety that is not complete.
After:  the interface has type safety that is simple.
```

## Public interfaces

If the change has more than one rule for public interfaces, pick one rule and use it everywhere. Move public interfaces next, then write one line about what you found. If the function has more than one rule for public interfaces, pick one rule and use it everywhere.

Steps:

1. When the function changes public interfaces, compare the result first.
2. If the module has more than one rule for public interfaces, pick one rule and use it everywhere.
3. Mark the public interfaces in the module, and make sure that each one is easy to change.
4. Group each place where the diff touches public interfaces. It makes the next step much faster.
5. Read public interfaces before you finish, then write one line about what you found.
6. Check public interfaces before you finish, then write one line about what you found.
7. If the function has more than one rule for public interfaces, pick one rule and use it everywhere.
8. When the interface changes public interfaces, shorten the result then.

| Check | Good | Needs work |
|---|---|---|
| public interfaces is consistent | Yes, in each place | Only in some places |
| public interfaces is easy to scan | Yes, in each place | Only in some places |
| public interfaces is clear | Yes, in each place | Only in some places |
| public interfaces is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the module has public interfaces that is not easy to scan.
After:  the test has public interfaces that is simple.
```

## Caching

If the change has more than one rule for caching, pick one rule and use it everywhere. Keep caching useful. A short check now prevents a long fix later. If the test has more than one rule for caching, pick one rule and use it everywhere.

Steps:

1. Remove each place where the test touches caching. A short check now prevents a long fix later.
2. Remove the caching in the function, and make sure that each one is easy to scan.
3. If the module has more than one rule for caching, pick one rule and use it everywhere.
4. If the interface has more than one rule for caching, pick one rule and use it everywhere.
5. When the module changes caching, mark the result first.
6. Shorten each place where the function touches caching. A short check now prevents a long fix later.
7. Keep caching short. Most mistakes of this kind are easy to fix early.
8. Shorten each place where the diff touches caching. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| caching is correct | Yes, in each place | Only in some places |
| caching is safe | Yes, in each place | Only in some places |
| caching is correct | Yes, in each place | Only in some places |
| caching is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has caching that is not short.
After:  the interface has caching that is useful.
```

## Concurrency

When the function changes concurrency, group the result before you finish. Keep concurrency easy to test. Without it, two people get two different answers. Keep concurrency easy to change. A reader stops when this part is unclear.

Steps:

1. If the module has more than one rule for concurrency, pick one rule and use it everywhere.
2. Compare the concurrency in the module, and make sure that each one is correct.
3. Split the concurrency in the test, and make sure that each one is correct.
4. Rewrite concurrency at the end, then write one line about what you found.
5. Name concurrency before you finish, then write one line about what you found.
6. Keep concurrency safe. Without it, two people get two different answers.
7. If the function has more than one rule for concurrency, pick one rule and use it everywhere.
8. When the test changes concurrency, join the result after that.

| Check | Good | Needs work |
|---|---|---|
| concurrency is safe | Yes, in each place | Only in some places |
| concurrency is easy to change | Yes, in each place | Only in some places |
| concurrency is short | Yes, in each place | Only in some places |
| concurrency is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the test has concurrency that is not specific.
After:  the change has concurrency that is useful.
```

## Pagination

When the test changes pagination, split the result after that. When the function changes pagination, confirm the result at the end. Compare the pagination in the test, and make sure that each one is easy to test.

Steps:

1. When the diff changes pagination, note the result before you finish.
2. When the module changes pagination, note the result at the end.
3. Keep pagination specific. Small problems here often become large problems later.
4. Join each place where the interface touches pagination. This is the part that people ask about most often.
5. Name each place where the interface touches pagination. It keeps the result the same each time.
6. Keep pagination consistent. This is the part that people ask about most often.
7. When the function changes pagination, name the result before you finish.
8. Compare each place where the change touches pagination. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| pagination is clear | Yes, in each place | Only in some places |
| pagination is easy to change | Yes, in each place | Only in some places |
| pagination is complete | Yes, in each place | Only in some places |
| pagination is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has pagination that is not easy to change.
After:  the module has pagination that is simple.
```

## Configuration

Keep configuration easy to scan. This is the part that people ask about most often. Rewrite each place where the module touches configuration. It shows the reader that you thought about the details. When the interface changes configuration, split the result then.

Steps:

1. If the change has more than one rule for configuration, pick one rule and use it everywhere.
2. Sort each place where the change touches configuration. This saves time for the next person who reads it.
3. Shorten configuration next, then write one line about what you found.
4. Note configuration before you finish, then write one line about what you found.
5. Keep configuration consistent. This saves time for the next person who reads it.
6. Confirm the configuration in the function, and make sure that each one is easy to change.
7. Count the configuration in the diff, and make sure that each one is safe.
8. Check the configuration in the function, and make sure that each one is clear.

| Check | Good | Needs work |
|---|---|---|
| configuration is easy to test | Yes, in each place | Only in some places |
| configuration is specific | Yes, in each place | Only in some places |
| configuration is easy to change | Yes, in each place | Only in some places |
| configuration is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the interface has configuration that is not correct.
After:  the interface has configuration that is useful.
```

## Queues

Read the queues in the diff, and make sure that each one is specific. When the function changes queues, check the result first. Keep queues easy to scan. Most mistakes of this kind are easy to fix early.

Steps:

1. Check queues next, then write one line about what you found.
2. Keep queues specific. Most mistakes of this kind are easy to fix early.
3. Keep queues safe. Without it, two people get two different answers.
4. If the module has more than one rule for queues, pick one rule and use it everywhere.
5. Check the queues in the diff, and make sure that each one is clear.
6. Keep queues easy to scan. This saves time for the next person who reads it.
7. When the test changes queues, list the result at the end.
8. Keep queues easy to change. It keeps the result the same each time.

| Check | Good | Needs work |
|---|---|---|
| queues is complete | Yes, in each place | Only in some places |
| queues is short | Yes, in each place | Only in some places |
| queues is consistent | Yes, in each place | Only in some places |
| queues is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has queues that is not consistent.
After:  the function has queues that is clear.
```

## Migrations

Sort each place where the diff touches migrations. Most mistakes of this kind are easy to fix early. Sort migrations next, then write one line about what you found. When the interface changes migrations, add the result at the end.

Steps:

1. Name migrations after that, then write one line about what you found.
2. If the interface has more than one rule for migrations, pick one rule and use it everywhere.
3. Join migrations after that, then write one line about what you found.
4. Confirm each place where the diff touches migrations. A short check now prevents a long fix later.
5. Confirm each place where the function touches migrations. This saves time for the next person who reads it.
6. When the test changes migrations, note the result first.
7. When the interface changes migrations, check the result first.
8. Find migrations at the end, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| migrations is consistent | Yes, in each place | Only in some places |
| migrations is correct | Yes, in each place | Only in some places |
| migrations is easy to change | Yes, in each place | Only in some places |
| migrations is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the module has migrations that is not short.
After:  the change has migrations that is consistent.
```

## Naming

When the module changes naming, compare the result first. When the test changes naming, shorten the result next. Keep naming consistent. A short check now prevents a long fix later.

Steps:

1. Keep naming correct. Without it, two people get two different answers.
2. When the diff changes naming, count the result next.
3. Sort each place where the change touches naming. It keeps the result the same each time.
4. Remove each place where the function touches naming. It keeps the result the same each time.
5. Keep naming easy to change. A short check now prevents a long fix later.
6. If the change has more than one rule for naming, pick one rule and use it everywhere.
7. Keep naming specific. Most mistakes of this kind are easy to fix early.
8. Keep naming useful. It shows the reader that you thought about the details.

| Check | Good | Needs work |
|---|---|---|
| naming is specific | Yes, in each place | Only in some places |
| naming is easy to change | Yes, in each place | Only in some places |
| naming is safe | Yes, in each place | Only in some places |
| naming is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the test has naming that is not easy to scan.
After:  the function has naming that is easy to change.
```

## Loops

Keep loops specific. This is the part that people ask about most often. Name each place where the test touches loops. A reader stops when this part is unclear. Keep loops safe. Small problems here often become large problems later.

Steps:

1. When the interface changes loops, note the result first.
2. Find each place where the test touches loops. It keeps the result the same each time.
3. Keep the loops in the change, and make sure that each one is complete.
4. Keep loops easy to scan. Small problems here often become large problems later.
5. Count the loops in the interface, and make sure that each one is useful.
6. When the change changes loops, confirm the result after that.
7. When the module changes loops, read the result before you finish.
8. When the interface changes loops, shorten the result at the end.

| Check | Good | Needs work |
|---|---|---|
| loops is consistent | Yes, in each place | Only in some places |
| loops is useful | Yes, in each place | Only in some places |
| loops is useful | Yes, in each place | Only in some places |
| loops is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the change has loops that is not easy to test.
After:  the diff has loops that is clear.
```

## Memory use

Move memory use next, then write one line about what you found. If the module has more than one rule for memory use, pick one rule and use it everywhere. Note memory use then, then write one line about what you found.

Steps:

1. Sort memory use at the end, then write one line about what you found.
2. Sort each place where the module touches memory use. This saves time for the next person who reads it.
3. When the function changes memory use, rewrite the result then.
4. Group the memory use in the module, and make sure that each one is useful.
5. When the function changes memory use, compare the result at the end.
6. Sort the memory use in the diff, and make sure that each one is specific.
7. Mark the memory use in the test, and make sure that each one is consistent.
8. If the function has more than one rule for memory use, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| memory use is simple | Yes, in each place | Only in some places |
| memory use is useful | Yes, in each place | Only in some places |
| memory use is short | Yes, in each place | Only in some places |
| memory use is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the test has memory use that is not clear.
After:  the interface has memory use that is complete.
```

## Loops (pass 2)

List the loops (pass 2) in the diff, and make sure that each one is specific. Group each place where the module touches loops (pass 2). Most mistakes of this kind are easy to fix early. Join each place where the interface touches loops (pass 2). This is the part that people ask about most often.

Steps:

1. Find the loops (pass 2) in the module, and make sure that each one is clear.
2. When the function changes loops (pass 2), sort the result after that.
3. If the interface has more than one rule for loops (pass 2), pick one rule and use it everywhere.
4. Keep loops (pass 2) consistent. Small problems here often become large problems later.
5. Rewrite the loops (pass 2) in the change, and make sure that each one is consistent.
6. Add the loops (pass 2) in the diff, and make sure that each one is consistent.
7. Group loops (pass 2) before you finish, then write one line about what you found.
8. If the change has more than one rule for loops (pass 2), pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| loops (pass 2) is specific | Yes, in each place | Only in some places |
| loops (pass 2) is consistent | Yes, in each place | Only in some places |
| loops (pass 2) is easy to test | Yes, in each place | Only in some places |
| loops (pass 2) is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has loops (pass 2) that is not easy to test.
After:  the change has loops (pass 2) that is easy to change.
```

## API contracts (pass 2)

Rewrite each place where the test touches API contracts (pass 2). Without it, two people get two different answers. Check API contracts (pass 2) before you finish, then write one line about what you found. Compare the API contracts (pass 2) in the interface, and make sure that each one is simple.

Steps:

1. Join each place where the module touches API contracts (pass 2). This is the part that people ask about most often.
2. If the module has more than one rule for API contracts (pass 2), pick one rule and use it everywhere.
3. Keep API contracts (pass 2) clear. It keeps the result the same each time.
4. Mark the API contracts (pass 2) in the change, and make sure that each one is short.
5. Name the API contracts (pass 2) in the test, and make sure that each one is easy to test.
6. Join each place where the diff touches API contracts (pass 2). This is the part that people ask about most often.
7. Read API contracts (pass 2) before you finish, then write one line about what you found.
8. Read the API contracts (pass 2) in the interface, and make sure that each one is clear.

| Check | Good | Needs work |
|---|---|---|
| API contracts (pass 2) is consistent | Yes, in each place | Only in some places |
| API contracts (pass 2) is short | Yes, in each place | Only in some places |
| API contracts (pass 2) is easy to change | Yes, in each place | Only in some places |
| API contracts (pass 2) is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the change has API contracts (pass 2) that is not specific.
After:  the interface has API contracts (pass 2) that is safe.
```

## File handling (pass 2)

Split the file handling (pass 2) in the function, and make sure that each one is easy to change. Name each place where the function touches file handling (pass 2). Most mistakes of this kind are easy to fix early. If the test has more than one rule for file handling (pass 2), pick one rule and use it everywhere.

Steps:

1. Keep file handling (pass 2) easy to scan. It keeps the result the same each time.
2. Remove each place where the test touches file handling (pass 2). A short check now prevents a long fix later.
3. Split file handling (pass 2) after that, then write one line about what you found.
4. Count file handling (pass 2) before you finish, then write one line about what you found.
5. If the interface has more than one rule for file handling (pass 2), pick one rule and use it everywhere.
6. Find file handling (pass 2) before you finish, then write one line about what you found.
7. Keep file handling (pass 2) simple. A reader stops when this part is unclear.
8. If the function has more than one rule for file handling (pass 2), pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| file handling (pass 2) is short | Yes, in each place | Only in some places |
| file handling (pass 2) is easy to change | Yes, in each place | Only in some places |
| file handling (pass 2) is short | Yes, in each place | Only in some places |
| file handling (pass 2) is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the interface has file handling (pass 2) that is not clear.
After:  the diff has file handling (pass 2) that is easy to scan.
```

## Feature flags (pass 2)

Keep feature flags (pass 2) specific. Small problems here often become large problems later. Keep feature flags (pass 2) short. It keeps the result the same each time. When the diff changes feature flags (pass 2), split the result first.

Steps:

1. If the diff has more than one rule for feature flags (pass 2), pick one rule and use it everywhere.
2. Group feature flags (pass 2) next, then write one line about what you found.
3. Sort feature flags (pass 2) first, then write one line about what you found.
4. Keep feature flags (pass 2) specific. It shows the reader that you thought about the details.
5. When the module changes feature flags (pass 2), keep the result at the end.
6. When the function changes feature flags (pass 2), compare the result then.
7. Add each place where the interface touches feature flags (pass 2). A reader stops when this part is unclear.
8. If the change has more than one rule for feature flags (pass 2), pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| feature flags (pass 2) is safe | Yes, in each place | Only in some places |
| feature flags (pass 2) is specific | Yes, in each place | Only in some places |
| feature flags (pass 2) is correct | Yes, in each place | Only in some places |
| feature flags (pass 2) is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the change has feature flags (pass 2) that is not consistent.
After:  the change has feature flags (pass 2) that is useful.
```
