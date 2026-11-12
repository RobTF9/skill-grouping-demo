---
name: debug-logs
description: Find the cause of an error in a set of logs.
---

# Debug logs

Find the first error in the logs. Read the lines before it. Name the most likely cause.

## Time stamps

Keep time stamps simple. It shows the reader that you thought about the details. When the trace changes time stamps, move the result before you finish. If the log has more than one rule for time stamps, pick one rule and use it everywhere.

Steps:

1. If the error has more than one rule for time stamps, pick one rule and use it everywhere.
2. Confirm each place where the trace touches time stamps. It shows the reader that you thought about the details.
3. If the log has more than one rule for time stamps, pick one rule and use it everywhere.
4. If the host has more than one rule for time stamps, pick one rule and use it everywhere.
5. Find each place where the error touches time stamps. It makes the next step much faster.
6. Mark the time stamps in the host, and make sure that each one is short.
7. Keep time stamps easy to change. Most mistakes of this kind are easy to fix early.
8. Count each place where the log touches time stamps. This saves time for the next person who reads it.

| Check | Good | Needs work |
|---|---|---|
| time stamps is easy to scan | Yes, in each place | Only in some places |
| time stamps is short | Yes, in each place | Only in some places |
| time stamps is clear | Yes, in each place | Only in some places |
| time stamps is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the error has time stamps that is not consistent.
After:  the host has time stamps that is safe.
```

## Clock drift

Keep clock drift safe. A short check now prevents a long fix later. When the host changes clock drift, rewrite the result first. If the host has more than one rule for clock drift, pick one rule and use it everywhere.

Steps:

1. When the log changes clock drift, count the result after that.
2. When the request changes clock drift, remove the result then.
3. Keep clock drift easy to change. Small problems here often become large problems later.
4. Keep clock drift safe. A short check now prevents a long fix later.
5. Keep clock drift easy to test. Small problems here often become large problems later.
6. Group each place where the error touches clock drift. Most mistakes of this kind are easy to fix early.
7. Read the clock drift in the trace, and make sure that each one is correct.
8. List each place where the host touches clock drift. Without it, two people get two different answers.

| Check | Good | Needs work |
|---|---|---|
| clock drift is short | Yes, in each place | Only in some places |
| clock drift is short | Yes, in each place | Only in some places |
| clock drift is specific | Yes, in each place | Only in some places |
| clock drift is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the host has clock drift that is not complete.
After:  the request has clock drift that is easy to test.
```

## Timeouts

List each place where the service touches timeouts. A short check now prevents a long fix later. Keep timeouts clear. Most mistakes of this kind are easy to fix early. Name each place where the host touches timeouts. A reader stops when this part is unclear.

Steps:

1. When the request changes timeouts, check the result at the end.
2. Note timeouts then, then write one line about what you found.
3. Mark the timeouts in the trace, and make sure that each one is easy to scan.
4. If the host has more than one rule for timeouts, pick one rule and use it everywhere.
5. Read timeouts after that, then write one line about what you found.
6. Keep timeouts useful. It shows the reader that you thought about the details.
7. Keep timeouts useful. It keeps the result the same each time.
8. If the request has more than one rule for timeouts, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| timeouts is complete | Yes, in each place | Only in some places |
| timeouts is easy to change | Yes, in each place | Only in some places |
| timeouts is easy to change | Yes, in each place | Only in some places |
| timeouts is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the request has timeouts that is not clear.
After:  the host has timeouts that is simple.
```

## Log levels

If the request has more than one rule for log levels, pick one rule and use it everywhere. Keep log levels easy to test. It shows the reader that you thought about the details. When the trace changes log levels, check the result after that.

Steps:

1. Mark the log levels in the trace, and make sure that each one is consistent.
2. Keep log levels easy to change. A short check now prevents a long fix later.
3. Keep the log levels in the log, and make sure that each one is short.
4. Keep log levels clear. It keeps the result the same each time.
5. Split each place where the error touches log levels. It shows the reader that you thought about the details.
6. If the request has more than one rule for log levels, pick one rule and use it everywhere.
7. Check each place where the request touches log levels. Without it, two people get two different answers.
8. When the host changes log levels, note the result next.

| Check | Good | Needs work |
|---|---|---|
| log levels is easy to change | Yes, in each place | Only in some places |
| log levels is short | Yes, in each place | Only in some places |
| log levels is simple | Yes, in each place | Only in some places |
| log levels is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the service has log levels that is not short.
After:  the error has log levels that is easy to test.
```

## Worker restarts

If the service has more than one rule for worker restarts, pick one rule and use it everywhere. Split worker restarts next, then write one line about what you found. Find the worker restarts in the request, and make sure that each one is correct.

Steps:

1. Keep worker restarts easy to test. A short check now prevents a long fix later.
2. Keep worker restarts consistent. Most mistakes of this kind are easy to fix early.
3. Group each place where the log touches worker restarts. It makes the next step much faster.
4. Note the worker restarts in the request, and make sure that each one is useful.
5. When the trace changes worker restarts, name the result first.
6. Keep worker restarts easy to test. This saves time for the next person who reads it.
7. Keep worker restarts easy to scan. A reader stops when this part is unclear.
8. Keep worker restarts useful. Small problems here often become large problems later.

| Check | Good | Needs work |
|---|---|---|
| worker restarts is consistent | Yes, in each place | Only in some places |
| worker restarts is easy to scan | Yes, in each place | Only in some places |
| worker restarts is easy to change | Yes, in each place | Only in some places |
| worker restarts is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the error has worker restarts that is not simple.
After:  the log has worker restarts that is specific.
```

## Partial outages

Split partial outages before you finish, then write one line about what you found. Keep partial outages easy to change. It makes the next step much faster. Mark partial outages first, then write one line about what you found.

Steps:

1. If the trace has more than one rule for partial outages, pick one rule and use it everywhere.
2. If the host has more than one rule for partial outages, pick one rule and use it everywhere.
3. When the request changes partial outages, note the result after that.
4. When the host changes partial outages, confirm the result after that.
5. If the service has more than one rule for partial outages, pick one rule and use it everywhere.
6. Count the partial outages in the log, and make sure that each one is easy to change.
7. Name each place where the service touches partial outages. It shows the reader that you thought about the details.
8. Mark partial outages after that, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| partial outages is clear | Yes, in each place | Only in some places |
| partial outages is simple | Yes, in each place | Only in some places |
| partial outages is simple | Yes, in each place | Only in some places |
| partial outages is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the service has partial outages that is not correct.
After:  the trace has partial outages that is safe.
```

## Schema changes

Check each place where the error touches schema changes. A reader stops when this part is unclear. Split schema changes after that, then write one line about what you found. Read schema changes then, then write one line about what you found.

Steps:

1. Keep schema changes at the end, then write one line about what you found.
2. Keep schema changes easy to change. Without it, two people get two different answers.
3. Keep schema changes specific. This saves time for the next person who reads it.
4. Check the schema changes in the request, and make sure that each one is useful.
5. If the log has more than one rule for schema changes, pick one rule and use it everywhere.
6. When the service changes schema changes, list the result then.
7. Remove schema changes after that, then write one line about what you found.
8. When the log changes schema changes, remove the result after that.

| Check | Good | Needs work |
|---|---|---|
| schema changes is specific | Yes, in each place | Only in some places |
| schema changes is short | Yes, in each place | Only in some places |
| schema changes is easy to scan | Yes, in each place | Only in some places |
| schema changes is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the service has schema changes that is not easy to change.
After:  the host has schema changes that is easy to test.
```

## Memory warnings

Keep memory warnings clear. It keeps the result the same each time. Check memory warnings first, then write one line about what you found. If the request has more than one rule for memory warnings, pick one rule and use it everywhere.

Steps:

1. If the trace has more than one rule for memory warnings, pick one rule and use it everywhere.
2. Keep memory warnings short. It makes the next step much faster.
3. Keep the memory warnings in the trace, and make sure that each one is safe.
4. Add each place where the service touches memory warnings. A short check now prevents a long fix later.
5. Add the memory warnings in the request, and make sure that each one is simple.
6. Keep the memory warnings in the error, and make sure that each one is short.
7. Confirm memory warnings next, then write one line about what you found.
8. Mark the memory warnings in the request, and make sure that each one is specific.

| Check | Good | Needs work |
|---|---|---|
| memory warnings is simple | Yes, in each place | Only in some places |
| memory warnings is easy to change | Yes, in each place | Only in some places |
| memory warnings is consistent | Yes, in each place | Only in some places |
| memory warnings is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the error has memory warnings that is not specific.
After:  the host has memory warnings that is easy to test.
```

## Crash loops

Name crash loops then, then write one line about what you found. Keep crash loops specific. Without it, two people get two different answers. When the trace changes crash loops, list the result then.

Steps:

1. Shorten crash loops after that, then write one line about what you found.
2. Keep crash loops simple. Small problems here often become large problems later.
3. Find the crash loops in the error, and make sure that each one is clear.
4. If the trace has more than one rule for crash loops, pick one rule and use it everywhere.
5. If the host has more than one rule for crash loops, pick one rule and use it everywhere.
6. When the trace changes crash loops, shorten the result after that.
7. When the host changes crash loops, move the result next.
8. Keep crash loops complete. A short check now prevents a long fix later.

| Check | Good | Needs work |
|---|---|---|
| crash loops is short | Yes, in each place | Only in some places |
| crash loops is specific | Yes, in each place | Only in some places |
| crash loops is simple | Yes, in each place | Only in some places |
| crash loops is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the service has crash loops that is not useful.
After:  the log has crash loops that is complete.
```

## TLS errors

Keep TLS errors short. It shows the reader that you thought about the details. Keep TLS errors complete. A reader stops when this part is unclear. Shorten the TLS errors in the error, and make sure that each one is easy to test.

Steps:

1. If the service has more than one rule for TLS errors, pick one rule and use it everywhere.
2. Check TLS errors then, then write one line about what you found.
3. Remove the TLS errors in the request, and make sure that each one is short.
4. Add each place where the request touches TLS errors. Without it, two people get two different answers.
5. When the host changes TLS errors, remove the result at the end.
6. If the trace has more than one rule for TLS errors, pick one rule and use it everywhere.
7. Remove the TLS errors in the error, and make sure that each one is clear.
8. Count TLS errors before you finish, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| TLS errors is short | Yes, in each place | Only in some places |
| TLS errors is consistent | Yes, in each place | Only in some places |
| TLS errors is easy to change | Yes, in each place | Only in some places |
| TLS errors is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the service has TLS errors that is not correct.
After:  the host has TLS errors that is safe.
```

## Request IDs

Compare request IDs after that, then write one line about what you found. If the trace has more than one rule for request IDs, pick one rule and use it everywhere. Keep request IDs clear. This saves time for the next person who reads it.

Steps:

1. Keep request IDs easy to scan. It shows the reader that you thought about the details.
2. If the request has more than one rule for request IDs, pick one rule and use it everywhere.
3. Note the request IDs in the request, and make sure that each one is complete.
4. When the host changes request IDs, move the result at the end.
5. Keep request IDs then, then write one line about what you found.
6. Keep request IDs clear. It shows the reader that you thought about the details.
7. Keep each place where the log touches request IDs. Without it, two people get two different answers.
8. If the request has more than one rule for request IDs, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| request IDs is useful | Yes, in each place | Only in some places |
| request IDs is specific | Yes, in each place | Only in some places |
| request IDs is specific | Yes, in each place | Only in some places |
| request IDs is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the service has request IDs that is not easy to change.
After:  the log has request IDs that is consistent.
```

## Disk space

Shorten each place where the request touches disk space. Small problems here often become large problems later. Group disk space after that, then write one line about what you found. Keep disk space easy to scan. It makes the next step much faster.

Steps:

1. Add disk space first, then write one line about what you found.
2. Count the disk space in the service, and make sure that each one is easy to change.
3. When the host changes disk space, confirm the result before you finish.
4. If the error has more than one rule for disk space, pick one rule and use it everywhere.
5. Keep disk space short. This saves time for the next person who reads it.
6. Remove disk space first, then write one line about what you found.
7. When the service changes disk space, group the result then.
8. Shorten the disk space in the log, and make sure that each one is consistent.

| Check | Good | Needs work |
|---|---|---|
| disk space is simple | Yes, in each place | Only in some places |
| disk space is consistent | Yes, in each place | Only in some places |
| disk space is specific | Yes, in each place | Only in some places |
| disk space is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the request has disk space that is not simple.
After:  the log has disk space that is easy to change.
```

## Bad input

Group each place where the service touches bad input. It shows the reader that you thought about the details. Read bad input first, then write one line about what you found. Keep bad input useful. Without it, two people get two different answers.

Steps:

1. If the error has more than one rule for bad input, pick one rule and use it everywhere.
2. When the error changes bad input, name the result after that.
3. Name the bad input in the service, and make sure that each one is short.
4. Name the bad input in the host, and make sure that each one is easy to change.
5. Note the bad input in the log, and make sure that each one is correct.
6. When the host changes bad input, note the result then.
7. Join the bad input in the trace, and make sure that each one is specific.
8. Remove bad input next, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| bad input is simple | Yes, in each place | Only in some places |
| bad input is specific | Yes, in each place | Only in some places |
| bad input is easy to test | Yes, in each place | Only in some places |
| bad input is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the service has bad input that is not short.
After:  the request has bad input that is specific.
```

## Rate limits

If the host has more than one rule for rate limits, pick one rule and use it everywhere. When the service changes rate limits, name the result next. When the trace changes rate limits, move the result at the end.

Steps:

1. Compare the rate limits in the host, and make sure that each one is safe.
2. Count the rate limits in the host, and make sure that each one is useful.
3. Split rate limits then, then write one line about what you found.
4. Name rate limits next, then write one line about what you found.
5. List each place where the host touches rate limits. Small problems here often become large problems later.
6. Keep rate limits clear. This is the part that people ask about most often.
7. Confirm each place where the trace touches rate limits. Small problems here often become large problems later.
8. When the request changes rate limits, check the result first.

| Check | Good | Needs work |
|---|---|---|
| rate limits is complete | Yes, in each place | Only in some places |
| rate limits is complete | Yes, in each place | Only in some places |
| rate limits is easy to scan | Yes, in each place | Only in some places |
| rate limits is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the error has rate limits that is not easy to change.
After:  the request has rate limits that is useful.
```

## Queue backlogs

Read queue backlogs before you finish, then write one line about what you found. Keep queue backlogs simple. A short check now prevents a long fix later. Note each place where the request touches queue backlogs. Small problems here often become large problems later.

Steps:

1. When the request changes queue backlogs, count the result before you finish.
2. Mark the queue backlogs in the trace, and make sure that each one is clear.
3. Keep queue backlogs consistent. It keeps the result the same each time.
4. Confirm each place where the log touches queue backlogs. A reader stops when this part is unclear.
5. Compare the queue backlogs in the host, and make sure that each one is correct.
6. Shorten the queue backlogs in the host, and make sure that each one is short.
7. When the trace changes queue backlogs, move the result then.
8. Remove queue backlogs at the end, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| queue backlogs is correct | Yes, in each place | Only in some places |
| queue backlogs is useful | Yes, in each place | Only in some places |
| queue backlogs is easy to scan | Yes, in each place | Only in some places |
| queue backlogs is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the host has queue backlogs that is not consistent.
After:  the host has queue backlogs that is simple.
```

## Connection pools

If the log has more than one rule for connection pools, pick one rule and use it everywhere. When the log changes connection pools, remove the result then. Compare each place where the service touches connection pools. It keeps the result the same each time.

Steps:

1. Join each place where the log touches connection pools. This saves time for the next person who reads it.
2. Join connection pools then, then write one line about what you found.
3. Note the connection pools in the trace, and make sure that each one is easy to test.
4. Keep the connection pools in the log, and make sure that each one is clear.
5. Move connection pools first, then write one line about what you found.
6. Remove connection pools first, then write one line about what you found.
7. Keep connection pools simple. A short check now prevents a long fix later.
8. When the log changes connection pools, join the result after that.

| Check | Good | Needs work |
|---|---|---|
| connection pools is simple | Yes, in each place | Only in some places |
| connection pools is short | Yes, in each place | Only in some places |
| connection pools is complete | Yes, in each place | Only in some places |
| connection pools is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the service has connection pools that is not easy to test.
After:  the log has connection pools that is correct.
```

## Cache misses

If the error has more than one rule for cache misses, pick one rule and use it everywhere. Confirm cache misses before you finish, then write one line about what you found. If the trace has more than one rule for cache misses, pick one rule and use it everywhere.

Steps:

1. Note the cache misses in the request, and make sure that each one is simple.
2. Split the cache misses in the trace, and make sure that each one is easy to test.
3. If the trace has more than one rule for cache misses, pick one rule and use it everywhere.
4. Rewrite each place where the error touches cache misses. It shows the reader that you thought about the details.
5. When the service changes cache misses, list the result at the end.
6. Check the cache misses in the service, and make sure that each one is complete.
7. List the cache misses in the trace, and make sure that each one is useful.
8. If the trace has more than one rule for cache misses, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| cache misses is short | Yes, in each place | Only in some places |
| cache misses is easy to scan | Yes, in each place | Only in some places |
| cache misses is short | Yes, in each place | Only in some places |
| cache misses is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the host has cache misses that is not easy to scan.
After:  the host has cache misses that is easy to change.
```

## DNS errors

Join DNS errors at the end, then write one line about what you found. Rewrite DNS errors before you finish, then write one line about what you found. Keep DNS errors easy to test. A short check now prevents a long fix later.

Steps:

1. Keep DNS errors specific. It keeps the result the same each time.
2. Sort each place where the host touches DNS errors. It shows the reader that you thought about the details.
3. When the host changes DNS errors, mark the result before you finish.
4. When the host changes DNS errors, mark the result then.
5. When the request changes DNS errors, find the result first.
6. Name the DNS errors in the service, and make sure that each one is correct.
7. If the host has more than one rule for DNS errors, pick one rule and use it everywhere.
8. When the service changes DNS errors, add the result first.

| Check | Good | Needs work |
|---|---|---|
| DNS errors is easy to change | Yes, in each place | Only in some places |
| DNS errors is clear | Yes, in each place | Only in some places |
| DNS errors is safe | Yes, in each place | Only in some places |
| DNS errors is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the log has DNS errors that is not short.
After:  the trace has DNS errors that is correct.
```

## Stack traces

Group stack traces at the end, then write one line about what you found. When the request changes stack traces, join the result at the end. When the host changes stack traces, sort the result after that.

Steps:

1. Keep stack traces easy to scan. It makes the next step much faster.
2. Keep each place where the request touches stack traces. Without it, two people get two different answers.
3. Confirm each place where the log touches stack traces. It makes the next step much faster.
4. Keep stack traces useful. A reader stops when this part is unclear.
5. Split each place where the error touches stack traces. This saves time for the next person who reads it.
6. Count the stack traces in the host, and make sure that each one is specific.
7. When the error changes stack traces, compare the result first.
8. When the request changes stack traces, shorten the result after that.

| Check | Good | Needs work |
|---|---|---|
| stack traces is short | Yes, in each place | Only in some places |
| stack traces is easy to scan | Yes, in each place | Only in some places |
| stack traces is clear | Yes, in each place | Only in some places |
| stack traces is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the error has stack traces that is not easy to change.
After:  the trace has stack traces that is complete.
```

## Retries

If the trace has more than one rule for retries, pick one rule and use it everywhere. Keep retries useful. A reader stops when this part is unclear. If the host has more than one rule for retries, pick one rule and use it everywhere.

Steps:

1. Compare the retries in the host, and make sure that each one is clear.
2. If the error has more than one rule for retries, pick one rule and use it everywhere.
3. When the trace changes retries, split the result then.
4. Shorten retries then, then write one line about what you found.
5. If the host has more than one rule for retries, pick one rule and use it everywhere.
6. Keep retries easy to change. It makes the next step much faster.
7. If the trace has more than one rule for retries, pick one rule and use it everywhere.
8. Confirm the retries in the log, and make sure that each one is safe.

| Check | Good | Needs work |
|---|---|---|
| retries is short | Yes, in each place | Only in some places |
| retries is short | Yes, in each place | Only in some places |
| retries is consistent | Yes, in each place | Only in some places |
| retries is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the trace has retries that is not easy to change.
After:  the trace has retries that is safe.
```

## Cron jobs

When the error changes cron jobs, split the result first. When the error changes cron jobs, list the result next. Rewrite cron jobs before you finish, then write one line about what you found.

Steps:

1. When the service changes cron jobs, confirm the result after that.
2. Check cron jobs next, then write one line about what you found.
3. Shorten the cron jobs in the log, and make sure that each one is easy to scan.
4. Check each place where the log touches cron jobs. This is the part that people ask about most often.
5. Group the cron jobs in the log, and make sure that each one is complete.
6. Count the cron jobs in the trace, and make sure that each one is correct.
7. Group each place where the request touches cron jobs. Without it, two people get two different answers.
8. Join cron jobs then, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| cron jobs is consistent | Yes, in each place | Only in some places |
| cron jobs is specific | Yes, in each place | Only in some places |
| cron jobs is specific | Yes, in each place | Only in some places |
| cron jobs is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the service has cron jobs that is not useful.
After:  the log has cron jobs that is useful.
```

## Lock waits

If the request has more than one rule for lock waits, pick one rule and use it everywhere. Split lock waits at the end, then write one line about what you found. If the service has more than one rule for lock waits, pick one rule and use it everywhere.

Steps:

1. When the host changes lock waits, move the result first.
2. Name each place where the request touches lock waits. It makes the next step much faster.
3. Join lock waits next, then write one line about what you found.
4. Move lock waits before you finish, then write one line about what you found.
5. Keep lock waits simple. It shows the reader that you thought about the details.
6. Move each place where the trace touches lock waits. It keeps the result the same each time.
7. If the trace has more than one rule for lock waits, pick one rule and use it everywhere.
8. Rewrite the lock waits in the host, and make sure that each one is consistent.

| Check | Good | Needs work |
|---|---|---|
| lock waits is easy to scan | Yes, in each place | Only in some places |
| lock waits is clear | Yes, in each place | Only in some places |
| lock waits is short | Yes, in each place | Only in some places |
| lock waits is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the host has lock waits that is not short.
After:  the host has lock waits that is easy to scan.
```

## Slow queries

When the host changes slow queries, compare the result next. Sort each place where the request touches slow queries. It shows the reader that you thought about the details. Keep slow queries clear. Small problems here often become large problems later.

Steps:

1. If the host has more than one rule for slow queries, pick one rule and use it everywhere.
2. Compare the slow queries in the service, and make sure that each one is easy to test.
3. Rewrite each place where the host touches slow queries. It shows the reader that you thought about the details.
4. Keep slow queries consistent. It keeps the result the same each time.
5. If the request has more than one rule for slow queries, pick one rule and use it everywhere.
6. Move slow queries before you finish, then write one line about what you found.
7. Keep slow queries consistent. A short check now prevents a long fix later.
8. When the log changes slow queries, name the result then.

| Check | Good | Needs work |
|---|---|---|
| slow queries is specific | Yes, in each place | Only in some places |
| slow queries is useful | Yes, in each place | Only in some places |
| slow queries is correct | Yes, in each place | Only in some places |
| slow queries is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the service has slow queries that is not simple.
After:  the host has slow queries that is useful.
```

## Health checks

If the log has more than one rule for health checks, pick one rule and use it everywhere. Keep health checks simple. A short check now prevents a long fix later. Compare each place where the trace touches health checks. It makes the next step much faster.

Steps:

1. Count health checks first, then write one line about what you found.
2. Keep health checks short. It keeps the result the same each time.
3. Mark the health checks in the host, and make sure that each one is safe.
4. Rewrite health checks before you finish, then write one line about what you found.
5. If the trace has more than one rule for health checks, pick one rule and use it everywhere.
6. List the health checks in the error, and make sure that each one is clear.
7. Shorten each place where the trace touches health checks. Without it, two people get two different answers.
8. If the error has more than one rule for health checks, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| health checks is easy to change | Yes, in each place | Only in some places |
| health checks is easy to scan | Yes, in each place | Only in some places |
| health checks is easy to test | Yes, in each place | Only in some places |
| health checks is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the request has health checks that is not specific.
After:  the host has health checks that is easy to scan.
```
