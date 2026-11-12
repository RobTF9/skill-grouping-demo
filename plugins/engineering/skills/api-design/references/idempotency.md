# Idempotency

## Webhooks

Compare each place where the response touches webhooks. It keeps the result the same each time. If the endpoint has more than one rule for webhooks, pick one rule and use it everywhere. When the client changes webhooks, split the result then.

Steps:

1. Split webhooks next, then write one line about what you found.
2. Keep webhooks complete. Small problems here often become large problems later.
3. Remove webhooks after that, then write one line about what you found.
4. Keep webhooks specific. A reader stops when this part is unclear.
5. Keep webhooks easy to test. It shows the reader that you thought about the details.
6. Move the webhooks in the endpoint, and make sure that each one is simple.
7. Keep webhooks safe. It makes the next step much faster.
8. When the resource changes webhooks, count the result next.

| Check | Good | Needs work |
|---|---|---|
| webhooks is complete | Yes, in each place | Only in some places |
| webhooks is specific | Yes, in each place | Only in some places |
| webhooks is simple | Yes, in each place | Only in some places |
| webhooks is short | Yes, in each place | Only in some places |

Example:

```text
Before: the endpoint has webhooks that is not complete.
After:  the request has webhooks that is safe.
```

## Partial updates

Group the partial updates in the resource, and make sure that each one is easy to test. If the request has more than one rule for partial updates, pick one rule and use it everywhere. If the client has more than one rule for partial updates, pick one rule and use it everywhere.

Steps:

1. When the endpoint changes partial updates, add the result then.
2. If the resource has more than one rule for partial updates, pick one rule and use it everywhere.
3. Compare each place where the response touches partial updates. Small problems here often become large problems later.
4. When the response changes partial updates, confirm the result after that.
5. When the request changes partial updates, rewrite the result first.
6. Rewrite the partial updates in the client, and make sure that each one is easy to change.
7. Mark the partial updates in the endpoint, and make sure that each one is correct.
8. Remove each place where the endpoint touches partial updates. Most mistakes of this kind are easy to fix early.

| Check | Good | Needs work |
|---|---|---|
| partial updates is simple | Yes, in each place | Only in some places |
| partial updates is easy to scan | Yes, in each place | Only in some places |
| partial updates is simple | Yes, in each place | Only in some places |
| partial updates is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the client has partial updates that is not useful.
After:  the resource has partial updates that is safe.
```

## Field names

Keep field names consistent. A reader stops when this part is unclear. If the response has more than one rule for field names, pick one rule and use it everywhere. When the schema changes field names, sort the result first.

Steps:

1. Read the field names in the request, and make sure that each one is clear.
2. If the schema has more than one rule for field names, pick one rule and use it everywhere.
3. If the resource has more than one rule for field names, pick one rule and use it everywhere.
4. Group the field names in the response, and make sure that each one is clear.
5. Read each place where the response touches field names. Small problems here often become large problems later.
6. Group each place where the client touches field names. A short check now prevents a long fix later.
7. When the endpoint changes field names, compare the result before you finish.
8. If the schema has more than one rule for field names, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| field names is clear | Yes, in each place | Only in some places |
| field names is easy to scan | Yes, in each place | Only in some places |
| field names is specific | Yes, in each place | Only in some places |
| field names is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the response has field names that is not safe.
After:  the resource has field names that is short.
```

## Paging

If the response has more than one rule for paging, pick one rule and use it everywhere. If the endpoint has more than one rule for paging, pick one rule and use it everywhere. Name paging next, then write one line about what you found.

Steps:

1. Join paging at the end, then write one line about what you found.
2. When the schema changes paging, mark the result next.
3. Shorten paging first, then write one line about what you found.
4. Join each place where the schema touches paging. Without it, two people get two different answers.
5. Group the paging in the resource, and make sure that each one is easy to test.
6. If the request has more than one rule for paging, pick one rule and use it everywhere.
7. Mark paging before you finish, then write one line about what you found.
8. Split the paging in the request, and make sure that each one is short.

| Check | Good | Needs work |
|---|---|---|
| paging is specific | Yes, in each place | Only in some places |
| paging is easy to change | Yes, in each place | Only in some places |
| paging is easy to scan | Yes, in each place | Only in some places |
| paging is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the schema has paging that is not useful.
After:  the response has paging that is specific.
```

## Rate limits

Keep rate limits easy to scan. A short check now prevents a long fix later. Shorten rate limits first, then write one line about what you found. Group the rate limits in the client, and make sure that each one is simple.

Steps:

1. Keep rate limits useful. This is the part that people ask about most often.
2. When the response changes rate limits, rewrite the result first.
3. Add the rate limits in the endpoint, and make sure that each one is easy to scan.
4. Add the rate limits in the endpoint, and make sure that each one is useful.
5. When the request changes rate limits, confirm the result next.
6. Keep rate limits short. Without it, two people get two different answers.
7. Move rate limits after that, then write one line about what you found.
8. Sort each place where the schema touches rate limits. It shows the reader that you thought about the details.

| Check | Good | Needs work |
|---|---|---|
| rate limits is specific | Yes, in each place | Only in some places |
| rate limits is easy to change | Yes, in each place | Only in some places |
| rate limits is specific | Yes, in each place | Only in some places |
| rate limits is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the request has rate limits that is not clear.
After:  the endpoint has rate limits that is useful.
```

## IDs

If the request has more than one rule for IDs, pick one rule and use it everywhere. If the request has more than one rule for IDs, pick one rule and use it everywhere. If the request has more than one rule for IDs, pick one rule and use it everywhere.

Steps:

1. Move each place where the request touches IDs. Without it, two people get two different answers.
2. When the response changes IDs, find the result next.
3. Keep IDs useful. A reader stops when this part is unclear.
4. Shorten each place where the schema touches IDs. Most mistakes of this kind are easy to fix early.
5. Read IDs first, then write one line about what you found.
6. Mark the IDs in the schema, and make sure that each one is easy to test.
7. Keep IDs at the end, then write one line about what you found.
8. Check each place where the request touches IDs. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| IDs is short | Yes, in each place | Only in some places |
| IDs is clear | Yes, in each place | Only in some places |
| IDs is useful | Yes, in each place | Only in some places |
| IDs is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the resource has IDs that is not short.
After:  the endpoint has IDs that is clear.
```

## File uploads

Check each place where the client touches file uploads. This is the part that people ask about most often. Mark each place where the client touches file uploads. Without it, two people get two different answers. If the response has more than one rule for file uploads, pick one rule and use it everywhere.

Steps:

1. Find the file uploads in the response, and make sure that each one is easy to test.
2. Remove file uploads after that, then write one line about what you found.
3. Keep file uploads easy to test. Most mistakes of this kind are easy to fix early.
4. Rewrite each place where the resource touches file uploads. A short check now prevents a long fix later.
5. Keep file uploads specific. It makes the next step much faster.
6. When the endpoint changes file uploads, move the result next.
7. Check each place where the endpoint touches file uploads. This saves time for the next person who reads it.
8. Keep file uploads short. It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| file uploads is useful | Yes, in each place | Only in some places |
| file uploads is consistent | Yes, in each place | Only in some places |
| file uploads is easy to change | Yes, in each place | Only in some places |
| file uploads is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the endpoint has file uploads that is not safe.
After:  the endpoint has file uploads that is correct.
```

## Idempotency

Rewrite the idempotency in the response, and make sure that each one is correct. Remove each place where the schema touches idempotency. It shows the reader that you thought about the details. Keep each place where the client touches idempotency. It shows the reader that you thought about the details.

Steps:

1. Find idempotency after that, then write one line about what you found.
2. Keep idempotency easy to scan. Small problems here often become large problems later.
3. When the response changes idempotency, read the result before you finish.
4. When the response changes idempotency, move the result then.
5. Add the idempotency in the schema, and make sure that each one is easy to scan.
6. Keep idempotency correct. This is the part that people ask about most often.
7. Count idempotency first, then write one line about what you found.
8. Keep idempotency complete. Small problems here often become large problems later.

| Check | Good | Needs work |
|---|---|---|
| idempotency is correct | Yes, in each place | Only in some places |
| idempotency is simple | Yes, in each place | Only in some places |
| idempotency is easy to change | Yes, in each place | Only in some places |
| idempotency is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the resource has idempotency that is not correct.
After:  the schema has idempotency that is safe.
```

## Enums

If the response has more than one rule for enums, pick one rule and use it everywhere. Compare enums next, then write one line about what you found. When the request changes enums, note the result before you finish.

Steps:

1. Mark enums before you finish, then write one line about what you found.
2. Find each place where the resource touches enums. Small problems here often become large problems later.
3. Keep enums short. It shows the reader that you thought about the details.
4. Remove the enums in the schema, and make sure that each one is specific.
5. Find each place where the resource touches enums. Most mistakes of this kind are easy to fix early.
6. Remove each place where the response touches enums. Small problems here often become large problems later.
7. Keep enums easy to test. This saves time for the next person who reads it.
8. When the endpoint changes enums, mark the result then.

| Check | Good | Needs work |
|---|---|---|
| enums is easy to test | Yes, in each place | Only in some places |
| enums is easy to test | Yes, in each place | Only in some places |
| enums is safe | Yes, in each place | Only in some places |
| enums is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the client has enums that is not useful.
After:  the response has enums that is complete.
```

## Search

Keep search simple. A reader stops when this part is unclear. Find search first, then write one line about what you found. Check the search in the schema, and make sure that each one is correct.

Steps:

1. Keep search specific. It shows the reader that you thought about the details.
2. List the search in the endpoint, and make sure that each one is clear.
3. Keep search safe. Without it, two people get two different answers.
4. Join the search in the response, and make sure that each one is consistent.
5. Keep search consistent. This is the part that people ask about most often.
6. When the schema changes search, confirm the result first.
7. Name each place where the schema touches search. It shows the reader that you thought about the details.
8. Read search at the end, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| search is easy to scan | Yes, in each place | Only in some places |
| search is correct | Yes, in each place | Only in some places |
| search is easy to change | Yes, in each place | Only in some places |
| search is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the schema has search that is not consistent.
After:  the schema has search that is useful.
```

## Bulk actions

Keep bulk actions safe. It keeps the result the same each time. Count the bulk actions in the resource, and make sure that each one is specific. Check each place where the endpoint touches bulk actions. Without it, two people get two different answers.

Steps:

1. Check bulk actions before you finish, then write one line about what you found.
2. Keep bulk actions safe. Most mistakes of this kind are easy to fix early.
3. If the request has more than one rule for bulk actions, pick one rule and use it everywhere.
4. Keep bulk actions specific. Without it, two people get two different answers.
5. Keep bulk actions useful. A reader stops when this part is unclear.
6. Group each place where the response touches bulk actions. This is the part that people ask about most often.
7. Move each place where the client touches bulk actions. Small problems here often become large problems later.
8. Find bulk actions first, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| bulk actions is clear | Yes, in each place | Only in some places |
| bulk actions is easy to test | Yes, in each place | Only in some places |
| bulk actions is easy to scan | Yes, in each place | Only in some places |
| bulk actions is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the response has bulk actions that is not clear.
After:  the response has bulk actions that is complete.
```

## Conditional requests

If the resource has more than one rule for conditional requests, pick one rule and use it everywhere. Check conditional requests first, then write one line about what you found. Mark each place where the schema touches conditional requests. This saves time for the next person who reads it.

Steps:

1. Move conditional requests before you finish, then write one line about what you found.
2. When the schema changes conditional requests, name the result then.
3. Note conditional requests then, then write one line about what you found.
4. If the response has more than one rule for conditional requests, pick one rule and use it everywhere.
5. If the client has more than one rule for conditional requests, pick one rule and use it everywhere.
6. Shorten each place where the request touches conditional requests. A short check now prevents a long fix later.
7. Keep conditional requests specific. This is the part that people ask about most often.
8. Find each place where the request touches conditional requests. It keeps the result the same each time.

| Check | Good | Needs work |
|---|---|---|
| conditional requests is clear | Yes, in each place | Only in some places |
| conditional requests is specific | Yes, in each place | Only in some places |
| conditional requests is easy to test | Yes, in each place | Only in some places |
| conditional requests is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the schema has conditional requests that is not easy to scan.
After:  the response has conditional requests that is safe.
```

## Filters

Count the filters in the resource, and make sure that each one is safe. If the client has more than one rule for filters, pick one rule and use it everywhere. When the resource changes filters, note the result after that.

Steps:

1. When the request changes filters, mark the result before you finish.
2. When the endpoint changes filters, keep the result at the end.
3. Shorten the filters in the client, and make sure that each one is easy to change.
4. If the client has more than one rule for filters, pick one rule and use it everywhere.
5. List filters first, then write one line about what you found.
6. Group the filters in the endpoint, and make sure that each one is consistent.
7. Keep filters easy to change. Small problems here often become large problems later.
8. Keep filters useful. Most mistakes of this kind are easy to fix early.

| Check | Good | Needs work |
|---|---|---|
| filters is easy to test | Yes, in each place | Only in some places |
| filters is clear | Yes, in each place | Only in some places |
| filters is specific | Yes, in each place | Only in some places |
| filters is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the response has filters that is not short.
After:  the resource has filters that is safe.
```

## Date formats

Sort the date formats in the endpoint, and make sure that each one is simple. Check the date formats in the response, and make sure that each one is complete. If the resource has more than one rule for date formats, pick one rule and use it everywhere.

Steps:

1. Add each place where the schema touches date formats. Without it, two people get two different answers.
2. Keep date formats easy to change. Most mistakes of this kind are easy to fix early.
3. Rewrite the date formats in the resource, and make sure that each one is safe.
4. Check each place where the client touches date formats. It makes the next step much faster.
5. Mark date formats after that, then write one line about what you found.
6. Keep the date formats in the request, and make sure that each one is easy to scan.
7. Compare date formats before you finish, then write one line about what you found.
8. Rewrite the date formats in the resource, and make sure that each one is easy to test.

| Check | Good | Needs work |
|---|---|---|
| date formats is easy to test | Yes, in each place | Only in some places |
| date formats is correct | Yes, in each place | Only in some places |
| date formats is simple | Yes, in each place | Only in some places |
| date formats is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the client has date formats that is not easy to change.
After:  the endpoint has date formats that is consistent.
```

## Status codes

Keep status codes simple. It keeps the result the same each time. When the request changes status codes, sort the result before you finish. If the client has more than one rule for status codes, pick one rule and use it everywhere.

Steps:

1. Keep status codes safe. It makes the next step much faster.
2. Move each place where the response touches status codes. This is the part that people ask about most often.
3. If the schema has more than one rule for status codes, pick one rule and use it everywhere.
4. Shorten each place where the endpoint touches status codes. It keeps the result the same each time.
5. When the response changes status codes, rewrite the result first.
6. When the endpoint changes status codes, keep the result next.
7. Keep status codes consistent. It makes the next step much faster.
8. When the endpoint changes status codes, note the result then.

| Check | Good | Needs work |
|---|---|---|
| status codes is short | Yes, in each place | Only in some places |
| status codes is easy to test | Yes, in each place | Only in some places |
| status codes is useful | Yes, in each place | Only in some places |
| status codes is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the request has status codes that is not specific.
After:  the schema has status codes that is easy to change.
```

## Long tasks

When the response changes long tasks, shorten the result after that. Mark the long tasks in the endpoint, and make sure that each one is specific. Keep long tasks short. Most mistakes of this kind are easy to fix early.

Steps:

1. Keep the long tasks in the client, and make sure that each one is consistent.
2. Add the long tasks in the schema, and make sure that each one is easy to scan.
3. Rewrite the long tasks in the request, and make sure that each one is short.
4. If the client has more than one rule for long tasks, pick one rule and use it everywhere.
5. When the resource changes long tasks, note the result then.
6. If the schema has more than one rule for long tasks, pick one rule and use it everywhere.
7. If the client has more than one rule for long tasks, pick one rule and use it everywhere.
8. When the client changes long tasks, count the result at the end.

| Check | Good | Needs work |
|---|---|---|
| long tasks is specific | Yes, in each place | Only in some places |
| long tasks is correct | Yes, in each place | Only in some places |
| long tasks is short | Yes, in each place | Only in some places |
| long tasks is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the response has long tasks that is not safe.
After:  the client has long tasks that is consistent.
```

## Deprecation

If the endpoint has more than one rule for deprecation, pick one rule and use it everywhere. Confirm each place where the request touches deprecation. A short check now prevents a long fix later. Split deprecation then, then write one line about what you found.

Steps:

1. Remove the deprecation in the endpoint, and make sure that each one is easy to change.
2. When the schema changes deprecation, check the result next.
3. Count each place where the request touches deprecation. Without it, two people get two different answers.
4. If the request has more than one rule for deprecation, pick one rule and use it everywhere.
5. Confirm each place where the client touches deprecation. A reader stops when this part is unclear.
6. Remove each place where the client touches deprecation. It makes the next step much faster.
7. If the client has more than one rule for deprecation, pick one rule and use it everywhere.
8. Move deprecation before you finish, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| deprecation is complete | Yes, in each place | Only in some places |
| deprecation is consistent | Yes, in each place | Only in some places |
| deprecation is simple | Yes, in each place | Only in some places |
| deprecation is short | Yes, in each place | Only in some places |

Example:

```text
Before: the request has deprecation that is not specific.
After:  the resource has deprecation that is short.
```

## Caching headers

When the client changes caching headers, move the result after that. Compare the caching headers in the request, and make sure that each one is easy to test. When the response changes caching headers, sort the result first.

Steps:

1. Keep caching headers after that, then write one line about what you found.
2. Keep caching headers after that, then write one line about what you found.
3. When the schema changes caching headers, join the result then.
4. Read the caching headers in the schema, and make sure that each one is complete.
5. When the resource changes caching headers, group the result next.
6. Name the caching headers in the resource, and make sure that each one is short.
7. If the response has more than one rule for caching headers, pick one rule and use it everywhere.
8. Compare each place where the endpoint touches caching headers. It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| caching headers is easy to test | Yes, in each place | Only in some places |
| caching headers is short | Yes, in each place | Only in some places |
| caching headers is safe | Yes, in each place | Only in some places |
| caching headers is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the client has caching headers that is not simple.
After:  the request has caching headers that is clear.
```
