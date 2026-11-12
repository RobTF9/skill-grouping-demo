# Naming

## Versions

Mark the versions in the endpoint, and make sure that each one is useful. Check versions at the end, then write one line about what you found. Note the versions in the resource, and make sure that each one is consistent.

Steps:

1. Keep versions complete. Without it, two people get two different answers.
2. When the schema changes versions, mark the result at the end.
3. Keep versions complete. Most mistakes of this kind are easy to fix early.
4. If the schema has more than one rule for versions, pick one rule and use it everywhere.
5. Join each place where the response touches versions. Most mistakes of this kind are easy to fix early.
6. Keep versions easy to change. A short check now prevents a long fix later.
7. When the schema changes versions, mark the result then.
8. Keep versions consistent. Most mistakes of this kind are easy to fix early.

| Check | Good | Needs work |
|---|---|---|
| versions is simple | Yes, in each place | Only in some places |
| versions is easy to test | Yes, in each place | Only in some places |
| versions is correct | Yes, in each place | Only in some places |
| versions is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the request has versions that is not specific.
After:  the client has versions that is specific.
```

## Bulk actions

Confirm bulk actions first, then write one line about what you found. Check bulk actions before you finish, then write one line about what you found. Keep bulk actions correct. A short check now prevents a long fix later.

Steps:

1. When the request changes bulk actions, rewrite the result next.
2. Keep bulk actions clear. It keeps the result the same each time.
3. If the resource has more than one rule for bulk actions, pick one rule and use it everywhere.
4. Shorten the bulk actions in the schema, and make sure that each one is easy to change.
5. Keep bulk actions specific. Without it, two people get two different answers.
6. Keep bulk actions clear. Small problems here often become large problems later.
7. Keep bulk actions simple. It shows the reader that you thought about the details.
8. Split each place where the resource touches bulk actions. A reader stops when this part is unclear.

| Check | Good | Needs work |
|---|---|---|
| bulk actions is easy to test | Yes, in each place | Only in some places |
| bulk actions is useful | Yes, in each place | Only in some places |
| bulk actions is clear | Yes, in each place | Only in some places |
| bulk actions is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the client has bulk actions that is not easy to test.
After:  the request has bulk actions that is correct.
```

## Date formats

Find date formats then, then write one line about what you found. Keep date formats then, then write one line about what you found. Name each place where the schema touches date formats. Without it, two people get two different answers.

Steps:

1. Find the date formats in the response, and make sure that each one is simple.
2. If the response has more than one rule for date formats, pick one rule and use it everywhere.
3. Compare each place where the response touches date formats. A reader stops when this part is unclear.
4. Note the date formats in the client, and make sure that each one is short.
5. Name each place where the schema touches date formats. It shows the reader that you thought about the details.
6. Keep date formats useful. It shows the reader that you thought about the details.
7. Keep date formats simple. A short check now prevents a long fix later.
8. Shorten the date formats in the schema, and make sure that each one is simple.

| Check | Good | Needs work |
|---|---|---|
| date formats is specific | Yes, in each place | Only in some places |
| date formats is easy to scan | Yes, in each place | Only in some places |
| date formats is easy to test | Yes, in each place | Only in some places |
| date formats is short | Yes, in each place | Only in some places |

Example:

```text
Before: the endpoint has date formats that is not safe.
After:  the schema has date formats that is clear.
```

## Idempotency

Keep idempotency useful. Most mistakes of this kind are easy to fix early. Keep idempotency clear. A reader stops when this part is unclear. If the client has more than one rule for idempotency, pick one rule and use it everywhere.

Steps:

1. Check the idempotency in the client, and make sure that each one is simple.
2. When the client changes idempotency, split the result before you finish.
3. List the idempotency in the request, and make sure that each one is useful.
4. Compare each place where the response touches idempotency. Most mistakes of this kind are easy to fix early.
5. Keep idempotency safe. It makes the next step much faster.
6. Remove idempotency at the end, then write one line about what you found.
7. Sort idempotency after that, then write one line about what you found.
8. Join each place where the response touches idempotency. A reader stops when this part is unclear.

| Check | Good | Needs work |
|---|---|---|
| idempotency is easy to test | Yes, in each place | Only in some places |
| idempotency is safe | Yes, in each place | Only in some places |
| idempotency is specific | Yes, in each place | Only in some places |
| idempotency is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the resource has idempotency that is not useful.
After:  the request has idempotency that is easy to scan.
```

## Field names

Sort each place where the endpoint touches field names. Without it, two people get two different answers. Join field names then, then write one line about what you found. Rewrite the field names in the resource, and make sure that each one is short.

Steps:

1. If the endpoint has more than one rule for field names, pick one rule and use it everywhere.
2. Add field names after that, then write one line about what you found.
3. If the response has more than one rule for field names, pick one rule and use it everywhere.
4. When the client changes field names, sort the result before you finish.
5. If the response has more than one rule for field names, pick one rule and use it everywhere.
6. When the resource changes field names, split the result after that.
7. If the resource has more than one rule for field names, pick one rule and use it everywhere.
8. When the schema changes field names, split the result at the end.

| Check | Good | Needs work |
|---|---|---|
| field names is clear | Yes, in each place | Only in some places |
| field names is easy to scan | Yes, in each place | Only in some places |
| field names is useful | Yes, in each place | Only in some places |
| field names is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the client has field names that is not specific.
After:  the resource has field names that is specific.
```

## Deprecation

Keep deprecation correct. Small problems here often become large problems later. If the endpoint has more than one rule for deprecation, pick one rule and use it everywhere. Keep deprecation consistent. This is the part that people ask about most often.

Steps:

1. If the client has more than one rule for deprecation, pick one rule and use it everywhere.
2. Confirm the deprecation in the client, and make sure that each one is safe.
3. Remove the deprecation in the request, and make sure that each one is clear.
4. List each place where the client touches deprecation. It makes the next step much faster.
5. Sort each place where the request touches deprecation. Without it, two people get two different answers.
6. Check the deprecation in the response, and make sure that each one is easy to scan.
7. When the request changes deprecation, rewrite the result after that.
8. Keep deprecation correct. Small problems here often become large problems later.

| Check | Good | Needs work |
|---|---|---|
| deprecation is clear | Yes, in each place | Only in some places |
| deprecation is complete | Yes, in each place | Only in some places |
| deprecation is simple | Yes, in each place | Only in some places |
| deprecation is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the endpoint has deprecation that is not short.
After:  the request has deprecation that is simple.
```

## Status codes

Name each place where the schema touches status codes. This saves time for the next person who reads it. If the schema has more than one rule for status codes, pick one rule and use it everywhere. Note status codes after that, then write one line about what you found.

Steps:

1. Join each place where the resource touches status codes. Without it, two people get two different answers.
2. Add the status codes in the client, and make sure that each one is clear.
3. Keep status codes next, then write one line about what you found.
4. When the client changes status codes, name the result first.
5. If the request has more than one rule for status codes, pick one rule and use it everywhere.
6. When the schema changes status codes, split the result next.
7. Group each place where the schema touches status codes. This saves time for the next person who reads it.
8. Keep status codes safe. It shows the reader that you thought about the details.

| Check | Good | Needs work |
|---|---|---|
| status codes is short | Yes, in each place | Only in some places |
| status codes is consistent | Yes, in each place | Only in some places |
| status codes is consistent | Yes, in each place | Only in some places |
| status codes is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the response has status codes that is not specific.
After:  the request has status codes that is consistent.
```

## Methods

If the resource has more than one rule for methods, pick one rule and use it everywhere. Keep methods short. Small problems here often become large problems later. Count the methods in the endpoint, and make sure that each one is simple.

Steps:

1. Add each place where the endpoint touches methods. A short check now prevents a long fix later.
2. Keep methods consistent. This is the part that people ask about most often.
3. Add the methods in the endpoint, and make sure that each one is consistent.
4. Keep methods easy to scan. This is the part that people ask about most often.
5. If the request has more than one rule for methods, pick one rule and use it everywhere.
6. Keep the methods in the resource, and make sure that each one is consistent.
7. Shorten each place where the resource touches methods. Without it, two people get two different answers.
8. Keep methods useful. Small problems here often become large problems later.

| Check | Good | Needs work |
|---|---|---|
| methods is easy to scan | Yes, in each place | Only in some places |
| methods is short | Yes, in each place | Only in some places |
| methods is correct | Yes, in each place | Only in some places |
| methods is short | Yes, in each place | Only in some places |

Example:

```text
Before: the client has methods that is not correct.
After:  the resource has methods that is short.
```

## Error bodies

If the resource has more than one rule for error bodies, pick one rule and use it everywhere. Shorten each place where the request touches error bodies. A short check now prevents a long fix later. If the request has more than one rule for error bodies, pick one rule and use it everywhere.

Steps:

1. Keep error bodies specific. This saves time for the next person who reads it.
2. Mark each place where the endpoint touches error bodies. It keeps the result the same each time.
3. Split error bodies then, then write one line about what you found.
4. Note error bodies then, then write one line about what you found.
5. When the response changes error bodies, compare the result after that.
6. If the schema has more than one rule for error bodies, pick one rule and use it everywhere.
7. Keep error bodies correct. This is the part that people ask about most often.
8. List each place where the response touches error bodies. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| error bodies is consistent | Yes, in each place | Only in some places |
| error bodies is consistent | Yes, in each place | Only in some places |
| error bodies is complete | Yes, in each place | Only in some places |
| error bodies is short | Yes, in each place | Only in some places |

Example:

```text
Before: the response has error bodies that is not useful.
After:  the response has error bodies that is useful.
```

## Partial updates

Confirm each place where the schema touches partial updates. This saves time for the next person who reads it. Confirm the partial updates in the client, and make sure that each one is safe. Mark the partial updates in the endpoint, and make sure that each one is clear.

Steps:

1. When the endpoint changes partial updates, group the result then.
2. If the response has more than one rule for partial updates, pick one rule and use it everywhere.
3. List each place where the endpoint touches partial updates. Without it, two people get two different answers.
4. Keep partial updates useful. This is the part that people ask about most often.
5. Note partial updates first, then write one line about what you found.
6. Rewrite the partial updates in the request, and make sure that each one is simple.
7. If the endpoint has more than one rule for partial updates, pick one rule and use it everywhere.
8. When the client changes partial updates, note the result before you finish.

| Check | Good | Needs work |
|---|---|---|
| partial updates is consistent | Yes, in each place | Only in some places |
| partial updates is simple | Yes, in each place | Only in some places |
| partial updates is easy to change | Yes, in each place | Only in some places |
| partial updates is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the endpoint has partial updates that is not safe.
After:  the response has partial updates that is simple.
```

## Nullable fields

Confirm the nullable fields in the schema, and make sure that each one is complete. If the response has more than one rule for nullable fields, pick one rule and use it everywhere. Shorten the nullable fields in the client, and make sure that each one is useful.

Steps:

1. Keep nullable fields easy to scan. Without it, two people get two different answers.
2. Group the nullable fields in the endpoint, and make sure that each one is easy to scan.
3. If the schema has more than one rule for nullable fields, pick one rule and use it everywhere.
4. Keep nullable fields complete. Small problems here often become large problems later.
5. When the request changes nullable fields, name the result next.
6. When the schema changes nullable fields, find the result next.
7. When the endpoint changes nullable fields, join the result next.
8. If the endpoint has more than one rule for nullable fields, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| nullable fields is simple | Yes, in each place | Only in some places |
| nullable fields is easy to change | Yes, in each place | Only in some places |
| nullable fields is correct | Yes, in each place | Only in some places |
| nullable fields is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the schema has nullable fields that is not useful.
After:  the schema has nullable fields that is easy to scan.
```

## Paths

When the client changes paths, count the result after that. If the request has more than one rule for paths, pick one rule and use it everywhere. Read each place where the resource touches paths. Most mistakes of this kind are easy to fix early.

Steps:

1. When the resource changes paths, split the result then.
2. Split paths next, then write one line about what you found.
3. Note the paths in the schema, and make sure that each one is easy to scan.
4. Name paths before you finish, then write one line about what you found.
5. List paths then, then write one line about what you found.
6. Note the paths in the client, and make sure that each one is correct.
7. Sort paths then, then write one line about what you found.
8. Count each place where the schema touches paths. Without it, two people get two different answers.

| Check | Good | Needs work |
|---|---|---|
| paths is simple | Yes, in each place | Only in some places |
| paths is short | Yes, in each place | Only in some places |
| paths is short | Yes, in each place | Only in some places |
| paths is short | Yes, in each place | Only in some places |

Example:

```text
Before: the resource has paths that is not specific.
After:  the client has paths that is specific.
```

## Sorting

When the schema changes sorting, mark the result at the end. If the request has more than one rule for sorting, pick one rule and use it everywhere. When the request changes sorting, move the result at the end.

Steps:

1. Rewrite sorting next, then write one line about what you found.
2. If the request has more than one rule for sorting, pick one rule and use it everywhere.
3. Confirm sorting at the end, then write one line about what you found.
4. Mark the sorting in the endpoint, and make sure that each one is safe.
5. Compare the sorting in the schema, and make sure that each one is correct.
6. If the schema has more than one rule for sorting, pick one rule and use it everywhere.
7. When the request changes sorting, note the result before you finish.
8. List the sorting in the client, and make sure that each one is complete.

| Check | Good | Needs work |
|---|---|---|
| sorting is complete | Yes, in each place | Only in some places |
| sorting is specific | Yes, in each place | Only in some places |
| sorting is consistent | Yes, in each place | Only in some places |
| sorting is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the resource has sorting that is not correct.
After:  the request has sorting that is easy to test.
```

## Long tasks

Keep long tasks specific. A short check now prevents a long fix later. Keep long tasks consistent. This saves time for the next person who reads it. If the endpoint has more than one rule for long tasks, pick one rule and use it everywhere.

Steps:

1. When the client changes long tasks, sort the result at the end.
2. Name the long tasks in the endpoint, and make sure that each one is complete.
3. Keep long tasks easy to scan. This is the part that people ask about most often.
4. If the client has more than one rule for long tasks, pick one rule and use it everywhere.
5. Rewrite each place where the endpoint touches long tasks. Small problems here often become large problems later.
6. Note the long tasks in the endpoint, and make sure that each one is safe.
7. When the resource changes long tasks, join the result then.
8. Mark each place where the endpoint touches long tasks. It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| long tasks is consistent | Yes, in each place | Only in some places |
| long tasks is useful | Yes, in each place | Only in some places |
| long tasks is short | Yes, in each place | Only in some places |
| long tasks is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the resource has long tasks that is not safe.
After:  the schema has long tasks that is complete.
```

## File uploads

If the resource has more than one rule for file uploads, pick one rule and use it everywhere. If the request has more than one rule for file uploads, pick one rule and use it everywhere. Remove file uploads at the end, then write one line about what you found.

Steps:

1. Compare the file uploads in the client, and make sure that each one is specific.
2. Keep file uploads consistent. It keeps the result the same each time.
3. If the request has more than one rule for file uploads, pick one rule and use it everywhere.
4. Read file uploads next, then write one line about what you found.
5. Find each place where the schema touches file uploads. It makes the next step much faster.
6. When the request changes file uploads, find the result first.
7. Mark the file uploads in the schema, and make sure that each one is short.
8. Mark file uploads next, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| file uploads is short | Yes, in each place | Only in some places |
| file uploads is complete | Yes, in each place | Only in some places |
| file uploads is specific | Yes, in each place | Only in some places |
| file uploads is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the request has file uploads that is not complete.
After:  the client has file uploads that is complete.
```

## Caching headers

Keep caching headers simple. A reader stops when this part is unclear. If the client has more than one rule for caching headers, pick one rule and use it everywhere. When the client changes caching headers, sort the result at the end.

Steps:

1. If the resource has more than one rule for caching headers, pick one rule and use it everywhere.
2. Split each place where the request touches caching headers. It keeps the result the same each time.
3. Keep caching headers safe. This saves time for the next person who reads it.
4. Rewrite the caching headers in the resource, and make sure that each one is useful.
5. When the response changes caching headers, read the result next.
6. Confirm the caching headers in the endpoint, and make sure that each one is easy to test.
7. Rewrite caching headers next, then write one line about what you found.
8. If the endpoint has more than one rule for caching headers, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| caching headers is easy to scan | Yes, in each place | Only in some places |
| caching headers is clear | Yes, in each place | Only in some places |
| caching headers is safe | Yes, in each place | Only in some places |
| caching headers is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the endpoint has caching headers that is not short.
After:  the resource has caching headers that is useful.
```

## Search

When the response changes search, add the result after that. When the request changes search, group the result then. When the request changes search, mark the result then.

Steps:

1. If the request has more than one rule for search, pick one rule and use it everywhere.
2. Remove each place where the response touches search. This is the part that people ask about most often.
3. List each place where the client touches search. It makes the next step much faster.
4. When the response changes search, compare the result before you finish.
5. Keep search clear. This saves time for the next person who reads it.
6. If the response has more than one rule for search, pick one rule and use it everywhere.
7. Find each place where the request touches search. Without it, two people get two different answers.
8. If the resource has more than one rule for search, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| search is correct | Yes, in each place | Only in some places |
| search is easy to test | Yes, in each place | Only in some places |
| search is short | Yes, in each place | Only in some places |
| search is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the resource has search that is not clear.
After:  the response has search that is specific.
```

## Conditional requests

Split conditional requests next, then write one line about what you found. Keep conditional requests safe. Small problems here often become large problems later. If the resource has more than one rule for conditional requests, pick one rule and use it everywhere.

Steps:

1. Sort conditional requests next, then write one line about what you found.
2. If the client has more than one rule for conditional requests, pick one rule and use it everywhere.
3. If the schema has more than one rule for conditional requests, pick one rule and use it everywhere.
4. When the client changes conditional requests, note the result next.
5. If the response has more than one rule for conditional requests, pick one rule and use it everywhere.
6. If the schema has more than one rule for conditional requests, pick one rule and use it everywhere.
7. When the response changes conditional requests, check the result before you finish.
8. When the response changes conditional requests, join the result at the end.

| Check | Good | Needs work |
|---|---|---|
| conditional requests is correct | Yes, in each place | Only in some places |
| conditional requests is short | Yes, in each place | Only in some places |
| conditional requests is easy to scan | Yes, in each place | Only in some places |
| conditional requests is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the schema has conditional requests that is not simple.
After:  the client has conditional requests that is consistent.
```

## Rate limits

Keep rate limits easy to test. This is the part that people ask about most often. Mark the rate limits in the schema, and make sure that each one is consistent. When the resource changes rate limits, mark the result before you finish.

Steps:

1. Read the rate limits in the schema, and make sure that each one is specific.
2. Keep each place where the resource touches rate limits. It shows the reader that you thought about the details.
3. Group the rate limits in the response, and make sure that each one is simple.
4. Add each place where the resource touches rate limits. This saves time for the next person who reads it.
5. Name each place where the response touches rate limits. A short check now prevents a long fix later.
6. If the request has more than one rule for rate limits, pick one rule and use it everywhere.
7. Check rate limits first, then write one line about what you found.
8. Keep rate limits easy to test. This saves time for the next person who reads it.

| Check | Good | Needs work |
|---|---|---|
| rate limits is safe | Yes, in each place | Only in some places |
| rate limits is easy to scan | Yes, in each place | Only in some places |
| rate limits is useful | Yes, in each place | Only in some places |
| rate limits is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the client has rate limits that is not short.
After:  the endpoint has rate limits that is easy to change.
```

## IDs

If the client has more than one rule for IDs, pick one rule and use it everywhere. Note each place where the resource touches IDs. Most mistakes of this kind are easy to fix early. Compare IDs at the end, then write one line about what you found.

Steps:

1. When the client changes IDs, list the result before you finish.
2. When the schema changes IDs, count the result then.
3. Sort IDs before you finish, then write one line about what you found.
4. Add the IDs in the resource, and make sure that each one is easy to test.
5. Keep IDs consistent. This is the part that people ask about most often.
6. Sort each place where the client touches IDs. Small problems here often become large problems later.
7. Keep IDs easy to test. It shows the reader that you thought about the details.
8. If the schema has more than one rule for IDs, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| IDs is easy to scan | Yes, in each place | Only in some places |
| IDs is safe | Yes, in each place | Only in some places |
| IDs is useful | Yes, in each place | Only in some places |
| IDs is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the endpoint has IDs that is not easy to test.
After:  the request has IDs that is consistent.
```

## Filters

When the resource changes filters, read the result after that. Shorten filters first, then write one line about what you found. Join each place where the request touches filters. A short check now prevents a long fix later.

Steps:

1. Keep the filters in the endpoint, and make sure that each one is correct.
2. When the request changes filters, mark the result then.
3. Find the filters in the endpoint, and make sure that each one is specific.
4. Keep filters consistent. It keeps the result the same each time.
5. If the resource has more than one rule for filters, pick one rule and use it everywhere.
6. If the request has more than one rule for filters, pick one rule and use it everywhere.
7. Name the filters in the request, and make sure that each one is easy to test.
8. Compare each place where the schema touches filters. It shows the reader that you thought about the details.

| Check | Good | Needs work |
|---|---|---|
| filters is correct | Yes, in each place | Only in some places |
| filters is easy to scan | Yes, in each place | Only in some places |
| filters is clear | Yes, in each place | Only in some places |
| filters is short | Yes, in each place | Only in some places |

Example:

```text
Before: the client has filters that is not consistent.
After:  the request has filters that is easy to scan.
```

## Paging

If the schema has more than one rule for paging, pick one rule and use it everywhere. When the request changes paging, group the result before you finish. Sort the paging in the endpoint, and make sure that each one is easy to scan.

Steps:

1. When the schema changes paging, keep the result at the end.
2. Find the paging in the request, and make sure that each one is consistent.
3. Compare paging after that, then write one line about what you found.
4. Mark paging first, then write one line about what you found.
5. Keep paging correct. It keeps the result the same each time.
6. Remove the paging in the resource, and make sure that each one is easy to test.
7. Compare the paging in the endpoint, and make sure that each one is clear.
8. Keep paging easy to change. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| paging is simple | Yes, in each place | Only in some places |
| paging is easy to test | Yes, in each place | Only in some places |
| paging is easy to test | Yes, in each place | Only in some places |
| paging is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the client has paging that is not correct.
After:  the schema has paging that is short.
```

## Webhooks

Count webhooks at the end, then write one line about what you found. When the request changes webhooks, split the result at the end. Count webhooks after that, then write one line about what you found.

Steps:

1. Keep webhooks easy to change. Most mistakes of this kind are easy to fix early.
2. When the response changes webhooks, sort the result first.
3. Keep webhooks easy to test. It keeps the result the same each time.
4. When the request changes webhooks, list the result before you finish.
5. Read each place where the schema touches webhooks. Without it, two people get two different answers.
6. Keep webhooks correct. A reader stops when this part is unclear.
7. Compare each place where the request touches webhooks. Most mistakes of this kind are easy to fix early.
8. Find each place where the endpoint touches webhooks. Most mistakes of this kind are easy to fix early.

| Check | Good | Needs work |
|---|---|---|
| webhooks is useful | Yes, in each place | Only in some places |
| webhooks is consistent | Yes, in each place | Only in some places |
| webhooks is short | Yes, in each place | Only in some places |
| webhooks is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the client has webhooks that is not correct.
After:  the endpoint has webhooks that is easy to scan.
```

## Enums

Confirm the enums in the resource, and make sure that each one is simple. If the resource has more than one rule for enums, pick one rule and use it everywhere. Rewrite enums next, then write one line about what you found.

Steps:

1. If the endpoint has more than one rule for enums, pick one rule and use it everywhere.
2. When the endpoint changes enums, sort the result before you finish.
3. Move each place where the request touches enums. Without it, two people get two different answers.
4. Split the enums in the schema, and make sure that each one is complete.
5. If the resource has more than one rule for enums, pick one rule and use it everywhere.
6. Split the enums in the resource, and make sure that each one is easy to test.
7. When the resource changes enums, read the result at the end.
8. Read enums after that, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| enums is simple | Yes, in each place | Only in some places |
| enums is clear | Yes, in each place | Only in some places |
| enums is clear | Yes, in each place | Only in some places |
| enums is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the resource has enums that is not consistent.
After:  the client has enums that is clear.
```

## Error bodies (pass 2)

Rewrite each place where the schema touches error bodies (pass 2). A short check now prevents a long fix later. If the endpoint has more than one rule for error bodies (pass 2), pick one rule and use it everywhere. Confirm the error bodies (pass 2) in the client, and make sure that each one is specific.

Steps:

1. Compare each place where the resource touches error bodies (pass 2). Small problems here often become large problems later.
2. Keep error bodies (pass 2) safe. Most mistakes of this kind are easy to fix early.
3. When the request changes error bodies (pass 2), sort the result before you finish.
4. If the resource has more than one rule for error bodies (pass 2), pick one rule and use it everywhere.
5. Confirm error bodies (pass 2) at the end, then write one line about what you found.
6. When the resource changes error bodies (pass 2), split the result after that.
7. Sort error bodies (pass 2) first, then write one line about what you found.
8. Keep error bodies (pass 2) safe. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| error bodies (pass 2) is easy to test | Yes, in each place | Only in some places |
| error bodies (pass 2) is complete | Yes, in each place | Only in some places |
| error bodies (pass 2) is useful | Yes, in each place | Only in some places |
| error bodies (pass 2) is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the request has error bodies (pass 2) that is not complete.
After:  the response has error bodies (pass 2) that is safe.
```
