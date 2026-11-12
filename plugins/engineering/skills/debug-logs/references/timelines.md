# Timelines

## Schema changes

Name the schema changes in the host, and make sure that each one is safe. Add each place where the trace touches schema changes. A short check now prevents a long fix later. Keep schema changes easy to test. A reader stops when this part is unclear.

Steps:

1. Keep schema changes specific. Most mistakes of this kind are easy to fix early.
2. Find the schema changes in the error, and make sure that each one is consistent.
3. List each place where the log touches schema changes. A short check now prevents a long fix later.
4. Keep the schema changes in the host, and make sure that each one is clear.
5. Shorten schema changes after that, then write one line about what you found.
6. Rewrite schema changes at the end, then write one line about what you found.
7. Confirm schema changes then, then write one line about what you found.
8. Join schema changes at the end, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| schema changes is safe | Yes, in each place | Only in some places |
| schema changes is easy to change | Yes, in each place | Only in some places |
| schema changes is complete | Yes, in each place | Only in some places |
| schema changes is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the log has schema changes that is not clear.
After:  the host has schema changes that is clear.
```

## Memory warnings

Keep memory warnings complete. It keeps the result the same each time. Note the memory warnings in the request, and make sure that each one is safe. Read memory warnings next, then write one line about what you found.

Steps:

1. Split each place where the log touches memory warnings. A reader stops when this part is unclear.
2. When the trace changes memory warnings, read the result then.
3. Remove the memory warnings in the host, and make sure that each one is correct.
4. When the host changes memory warnings, note the result next.
5. When the trace changes memory warnings, rewrite the result before you finish.
6. Add memory warnings before you finish, then write one line about what you found.
7. If the host has more than one rule for memory warnings, pick one rule and use it everywhere.
8. Split memory warnings after that, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| memory warnings is correct | Yes, in each place | Only in some places |
| memory warnings is short | Yes, in each place | Only in some places |
| memory warnings is short | Yes, in each place | Only in some places |
| memory warnings is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the trace has memory warnings that is not complete.
After:  the trace has memory warnings that is correct.
```

## Worker restarts

Count each place where the error touches worker restarts. It makes the next step much faster. If the log has more than one rule for worker restarts, pick one rule and use it everywhere. If the service has more than one rule for worker restarts, pick one rule and use it everywhere.

Steps:

1. Confirm each place where the service touches worker restarts. It makes the next step much faster.
2. Group each place where the trace touches worker restarts. Most mistakes of this kind are easy to fix early.
3. When the request changes worker restarts, confirm the result after that.
4. When the host changes worker restarts, read the result next.
5. Confirm the worker restarts in the error, and make sure that each one is specific.
6. If the request has more than one rule for worker restarts, pick one rule and use it everywhere.
7. Note worker restarts next, then write one line about what you found.
8. Sort each place where the log touches worker restarts. A short check now prevents a long fix later.

| Check | Good | Needs work |
|---|---|---|
| worker restarts is consistent | Yes, in each place | Only in some places |
| worker restarts is consistent | Yes, in each place | Only in some places |
| worker restarts is complete | Yes, in each place | Only in some places |
| worker restarts is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the error has worker restarts that is not easy to scan.
After:  the log has worker restarts that is safe.
```

## Crash loops

Compare the crash loops in the error, and make sure that each one is safe. Keep the crash loops in the request, and make sure that each one is consistent. Remove each place where the log touches crash loops. This is the part that people ask about most often.

Steps:

1. When the request changes crash loops, group the result before you finish.
2. Find crash loops then, then write one line about what you found.
3. Keep crash loops clear. It shows the reader that you thought about the details.
4. When the host changes crash loops, list the result next.
5. If the log has more than one rule for crash loops, pick one rule and use it everywhere.
6. Join crash loops next, then write one line about what you found.
7. Group each place where the request touches crash loops. It keeps the result the same each time.
8. Count the crash loops in the trace, and make sure that each one is easy to scan.

| Check | Good | Needs work |
|---|---|---|
| crash loops is clear | Yes, in each place | Only in some places |
| crash loops is easy to scan | Yes, in each place | Only in some places |
| crash loops is correct | Yes, in each place | Only in some places |
| crash loops is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the request has crash loops that is not complete.
After:  the service has crash loops that is simple.
```

## Partial outages

Add partial outages then, then write one line about what you found. When the service changes partial outages, remove the result after that. If the log has more than one rule for partial outages, pick one rule and use it everywhere.

Steps:

1. Sort each place where the error touches partial outages. Most mistakes of this kind are easy to fix early.
2. Find each place where the host touches partial outages. This saves time for the next person who reads it.
3. If the error has more than one rule for partial outages, pick one rule and use it everywhere.
4. When the error changes partial outages, shorten the result before you finish.
5. When the error changes partial outages, note the result first.
6. Keep partial outages specific. This is the part that people ask about most often.
7. Read partial outages before you finish, then write one line about what you found.
8. If the log has more than one rule for partial outages, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| partial outages is complete | Yes, in each place | Only in some places |
| partial outages is easy to test | Yes, in each place | Only in some places |
| partial outages is short | Yes, in each place | Only in some places |
| partial outages is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the service has partial outages that is not specific.
After:  the trace has partial outages that is easy to test.
```

## Clock drift

When the request changes clock drift, compare the result then. If the error has more than one rule for clock drift, pick one rule and use it everywhere. Name each place where the service touches clock drift. A short check now prevents a long fix later.

Steps:

1. If the trace has more than one rule for clock drift, pick one rule and use it everywhere.
2. Name each place where the trace touches clock drift. It shows the reader that you thought about the details.
3. Find clock drift before you finish, then write one line about what you found.
4. When the trace changes clock drift, move the result next.
5. If the host has more than one rule for clock drift, pick one rule and use it everywhere.
6. When the host changes clock drift, compare the result before you finish.
7. Move each place where the request touches clock drift. It shows the reader that you thought about the details.
8. Rewrite clock drift first, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| clock drift is specific | Yes, in each place | Only in some places |
| clock drift is easy to change | Yes, in each place | Only in some places |
| clock drift is useful | Yes, in each place | Only in some places |
| clock drift is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the error has clock drift that is not easy to scan.
After:  the log has clock drift that is easy to test.
```

## Request IDs

Confirm request IDs at the end, then write one line about what you found. Mark request IDs then, then write one line about what you found. If the error has more than one rule for request IDs, pick one rule and use it everywhere.

Steps:

1. Move the request IDs in the request, and make sure that each one is specific.
2. If the request has more than one rule for request IDs, pick one rule and use it everywhere.
3. Find request IDs before you finish, then write one line about what you found.
4. When the error changes request IDs, compare the result next.
5. Keep request IDs specific. This is the part that people ask about most often.
6. Read request IDs after that, then write one line about what you found.
7. If the request has more than one rule for request IDs, pick one rule and use it everywhere.
8. Mark the request IDs in the request, and make sure that each one is easy to scan.

| Check | Good | Needs work |
|---|---|---|
| request IDs is specific | Yes, in each place | Only in some places |
| request IDs is safe | Yes, in each place | Only in some places |
| request IDs is useful | Yes, in each place | Only in some places |
| request IDs is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the error has request IDs that is not useful.
After:  the log has request IDs that is specific.
```

## Lock waits

Sort each place where the log touches lock waits. A short check now prevents a long fix later. Note each place where the service touches lock waits. It keeps the result the same each time. Keep lock waits easy to scan. Small problems here often become large problems later.

Steps:

1. Keep lock waits easy to test. Small problems here often become large problems later.
2. Keep lock waits then, then write one line about what you found.
3. When the trace changes lock waits, count the result next.
4. When the log changes lock waits, rewrite the result then.
5. If the error has more than one rule for lock waits, pick one rule and use it everywhere.
6. When the error changes lock waits, join the result first.
7. If the trace has more than one rule for lock waits, pick one rule and use it everywhere.
8. When the error changes lock waits, keep the result before you finish.

| Check | Good | Needs work |
|---|---|---|
| lock waits is easy to test | Yes, in each place | Only in some places |
| lock waits is useful | Yes, in each place | Only in some places |
| lock waits is useful | Yes, in each place | Only in some places |
| lock waits is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the host has lock waits that is not easy to scan.
After:  the request has lock waits that is useful.
```

## Retries

Mark each place where the service touches retries. It makes the next step much faster. Remove each place where the service touches retries. A reader stops when this part is unclear. Compare retries after that, then write one line about what you found.

Steps:

1. If the request has more than one rule for retries, pick one rule and use it everywhere.
2. List retries at the end, then write one line about what you found.
3. When the request changes retries, remove the result then.
4. Find the retries in the service, and make sure that each one is clear.
5. Keep retries specific. This is the part that people ask about most often.
6. Add the retries in the error, and make sure that each one is easy to scan.
7. Sort each place where the host touches retries. It shows the reader that you thought about the details.
8. Keep retries complete. It shows the reader that you thought about the details.

| Check | Good | Needs work |
|---|---|---|
| retries is complete | Yes, in each place | Only in some places |
| retries is easy to test | Yes, in each place | Only in some places |
| retries is useful | Yes, in each place | Only in some places |
| retries is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the service has retries that is not complete.
After:  the log has retries that is correct.
```

## Stack traces

Group each place where the host touches stack traces. This saves time for the next person who reads it. Find each place where the service touches stack traces. This saves time for the next person who reads it. Keep stack traces short. Small problems here often become large problems later.

Steps:

1. List each place where the trace touches stack traces. Without it, two people get two different answers.
2. Keep stack traces specific. This is the part that people ask about most often.
3. When the log changes stack traces, note the result after that.
4. List stack traces then, then write one line about what you found.
5. Keep stack traces easy to change. Without it, two people get two different answers.
6. Sort each place where the trace touches stack traces. A reader stops when this part is unclear.
7. Keep stack traces easy to test. It keeps the result the same each time.
8. Keep stack traces clear. Small problems here often become large problems later.

| Check | Good | Needs work |
|---|---|---|
| stack traces is specific | Yes, in each place | Only in some places |
| stack traces is consistent | Yes, in each place | Only in some places |
| stack traces is correct | Yes, in each place | Only in some places |
| stack traces is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the request has stack traces that is not specific.
After:  the trace has stack traces that is clear.
```

## Queue backlogs

Count the queue backlogs in the trace, and make sure that each one is clear. Rewrite the queue backlogs in the trace, and make sure that each one is specific. Rewrite each place where the request touches queue backlogs. It makes the next step much faster.

Steps:

1. Add each place where the service touches queue backlogs. Small problems here often become large problems later.
2. Mark the queue backlogs in the service, and make sure that each one is useful.
3. Join queue backlogs next, then write one line about what you found.
4. If the host has more than one rule for queue backlogs, pick one rule and use it everywhere.
5. If the error has more than one rule for queue backlogs, pick one rule and use it everywhere.
6. Check the queue backlogs in the log, and make sure that each one is correct.
7. List queue backlogs after that, then write one line about what you found.
8. If the service has more than one rule for queue backlogs, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| queue backlogs is complete | Yes, in each place | Only in some places |
| queue backlogs is short | Yes, in each place | Only in some places |
| queue backlogs is correct | Yes, in each place | Only in some places |
| queue backlogs is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the request has queue backlogs that is not simple.
After:  the log has queue backlogs that is simple.
```

## Time stamps

Keep time stamps clear. This saves time for the next person who reads it. List time stamps after that, then write one line about what you found. Sort each place where the error touches time stamps. This is the part that people ask about most often.

Steps:

1. Group each place where the service touches time stamps. It makes the next step much faster.
2. Rewrite the time stamps in the request, and make sure that each one is safe.
3. Sort time stamps after that, then write one line about what you found.
4. If the log has more than one rule for time stamps, pick one rule and use it everywhere.
5. If the error has more than one rule for time stamps, pick one rule and use it everywhere.
6. If the request has more than one rule for time stamps, pick one rule and use it everywhere.
7. Add the time stamps in the log, and make sure that each one is consistent.
8. When the host changes time stamps, list the result then.

| Check | Good | Needs work |
|---|---|---|
| time stamps is useful | Yes, in each place | Only in some places |
| time stamps is safe | Yes, in each place | Only in some places |
| time stamps is specific | Yes, in each place | Only in some places |
| time stamps is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the request has time stamps that is not useful.
After:  the log has time stamps that is simple.
```

## Rate limits

Keep rate limits safe. A reader stops when this part is unclear. Check the rate limits in the request, and make sure that each one is easy to test. When the host changes rate limits, move the result then.

Steps:

1. If the error has more than one rule for rate limits, pick one rule and use it everywhere.
2. When the error changes rate limits, group the result before you finish.
3. Join rate limits then, then write one line about what you found.
4. Sort each place where the trace touches rate limits. Most mistakes of this kind are easy to fix early.
5. Count each place where the host touches rate limits. It keeps the result the same each time.
6. Keep each place where the request touches rate limits. Most mistakes of this kind are easy to fix early.
7. Keep rate limits short. A short check now prevents a long fix later.
8. When the trace changes rate limits, split the result next.

| Check | Good | Needs work |
|---|---|---|
| rate limits is simple | Yes, in each place | Only in some places |
| rate limits is easy to change | Yes, in each place | Only in some places |
| rate limits is easy to change | Yes, in each place | Only in some places |
| rate limits is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the log has rate limits that is not easy to scan.
After:  the host has rate limits that is specific.
```

## DNS errors

Find the DNS errors in the trace, and make sure that each one is safe. List each place where the error touches DNS errors. A reader stops when this part is unclear. If the request has more than one rule for DNS errors, pick one rule and use it everywhere.

Steps:

1. When the log changes DNS errors, sort the result next.
2. Shorten the DNS errors in the error, and make sure that each one is consistent.
3. Mark the DNS errors in the service, and make sure that each one is short.
4. Count each place where the service touches DNS errors. Most mistakes of this kind are easy to fix early.
5. Add the DNS errors in the trace, and make sure that each one is clear.
6. When the request changes DNS errors, group the result before you finish.
7. Mark each place where the host touches DNS errors. It shows the reader that you thought about the details.
8. If the request has more than one rule for DNS errors, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| DNS errors is useful | Yes, in each place | Only in some places |
| DNS errors is consistent | Yes, in each place | Only in some places |
| DNS errors is complete | Yes, in each place | Only in some places |
| DNS errors is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the trace has DNS errors that is not consistent.
After:  the trace has DNS errors that is useful.
```

## TLS errors

Check each place where the service touches TLS errors. It makes the next step much faster. Keep TLS errors safe. A reader stops when this part is unclear. Count each place where the request touches TLS errors. It keeps the result the same each time.

Steps:

1. If the error has more than one rule for TLS errors, pick one rule and use it everywhere.
2. Mark each place where the trace touches TLS errors. This is the part that people ask about most often.
3. If the host has more than one rule for TLS errors, pick one rule and use it everywhere.
4. When the error changes TLS errors, keep the result after that.
5. If the trace has more than one rule for TLS errors, pick one rule and use it everywhere.
6. Confirm each place where the log touches TLS errors. Small problems here often become large problems later.
7. When the host changes TLS errors, note the result at the end.
8. Add TLS errors at the end, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| TLS errors is specific | Yes, in each place | Only in some places |
| TLS errors is complete | Yes, in each place | Only in some places |
| TLS errors is easy to test | Yes, in each place | Only in some places |
| TLS errors is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the trace has TLS errors that is not easy to test.
After:  the request has TLS errors that is easy to scan.
```

## Cache misses

Mark the cache misses in the log, and make sure that each one is consistent. Group each place where the error touches cache misses. It keeps the result the same each time. Count cache misses next, then write one line about what you found.

Steps:

1. List cache misses before you finish, then write one line about what you found.
2. When the log changes cache misses, sort the result next.
3. Keep cache misses correct. Without it, two people get two different answers.
4. When the host changes cache misses, group the result first.
5. Keep cache misses safe. A short check now prevents a long fix later.
6. Keep cache misses at the end, then write one line about what you found.
7. Keep cache misses clear. Small problems here often become large problems later.
8. List cache misses before you finish, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| cache misses is complete | Yes, in each place | Only in some places |
| cache misses is easy to test | Yes, in each place | Only in some places |
| cache misses is short | Yes, in each place | Only in some places |
| cache misses is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the error has cache misses that is not clear.
After:  the error has cache misses that is useful.
```

## Bad input

Add the bad input in the service, and make sure that each one is consistent. Split bad input first, then write one line about what you found. If the error has more than one rule for bad input, pick one rule and use it everywhere.

Steps:

1. Keep bad input short. This saves time for the next person who reads it.
2. If the request has more than one rule for bad input, pick one rule and use it everywhere.
3. Keep each place where the log touches bad input. A short check now prevents a long fix later.
4. Keep bad input useful. It shows the reader that you thought about the details.
5. If the service has more than one rule for bad input, pick one rule and use it everywhere.
6. When the trace changes bad input, mark the result first.
7. Sort each place where the host touches bad input. It keeps the result the same each time.
8. Keep bad input before you finish, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| bad input is specific | Yes, in each place | Only in some places |
| bad input is useful | Yes, in each place | Only in some places |
| bad input is consistent | Yes, in each place | Only in some places |
| bad input is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the host has bad input that is not easy to scan.
After:  the request has bad input that is easy to test.
```

## Health checks

Name each place where the host touches health checks. Without it, two people get two different answers. If the trace has more than one rule for health checks, pick one rule and use it everywhere. Split health checks after that, then write one line about what you found.

Steps:

1. When the request changes health checks, join the result next.
2. If the error has more than one rule for health checks, pick one rule and use it everywhere.
3. Keep health checks correct. It shows the reader that you thought about the details.
4. Keep health checks short. It shows the reader that you thought about the details.
5. Remove each place where the host touches health checks. It keeps the result the same each time.
6. When the trace changes health checks, split the result then.
7. Shorten health checks first, then write one line about what you found.
8. When the log changes health checks, keep the result before you finish.

| Check | Good | Needs work |
|---|---|---|
| health checks is simple | Yes, in each place | Only in some places |
| health checks is specific | Yes, in each place | Only in some places |
| health checks is clear | Yes, in each place | Only in some places |
| health checks is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the log has health checks that is not specific.
After:  the log has health checks that is easy to test.
```

## Timeouts

Shorten each place where the error touches timeouts. This saves time for the next person who reads it. Mark timeouts first, then write one line about what you found. Keep timeouts easy to test. A reader stops when this part is unclear.

Steps:

1. Remove timeouts before you finish, then write one line about what you found.
2. If the log has more than one rule for timeouts, pick one rule and use it everywhere.
3. Shorten timeouts then, then write one line about what you found.
4. When the host changes timeouts, check the result after that.
5. Keep timeouts complete. A short check now prevents a long fix later.
6. List the timeouts in the log, and make sure that each one is simple.
7. Add timeouts first, then write one line about what you found.
8. Keep timeouts safe. A reader stops when this part is unclear.

| Check | Good | Needs work |
|---|---|---|
| timeouts is short | Yes, in each place | Only in some places |
| timeouts is useful | Yes, in each place | Only in some places |
| timeouts is specific | Yes, in each place | Only in some places |
| timeouts is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the error has timeouts that is not easy to change.
After:  the host has timeouts that is safe.
```
