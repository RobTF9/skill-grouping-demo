# Log levels

## Timeouts

If the host has more than one rule for timeouts, pick one rule and use it everywhere. If the log has more than one rule for timeouts, pick one rule and use it everywhere. Keep each place where the log touches timeouts. Without it, two people get two different answers.

Steps:

1. When the host changes timeouts, join the result after that.
2. Confirm each place where the error touches timeouts. Without it, two people get two different answers.
3. If the service has more than one rule for timeouts, pick one rule and use it everywhere.
4. When the log changes timeouts, compare the result then.
5. Find timeouts after that, then write one line about what you found.
6. Keep timeouts short. Small problems here often become large problems later.
7. When the host changes timeouts, keep the result after that.
8. Rewrite each place where the error touches timeouts. It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| timeouts is easy to test | Yes, in each place | Only in some places |
| timeouts is easy to test | Yes, in each place | Only in some places |
| timeouts is easy to test | Yes, in each place | Only in some places |
| timeouts is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the host has timeouts that is not easy to scan.
After:  the service has timeouts that is clear.
```

## Partial outages

Group each place where the service touches partial outages. This is the part that people ask about most often. Join the partial outages in the log, and make sure that each one is easy to scan. If the host has more than one rule for partial outages, pick one rule and use it everywhere.

Steps:

1. Add each place where the host touches partial outages. This saves time for the next person who reads it.
2. Move each place where the error touches partial outages. Small problems here often become large problems later.
3. When the host changes partial outages, compare the result after that.
4. Confirm partial outages before you finish, then write one line about what you found.
5. When the host changes partial outages, confirm the result after that.
6. Rewrite partial outages next, then write one line about what you found.
7. Keep partial outages specific. It shows the reader that you thought about the details.
8. If the error has more than one rule for partial outages, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| partial outages is useful | Yes, in each place | Only in some places |
| partial outages is consistent | Yes, in each place | Only in some places |
| partial outages is short | Yes, in each place | Only in some places |
| partial outages is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the service has partial outages that is not easy to scan.
After:  the request has partial outages that is short.
```

## Lock waits

Split lock waits after that, then write one line about what you found. Keep lock waits easy to test. Small problems here often become large problems later. If the service has more than one rule for lock waits, pick one rule and use it everywhere.

Steps:

1. If the host has more than one rule for lock waits, pick one rule and use it everywhere.
2. Confirm the lock waits in the host, and make sure that each one is consistent.
3. Shorten each place where the error touches lock waits. It makes the next step much faster.
4. Group each place where the request touches lock waits. This is the part that people ask about most often.
5. Keep lock waits consistent. This saves time for the next person who reads it.
6. Keep lock waits easy to scan. It makes the next step much faster.
7. Find each place where the error touches lock waits. This is the part that people ask about most often.
8. If the host has more than one rule for lock waits, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| lock waits is simple | Yes, in each place | Only in some places |
| lock waits is easy to test | Yes, in each place | Only in some places |
| lock waits is correct | Yes, in each place | Only in some places |
| lock waits is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the trace has lock waits that is not easy to scan.
After:  the request has lock waits that is easy to test.
```

## Connection pools

Keep connection pools consistent. This saves time for the next person who reads it. Sort the connection pools in the service, and make sure that each one is useful. Compare each place where the host touches connection pools. A short check now prevents a long fix later.

Steps:

1. Group each place where the request touches connection pools. This saves time for the next person who reads it.
2. Name each place where the host touches connection pools. A short check now prevents a long fix later.
3. Count each place where the host touches connection pools. Without it, two people get two different answers.
4. If the service has more than one rule for connection pools, pick one rule and use it everywhere.
5. Move each place where the service touches connection pools. It shows the reader that you thought about the details.
6. When the request changes connection pools, remove the result at the end.
7. Keep connection pools short. It keeps the result the same each time.
8. Note connection pools next, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| connection pools is short | Yes, in each place | Only in some places |
| connection pools is easy to test | Yes, in each place | Only in some places |
| connection pools is safe | Yes, in each place | Only in some places |
| connection pools is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the host has connection pools that is not specific.
After:  the log has connection pools that is easy to change.
```

## Request IDs

If the service has more than one rule for request IDs, pick one rule and use it everywhere. Note the request IDs in the host, and make sure that each one is easy to scan. When the host changes request IDs, keep the result after that.

Steps:

1. Confirm request IDs next, then write one line about what you found.
2. Remove each place where the error touches request IDs. Without it, two people get two different answers.
3. Note the request IDs in the request, and make sure that each one is complete.
4. Note each place where the service touches request IDs. It makes the next step much faster.
5. Sort request IDs next, then write one line about what you found.
6. When the service changes request IDs, confirm the result next.
7. When the trace changes request IDs, list the result first.
8. Keep request IDs short. Small problems here often become large problems later.

| Check | Good | Needs work |
|---|---|---|
| request IDs is simple | Yes, in each place | Only in some places |
| request IDs is simple | Yes, in each place | Only in some places |
| request IDs is safe | Yes, in each place | Only in some places |
| request IDs is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the error has request IDs that is not easy to test.
After:  the log has request IDs that is easy to change.
```

## Health checks

Join each place where the trace touches health checks. It shows the reader that you thought about the details. Move each place where the trace touches health checks. It shows the reader that you thought about the details. Move health checks after that, then write one line about what you found.

Steps:

1. If the log has more than one rule for health checks, pick one rule and use it everywhere.
2. Name the health checks in the trace, and make sure that each one is easy to change.
3. When the host changes health checks, name the result then.
4. When the trace changes health checks, remove the result before you finish.
5. Join health checks at the end, then write one line about what you found.
6. Check the health checks in the request, and make sure that each one is easy to change.
7. When the error changes health checks, rewrite the result first.
8. If the log has more than one rule for health checks, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| health checks is clear | Yes, in each place | Only in some places |
| health checks is useful | Yes, in each place | Only in some places |
| health checks is simple | Yes, in each place | Only in some places |
| health checks is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the trace has health checks that is not clear.
After:  the request has health checks that is correct.
```

## Clock drift

Count each place where the trace touches clock drift. A short check now prevents a long fix later. Compare clock drift then, then write one line about what you found. Rewrite each place where the service touches clock drift. A short check now prevents a long fix later.

Steps:

1. Keep clock drift easy to test. This saves time for the next person who reads it.
2. When the service changes clock drift, read the result before you finish.
3. Join the clock drift in the trace, and make sure that each one is short.
4. Confirm clock drift then, then write one line about what you found.
5. When the host changes clock drift, split the result after that.
6. If the trace has more than one rule for clock drift, pick one rule and use it everywhere.
7. Note the clock drift in the log, and make sure that each one is short.
8. Keep clock drift simple. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| clock drift is clear | Yes, in each place | Only in some places |
| clock drift is clear | Yes, in each place | Only in some places |
| clock drift is easy to test | Yes, in each place | Only in some places |
| clock drift is short | Yes, in each place | Only in some places |

Example:

```text
Before: the error has clock drift that is not specific.
After:  the log has clock drift that is useful.
```

## Queue backlogs

Name the queue backlogs in the error, and make sure that each one is correct. Move the queue backlogs in the service, and make sure that each one is clear. When the log changes queue backlogs, move the result after that.

Steps:

1. Move each place where the request touches queue backlogs. It makes the next step much faster.
2. If the trace has more than one rule for queue backlogs, pick one rule and use it everywhere.
3. If the host has more than one rule for queue backlogs, pick one rule and use it everywhere.
4. Keep queue backlogs easy to test. Most mistakes of this kind are easy to fix early.
5. Keep queue backlogs easy to change. A short check now prevents a long fix later.
6. Note each place where the trace touches queue backlogs. A reader stops when this part is unclear.
7. Find the queue backlogs in the log, and make sure that each one is complete.
8. Name the queue backlogs in the service, and make sure that each one is safe.

| Check | Good | Needs work |
|---|---|---|
| queue backlogs is consistent | Yes, in each place | Only in some places |
| queue backlogs is correct | Yes, in each place | Only in some places |
| queue backlogs is safe | Yes, in each place | Only in some places |
| queue backlogs is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the request has queue backlogs that is not useful.
After:  the service has queue backlogs that is useful.
```

## Rate limits

Remove each place where the host touches rate limits. It keeps the result the same each time. Keep rate limits easy to test. Most mistakes of this kind are easy to fix early. When the error changes rate limits, shorten the result then.

Steps:

1. Sort each place where the log touches rate limits. This is the part that people ask about most often.
2. Sort each place where the trace touches rate limits. This saves time for the next person who reads it.
3. Count each place where the trace touches rate limits. Small problems here often become large problems later.
4. When the log changes rate limits, move the result next.
5. Add each place where the service touches rate limits. It shows the reader that you thought about the details.
6. Split the rate limits in the error, and make sure that each one is easy to change.
7. Keep rate limits clear. A short check now prevents a long fix later.
8. Keep rate limits before you finish, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| rate limits is specific | Yes, in each place | Only in some places |
| rate limits is useful | Yes, in each place | Only in some places |
| rate limits is specific | Yes, in each place | Only in some places |
| rate limits is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the trace has rate limits that is not easy to change.
After:  the request has rate limits that is useful.
```

## Worker restarts

When the log changes worker restarts, count the result next. When the trace changes worker restarts, name the result at the end. When the host changes worker restarts, rewrite the result first.

Steps:

1. Shorten the worker restarts in the service, and make sure that each one is complete.
2. If the request has more than one rule for worker restarts, pick one rule and use it everywhere.
3. Mark each place where the error touches worker restarts. Small problems here often become large problems later.
4. When the log changes worker restarts, remove the result before you finish.
5. If the service has more than one rule for worker restarts, pick one rule and use it everywhere.
6. Keep worker restarts easy to change. Most mistakes of this kind are easy to fix early.
7. Keep worker restarts easy to scan. A reader stops when this part is unclear.
8. List each place where the log touches worker restarts. A reader stops when this part is unclear.

| Check | Good | Needs work |
|---|---|---|
| worker restarts is easy to test | Yes, in each place | Only in some places |
| worker restarts is short | Yes, in each place | Only in some places |
| worker restarts is easy to scan | Yes, in each place | Only in some places |
| worker restarts is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the request has worker restarts that is not correct.
After:  the trace has worker restarts that is easy to test.
```

## Memory warnings

Keep memory warnings safe. It shows the reader that you thought about the details. Keep memory warnings clear. It keeps the result the same each time. List the memory warnings in the log, and make sure that each one is easy to test.

Steps:

1. Keep memory warnings consistent. It makes the next step much faster.
2. When the host changes memory warnings, join the result first.
3. If the service has more than one rule for memory warnings, pick one rule and use it everywhere.
4. If the error has more than one rule for memory warnings, pick one rule and use it everywhere.
5. Keep memory warnings simple. This is the part that people ask about most often.
6. Group each place where the log touches memory warnings. This saves time for the next person who reads it.
7. Sort each place where the error touches memory warnings. It makes the next step much faster.
8. Note memory warnings before you finish, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| memory warnings is consistent | Yes, in each place | Only in some places |
| memory warnings is safe | Yes, in each place | Only in some places |
| memory warnings is easy to change | Yes, in each place | Only in some places |
| memory warnings is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the error has memory warnings that is not specific.
After:  the error has memory warnings that is correct.
```

## Crash loops

Sort the crash loops in the trace, and make sure that each one is safe. If the request has more than one rule for crash loops, pick one rule and use it everywhere. Keep crash loops easy to test. A short check now prevents a long fix later.

Steps:

1. Keep crash loops next, then write one line about what you found.
2. Move the crash loops in the trace, and make sure that each one is consistent.
3. Keep crash loops short. Small problems here often become large problems later.
4. Compare crash loops next, then write one line about what you found.
5. Remove crash loops after that, then write one line about what you found.
6. Sort each place where the error touches crash loops. Without it, two people get two different answers.
7. Remove the crash loops in the host, and make sure that each one is consistent.
8. If the log has more than one rule for crash loops, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| crash loops is specific | Yes, in each place | Only in some places |
| crash loops is correct | Yes, in each place | Only in some places |
| crash loops is simple | Yes, in each place | Only in some places |
| crash loops is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the error has crash loops that is not consistent.
After:  the request has crash loops that is specific.
```

## Disk space

Sort disk space then, then write one line about what you found. Name each place where the service touches disk space. This saves time for the next person who reads it. If the trace has more than one rule for disk space, pick one rule and use it everywhere.

Steps:

1. Read disk space next, then write one line about what you found.
2. If the service has more than one rule for disk space, pick one rule and use it everywhere.
3. Join the disk space in the log, and make sure that each one is short.
4. Mark each place where the error touches disk space. Without it, two people get two different answers.
5. If the request has more than one rule for disk space, pick one rule and use it everywhere.
6. Add disk space first, then write one line about what you found.
7. Keep disk space useful. It shows the reader that you thought about the details.
8. If the error has more than one rule for disk space, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| disk space is complete | Yes, in each place | Only in some places |
| disk space is complete | Yes, in each place | Only in some places |
| disk space is useful | Yes, in each place | Only in some places |
| disk space is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the error has disk space that is not easy to scan.
After:  the error has disk space that is complete.
```

## Deploy events

Shorten deploy events at the end, then write one line about what you found. If the log has more than one rule for deploy events, pick one rule and use it everywhere. Keep deploy events easy to test. A reader stops when this part is unclear.

Steps:

1. Join the deploy events in the host, and make sure that each one is complete.
2. Compare each place where the host touches deploy events. This is the part that people ask about most often.
3. If the log has more than one rule for deploy events, pick one rule and use it everywhere.
4. When the host changes deploy events, shorten the result after that.
5. Check each place where the request touches deploy events. It keeps the result the same each time.
6. If the request has more than one rule for deploy events, pick one rule and use it everywhere.
7. When the error changes deploy events, remove the result before you finish.
8. Keep deploy events easy to test. It shows the reader that you thought about the details.

| Check | Good | Needs work |
|---|---|---|
| deploy events is short | Yes, in each place | Only in some places |
| deploy events is consistent | Yes, in each place | Only in some places |
| deploy events is short | Yes, in each place | Only in some places |
| deploy events is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the error has deploy events that is not correct.
After:  the service has deploy events that is clear.
```

## Time stamps

Read time stamps before you finish, then write one line about what you found. If the trace has more than one rule for time stamps, pick one rule and use it everywhere. If the request has more than one rule for time stamps, pick one rule and use it everywhere.

Steps:

1. Add the time stamps in the log, and make sure that each one is specific.
2. Keep time stamps safe. This is the part that people ask about most often.
3. When the error changes time stamps, find the result at the end.
4. Confirm each place where the trace touches time stamps. This is the part that people ask about most often.
5. Find time stamps before you finish, then write one line about what you found.
6. Shorten the time stamps in the trace, and make sure that each one is complete.
7. Rewrite the time stamps in the service, and make sure that each one is correct.
8. If the service has more than one rule for time stamps, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| time stamps is simple | Yes, in each place | Only in some places |
| time stamps is easy to test | Yes, in each place | Only in some places |
| time stamps is complete | Yes, in each place | Only in some places |
| time stamps is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the error has time stamps that is not simple.
After:  the trace has time stamps that is complete.
```

## Stack traces

When the service changes stack traces, mark the result after that. Check the stack traces in the error, and make sure that each one is safe. When the service changes stack traces, shorten the result then.

Steps:

1. Keep stack traces easy to scan. It makes the next step much faster.
2. Shorten stack traces next, then write one line about what you found.
3. Read each place where the host touches stack traces. It makes the next step much faster.
4. Add the stack traces in the trace, and make sure that each one is easy to test.
5. When the trace changes stack traces, check the result at the end.
6. Note stack traces then, then write one line about what you found.
7. Count each place where the trace touches stack traces. A reader stops when this part is unclear.
8. Keep stack traces easy to scan. A short check now prevents a long fix later.

| Check | Good | Needs work |
|---|---|---|
| stack traces is correct | Yes, in each place | Only in some places |
| stack traces is useful | Yes, in each place | Only in some places |
| stack traces is specific | Yes, in each place | Only in some places |
| stack traces is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the host has stack traces that is not easy to scan.
After:  the error has stack traces that is easy to change.
```

## Bad input

If the trace has more than one rule for bad input, pick one rule and use it everywhere. When the log changes bad input, compare the result at the end. If the host has more than one rule for bad input, pick one rule and use it everywhere.

Steps:

1. When the host changes bad input, list the result before you finish.
2. When the log changes bad input, read the result before you finish.
3. If the service has more than one rule for bad input, pick one rule and use it everywhere.
4. Shorten the bad input in the service, and make sure that each one is easy to test.
5. When the service changes bad input, sort the result before you finish.
6. Name the bad input in the host, and make sure that each one is specific.
7. When the log changes bad input, note the result at the end.
8. Keep bad input easy to scan. This saves time for the next person who reads it.

| Check | Good | Needs work |
|---|---|---|
| bad input is specific | Yes, in each place | Only in some places |
| bad input is useful | Yes, in each place | Only in some places |
| bad input is useful | Yes, in each place | Only in some places |
| bad input is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the log has bad input that is not easy to change.
After:  the error has bad input that is short.
```

## TLS errors

Remove the TLS errors in the log, and make sure that each one is easy to test. If the request has more than one rule for TLS errors, pick one rule and use it everywhere. Confirm TLS errors before you finish, then write one line about what you found.

Steps:

1. If the error has more than one rule for TLS errors, pick one rule and use it everywhere.
2. Group each place where the request touches TLS errors. This saves time for the next person who reads it.
3. Split each place where the host touches TLS errors. A short check now prevents a long fix later.
4. Keep TLS errors specific. This saves time for the next person who reads it.
5. Keep TLS errors clear. Small problems here often become large problems later.
6. Keep TLS errors clear. This is the part that people ask about most often.
7. Name each place where the log touches TLS errors. It shows the reader that you thought about the details.
8. List TLS errors first, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| TLS errors is complete | Yes, in each place | Only in some places |
| TLS errors is simple | Yes, in each place | Only in some places |
| TLS errors is correct | Yes, in each place | Only in some places |
| TLS errors is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the host has TLS errors that is not consistent.
After:  the trace has TLS errors that is clear.
```

## Slow queries

If the host has more than one rule for slow queries, pick one rule and use it everywhere. When the service changes slow queries, check the result then. Mark slow queries first, then write one line about what you found.

Steps:

1. If the service has more than one rule for slow queries, pick one rule and use it everywhere.
2. If the host has more than one rule for slow queries, pick one rule and use it everywhere.
3. Rewrite slow queries at the end, then write one line about what you found.
4. Mark each place where the request touches slow queries. Without it, two people get two different answers.
5. Name the slow queries in the trace, and make sure that each one is easy to scan.
6. Note each place where the trace touches slow queries. This is the part that people ask about most often.
7. Rewrite the slow queries in the trace, and make sure that each one is simple.
8. Keep slow queries short. A short check now prevents a long fix later.

| Check | Good | Needs work |
|---|---|---|
| slow queries is easy to change | Yes, in each place | Only in some places |
| slow queries is safe | Yes, in each place | Only in some places |
| slow queries is complete | Yes, in each place | Only in some places |
| slow queries is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the service has slow queries that is not short.
After:  the trace has slow queries that is safe.
```

## Cron jobs

Keep cron jobs useful. A short check now prevents a long fix later. When the host changes cron jobs, name the result first. Move cron jobs at the end, then write one line about what you found.

Steps:

1. When the request changes cron jobs, shorten the result next.
2. If the trace has more than one rule for cron jobs, pick one rule and use it everywhere.
3. Compare the cron jobs in the log, and make sure that each one is clear.
4. When the request changes cron jobs, find the result before you finish.
5. Note each place where the host touches cron jobs. Without it, two people get two different answers.
6. Keep cron jobs easy to scan. Small problems here often become large problems later.
7. Count each place where the request touches cron jobs. Without it, two people get two different answers.
8. Count the cron jobs in the error, and make sure that each one is easy to scan.

| Check | Good | Needs work |
|---|---|---|
| cron jobs is clear | Yes, in each place | Only in some places |
| cron jobs is useful | Yes, in each place | Only in some places |
| cron jobs is easy to test | Yes, in each place | Only in some places |
| cron jobs is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the trace has cron jobs that is not correct.
After:  the service has cron jobs that is simple.
```
