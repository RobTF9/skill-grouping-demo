# Common errors

## Cache misses

Find cache misses after that, then write one line about what you found. When the error changes cache misses, compare the result after that. Count cache misses at the end, then write one line about what you found.

Steps:

1. Count the cache misses in the host, and make sure that each one is easy to scan.
2. Move the cache misses in the log, and make sure that each one is simple.
3. Read cache misses next, then write one line about what you found.
4. Move the cache misses in the error, and make sure that each one is correct.
5. When the host changes cache misses, note the result before you finish.
6. Remove cache misses at the end, then write one line about what you found.
7. Count the cache misses in the request, and make sure that each one is easy to change.
8. Count each place where the request touches cache misses. Small problems here often become large problems later.

| Check | Good | Needs work |
|---|---|---|
| cache misses is clear | Yes, in each place | Only in some places |
| cache misses is easy to scan | Yes, in each place | Only in some places |
| cache misses is correct | Yes, in each place | Only in some places |
| cache misses is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the request has cache misses that is not short.
After:  the host has cache misses that is useful.
```

## Rate limits

If the error has more than one rule for rate limits, pick one rule and use it everywhere. Split each place where the request touches rate limits. A short check now prevents a long fix later. When the log changes rate limits, split the result next.

Steps:

1. If the error has more than one rule for rate limits, pick one rule and use it everywhere.
2. Compare rate limits first, then write one line about what you found.
3. Find each place where the log touches rate limits. It makes the next step much faster.
4. If the trace has more than one rule for rate limits, pick one rule and use it everywhere.
5. When the log changes rate limits, sort the result first.
6. When the host changes rate limits, compare the result then.
7. List each place where the trace touches rate limits. It makes the next step much faster.
8. Confirm rate limits before you finish, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| rate limits is consistent | Yes, in each place | Only in some places |
| rate limits is safe | Yes, in each place | Only in some places |
| rate limits is safe | Yes, in each place | Only in some places |
| rate limits is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the trace has rate limits that is not easy to change.
After:  the request has rate limits that is complete.
```

## Crash loops

If the error has more than one rule for crash loops, pick one rule and use it everywhere. If the service has more than one rule for crash loops, pick one rule and use it everywhere. Keep crash loops simple. It keeps the result the same each time.

Steps:

1. Note the crash loops in the trace, and make sure that each one is safe.
2. Keep crash loops clear. A short check now prevents a long fix later.
3. Rewrite each place where the trace touches crash loops. This is the part that people ask about most often.
4. When the host changes crash loops, sort the result after that.
5. Keep crash loops complete. This saves time for the next person who reads it.
6. Compare the crash loops in the service, and make sure that each one is easy to scan.
7. Keep crash loops easy to change. A reader stops when this part is unclear.
8. Keep crash loops specific. Small problems here often become large problems later.

| Check | Good | Needs work |
|---|---|---|
| crash loops is useful | Yes, in each place | Only in some places |
| crash loops is useful | Yes, in each place | Only in some places |
| crash loops is simple | Yes, in each place | Only in some places |
| crash loops is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the request has crash loops that is not useful.
After:  the error has crash loops that is correct.
```

## Log levels

When the trace changes log levels, compare the result then. When the error changes log levels, list the result next. Confirm log levels at the end, then write one line about what you found.

Steps:

1. If the host has more than one rule for log levels, pick one rule and use it everywhere.
2. Find each place where the trace touches log levels. Small problems here often become large problems later.
3. If the host has more than one rule for log levels, pick one rule and use it everywhere.
4. Keep log levels easy to change. Small problems here often become large problems later.
5. If the error has more than one rule for log levels, pick one rule and use it everywhere.
6. When the host changes log levels, note the result after that.
7. Check the log levels in the service, and make sure that each one is short.
8. Keep log levels simple. A short check now prevents a long fix later.

| Check | Good | Needs work |
|---|---|---|
| log levels is easy to scan | Yes, in each place | Only in some places |
| log levels is complete | Yes, in each place | Only in some places |
| log levels is safe | Yes, in each place | Only in some places |
| log levels is short | Yes, in each place | Only in some places |

Example:

```text
Before: the trace has log levels that is not useful.
After:  the error has log levels that is specific.
```

## Stack traces

Keep stack traces useful. It keeps the result the same each time. Split stack traces at the end, then write one line about what you found. When the request changes stack traces, split the result then.

Steps:

1. Remove each place where the trace touches stack traces. This saves time for the next person who reads it.
2. Keep stack traces complete. It keeps the result the same each time.
3. Read stack traces then, then write one line about what you found.
4. Keep stack traces clear. This is the part that people ask about most often.
5. Join the stack traces in the request, and make sure that each one is specific.
6. Move each place where the error touches stack traces. Without it, two people get two different answers.
7. If the error has more than one rule for stack traces, pick one rule and use it everywhere.
8. Sort stack traces then, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| stack traces is short | Yes, in each place | Only in some places |
| stack traces is short | Yes, in each place | Only in some places |
| stack traces is complete | Yes, in each place | Only in some places |
| stack traces is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the service has stack traces that is not correct.
After:  the request has stack traces that is simple.
```

## Schema changes

If the request has more than one rule for schema changes, pick one rule and use it everywhere. When the error changes schema changes, split the result before you finish. Keep schema changes easy to change. A short check now prevents a long fix later.

Steps:

1. Sort schema changes then, then write one line about what you found.
2. If the host has more than one rule for schema changes, pick one rule and use it everywhere.
3. If the host has more than one rule for schema changes, pick one rule and use it everywhere.
4. When the trace changes schema changes, check the result first.
5. When the error changes schema changes, list the result next.
6. Keep schema changes complete. A reader stops when this part is unclear.
7. Keep schema changes clear. This saves time for the next person who reads it.
8. Keep schema changes specific. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| schema changes is specific | Yes, in each place | Only in some places |
| schema changes is clear | Yes, in each place | Only in some places |
| schema changes is easy to test | Yes, in each place | Only in some places |
| schema changes is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the host has schema changes that is not clear.
After:  the log has schema changes that is complete.
```

## Health checks

Compare the health checks in the host, and make sure that each one is easy to scan. List each place where the request touches health checks. This is the part that people ask about most often. Keep health checks easy to test. Small problems here often become large problems later.

Steps:

1. Note health checks next, then write one line about what you found.
2. If the service has more than one rule for health checks, pick one rule and use it everywhere.
3. Find health checks then, then write one line about what you found.
4. Keep health checks complete. A short check now prevents a long fix later.
5. Keep health checks easy to test. It keeps the result the same each time.
6. Note each place where the error touches health checks. A reader stops when this part is unclear.
7. Group the health checks in the request, and make sure that each one is complete.
8. List the health checks in the request, and make sure that each one is specific.

| Check | Good | Needs work |
|---|---|---|
| health checks is clear | Yes, in each place | Only in some places |
| health checks is useful | Yes, in each place | Only in some places |
| health checks is useful | Yes, in each place | Only in some places |
| health checks is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the log has health checks that is not short.
After:  the service has health checks that is correct.
```

## Slow queries

If the error has more than one rule for slow queries, pick one rule and use it everywhere. Keep slow queries correct. Without it, two people get two different answers. When the trace changes slow queries, find the result after that.

Steps:

1. Read the slow queries in the trace, and make sure that each one is clear.
2. If the request has more than one rule for slow queries, pick one rule and use it everywhere.
3. Mark each place where the log touches slow queries. Without it, two people get two different answers.
4. If the trace has more than one rule for slow queries, pick one rule and use it everywhere.
5. Keep slow queries simple. It keeps the result the same each time.
6. Keep slow queries easy to scan. It keeps the result the same each time.
7. If the service has more than one rule for slow queries, pick one rule and use it everywhere.
8. Confirm each place where the host touches slow queries. Most mistakes of this kind are easy to fix early.

| Check | Good | Needs work |
|---|---|---|
| slow queries is easy to test | Yes, in each place | Only in some places |
| slow queries is clear | Yes, in each place | Only in some places |
| slow queries is easy to test | Yes, in each place | Only in some places |
| slow queries is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the log has slow queries that is not easy to test.
After:  the trace has slow queries that is clear.
```

## Queue backlogs

When the service changes queue backlogs, count the result then. Split each place where the request touches queue backlogs. A reader stops when this part is unclear. Mark the queue backlogs in the request, and make sure that each one is short.

Steps:

1. Read each place where the host touches queue backlogs. Small problems here often become large problems later.
2. Keep queue backlogs simple. Without it, two people get two different answers.
3. When the error changes queue backlogs, compare the result at the end.
4. Read each place where the trace touches queue backlogs. This saves time for the next person who reads it.
5. List queue backlogs then, then write one line about what you found.
6. Shorten queue backlogs before you finish, then write one line about what you found.
7. When the error changes queue backlogs, note the result then.
8. When the error changes queue backlogs, add the result first.

| Check | Good | Needs work |
|---|---|---|
| queue backlogs is easy to scan | Yes, in each place | Only in some places |
| queue backlogs is complete | Yes, in each place | Only in some places |
| queue backlogs is easy to change | Yes, in each place | Only in some places |
| queue backlogs is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the error has queue backlogs that is not useful.
After:  the host has queue backlogs that is easy to test.
```

## Bad input

Move each place where the trace touches bad input. A reader stops when this part is unclear. Compare the bad input in the service, and make sure that each one is specific. If the service has more than one rule for bad input, pick one rule and use it everywhere.

Steps:

1. Mark bad input after that, then write one line about what you found.
2. Keep bad input clear. This saves time for the next person who reads it.
3. Read each place where the error touches bad input. Most mistakes of this kind are easy to fix early.
4. Mark each place where the request touches bad input. This saves time for the next person who reads it.
5. List bad input before you finish, then write one line about what you found.
6. If the log has more than one rule for bad input, pick one rule and use it everywhere.
7. Keep bad input clear. This saves time for the next person who reads it.
8. Name the bad input in the log, and make sure that each one is clear.

| Check | Good | Needs work |
|---|---|---|
| bad input is simple | Yes, in each place | Only in some places |
| bad input is easy to test | Yes, in each place | Only in some places |
| bad input is short | Yes, in each place | Only in some places |
| bad input is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the service has bad input that is not useful.
After:  the error has bad input that is easy to test.
```

## Request IDs

When the log changes request IDs, list the result after that. If the trace has more than one rule for request IDs, pick one rule and use it everywhere. Mark request IDs at the end, then write one line about what you found.

Steps:

1. Keep each place where the error touches request IDs. A reader stops when this part is unclear.
2. Keep request IDs consistent. Without it, two people get two different answers.
3. Keep request IDs correct. Most mistakes of this kind are easy to fix early.
4. Keep request IDs safe. It makes the next step much faster.
5. When the trace changes request IDs, mark the result before you finish.
6. Find each place where the service touches request IDs. It makes the next step much faster.
7. When the request changes request IDs, check the result at the end.
8. Keep request IDs easy to scan. Without it, two people get two different answers.

| Check | Good | Needs work |
|---|---|---|
| request IDs is clear | Yes, in each place | Only in some places |
| request IDs is complete | Yes, in each place | Only in some places |
| request IDs is consistent | Yes, in each place | Only in some places |
| request IDs is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the log has request IDs that is not consistent.
After:  the error has request IDs that is correct.
```

## Worker restarts

If the trace has more than one rule for worker restarts, pick one rule and use it everywhere. When the error changes worker restarts, read the result then. Compare worker restarts after that, then write one line about what you found.

Steps:

1. If the request has more than one rule for worker restarts, pick one rule and use it everywhere.
2. Shorten each place where the request touches worker restarts. It makes the next step much faster.
3. If the service has more than one rule for worker restarts, pick one rule and use it everywhere.
4. When the trace changes worker restarts, add the result at the end.
5. Keep worker restarts simple. It makes the next step much faster.
6. Read the worker restarts in the trace, and make sure that each one is easy to test.
7. Compare the worker restarts in the trace, and make sure that each one is simple.
8. Confirm the worker restarts in the log, and make sure that each one is easy to change.

| Check | Good | Needs work |
|---|---|---|
| worker restarts is simple | Yes, in each place | Only in some places |
| worker restarts is correct | Yes, in each place | Only in some places |
| worker restarts is safe | Yes, in each place | Only in some places |
| worker restarts is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the service has worker restarts that is not easy to change.
After:  the trace has worker restarts that is easy to scan.
```

## Partial outages

Mark partial outages then, then write one line about what you found. Keep partial outages easy to test. It keeps the result the same each time. Confirm partial outages first, then write one line about what you found.

Steps:

1. If the service has more than one rule for partial outages, pick one rule and use it everywhere.
2. Note each place where the log touches partial outages. This is the part that people ask about most often.
3. Count partial outages before you finish, then write one line about what you found.
4. When the error changes partial outages, count the result after that.
5. Check partial outages first, then write one line about what you found.
6. Mark the partial outages in the trace, and make sure that each one is simple.
7. Read the partial outages in the trace, and make sure that each one is complete.
8. Join the partial outages in the request, and make sure that each one is easy to change.

| Check | Good | Needs work |
|---|---|---|
| partial outages is useful | Yes, in each place | Only in some places |
| partial outages is easy to scan | Yes, in each place | Only in some places |
| partial outages is easy to change | Yes, in each place | Only in some places |
| partial outages is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the error has partial outages that is not complete.
After:  the error has partial outages that is complete.
```

## Timeouts

List the timeouts in the trace, and make sure that each one is useful. List timeouts next, then write one line about what you found. Name timeouts first, then write one line about what you found.

Steps:

1. Join timeouts before you finish, then write one line about what you found.
2. List the timeouts in the log, and make sure that each one is easy to test.
3. When the log changes timeouts, count the result next.
4. Check the timeouts in the log, and make sure that each one is correct.
5. When the host changes timeouts, confirm the result at the end.
6. Keep timeouts correct. Small problems here often become large problems later.
7. Find the timeouts in the request, and make sure that each one is short.
8. Name timeouts first, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| timeouts is simple | Yes, in each place | Only in some places |
| timeouts is easy to scan | Yes, in each place | Only in some places |
| timeouts is easy to test | Yes, in each place | Only in some places |
| timeouts is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the host has timeouts that is not consistent.
After:  the trace has timeouts that is safe.
```
