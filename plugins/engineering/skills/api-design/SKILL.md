---
name: api-design
description: Design a REST endpoint with its path, method, status codes and errors.
---

# API design

Design the endpoint before you write code. Write the design as a short table, then the examples.

## Versions

If the request has more than one rule for versions, pick one rule and use it everywhere. Compare each place where the request touches versions. Most mistakes of this kind are easy to fix early. If the response has more than one rule for versions, pick one rule and use it everywhere.

Steps:

1. Count the versions in the schema, and make sure that each one is consistent.
2. Check the versions in the schema, and make sure that each one is specific.
3. If the endpoint has more than one rule for versions, pick one rule and use it everywhere.
4. When the resource changes versions, add the result next.
5. Keep versions specific. A short check now prevents a long fix later.
6. If the schema has more than one rule for versions, pick one rule and use it everywhere.
7. Keep versions specific. Without it, two people get two different answers.
8. Mark versions first, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| versions is easy to scan | Yes, in each place | Only in some places |
| versions is simple | Yes, in each place | Only in some places |
| versions is easy to change | Yes, in each place | Only in some places |
| versions is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the resource has versions that is not correct.
After:  the schema has versions that is short.
```

## IDs

List IDs at the end, then write one line about what you found. Keep each place where the client touches IDs. A short check now prevents a long fix later. Keep IDs consistent. Small problems here often become large problems later.

Steps:

1. Group each place where the response touches IDs. This saves time for the next person who reads it.
2. If the schema has more than one rule for IDs, pick one rule and use it everywhere.
3. Compare the IDs in the schema, and make sure that each one is clear.
4. If the endpoint has more than one rule for IDs, pick one rule and use it everywhere.
5. Keep IDs correct. It shows the reader that you thought about the details.
6. Check the IDs in the schema, and make sure that each one is useful.
7. When the schema changes IDs, name the result then.
8. If the resource has more than one rule for IDs, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| IDs is complete | Yes, in each place | Only in some places |
| IDs is useful | Yes, in each place | Only in some places |
| IDs is complete | Yes, in each place | Only in some places |
| IDs is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the endpoint has IDs that is not simple.
After:  the response has IDs that is complete.
```

## Long tasks

Keep long tasks correct. It keeps the result the same each time. Check the long tasks in the resource, and make sure that each one is correct. If the request has more than one rule for long tasks, pick one rule and use it everywhere.

Steps:

1. Sort each place where the resource touches long tasks. A short check now prevents a long fix later.
2. Find each place where the client touches long tasks. It shows the reader that you thought about the details.
3. Split each place where the response touches long tasks. Most mistakes of this kind are easy to fix early.
4. Keep long tasks correct. A short check now prevents a long fix later.
5. List long tasks at the end, then write one line about what you found.
6. If the endpoint has more than one rule for long tasks, pick one rule and use it everywhere.
7. Rewrite each place where the response touches long tasks. This is the part that people ask about most often.
8. If the response has more than one rule for long tasks, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| long tasks is easy to test | Yes, in each place | Only in some places |
| long tasks is simple | Yes, in each place | Only in some places |
| long tasks is easy to change | Yes, in each place | Only in some places |
| long tasks is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the resource has long tasks that is not easy to test.
After:  the client has long tasks that is easy to change.
```

## Field names

Keep field names correct. Small problems here often become large problems later. When the request changes field names, keep the result at the end. If the schema has more than one rule for field names, pick one rule and use it everywhere.

Steps:

1. When the schema changes field names, list the result then.
2. Keep field names easy to change. It shows the reader that you thought about the details.
3. Add field names before you finish, then write one line about what you found.
4. Keep field names simple. Small problems here often become large problems later.
5. Note each place where the schema touches field names. It shows the reader that you thought about the details.
6. Shorten each place where the resource touches field names. It shows the reader that you thought about the details.
7. Move the field names in the request, and make sure that each one is easy to scan.
8. If the client has more than one rule for field names, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| field names is easy to test | Yes, in each place | Only in some places |
| field names is correct | Yes, in each place | Only in some places |
| field names is useful | Yes, in each place | Only in some places |
| field names is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the schema has field names that is not specific.
After:  the schema has field names that is specific.
```

## Filters

When the schema changes filters, rewrite the result after that. Mark the filters in the endpoint, and make sure that each one is consistent. Keep filters simple. It shows the reader that you thought about the details.

Steps:

1. Keep filters simple. This saves time for the next person who reads it.
2. Split the filters in the resource, and make sure that each one is easy to change.
3. Find the filters in the response, and make sure that each one is correct.
4. Keep filters before you finish, then write one line about what you found.
5. If the client has more than one rule for filters, pick one rule and use it everywhere.
6. Join each place where the schema touches filters. Without it, two people get two different answers.
7. Join each place where the resource touches filters. It keeps the result the same each time.
8. Keep the filters in the resource, and make sure that each one is easy to test.

| Check | Good | Needs work |
|---|---|---|
| filters is easy to change | Yes, in each place | Only in some places |
| filters is short | Yes, in each place | Only in some places |
| filters is easy to change | Yes, in each place | Only in some places |
| filters is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the client has filters that is not safe.
After:  the response has filters that is simple.
```

## Paging

Keep paging complete. This saves time for the next person who reads it. When the request changes paging, group the result then. Keep paging useful. A short check now prevents a long fix later.

Steps:

1. When the response changes paging, sort the result next.
2. Group each place where the response touches paging. A reader stops when this part is unclear.
3. Remove each place where the response touches paging. This is the part that people ask about most often.
4. If the request has more than one rule for paging, pick one rule and use it everywhere.
5. Find each place where the client touches paging. Most mistakes of this kind are easy to fix early.
6. When the request changes paging, remove the result before you finish.
7. When the resource changes paging, check the result at the end.
8. If the endpoint has more than one rule for paging, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| paging is safe | Yes, in each place | Only in some places |
| paging is simple | Yes, in each place | Only in some places |
| paging is correct | Yes, in each place | Only in some places |
| paging is short | Yes, in each place | Only in some places |

Example:

```text
Before: the endpoint has paging that is not useful.
After:  the client has paging that is clear.
```

## Sorting

Keep sorting useful. It keeps the result the same each time. Move each place where the schema touches sorting. Small problems here often become large problems later. Keep sorting correct. This is the part that people ask about most often.

Steps:

1. Count the sorting in the request, and make sure that each one is easy to change.
2. Keep each place where the client touches sorting. A short check now prevents a long fix later.
3. Keep sorting specific. Without it, two people get two different answers.
4. Remove sorting first, then write one line about what you found.
5. Name the sorting in the resource, and make sure that each one is clear.
6. When the response changes sorting, confirm the result after that.
7. Sort each place where the client touches sorting. A reader stops when this part is unclear.
8. Check sorting next, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| sorting is clear | Yes, in each place | Only in some places |
| sorting is simple | Yes, in each place | Only in some places |
| sorting is simple | Yes, in each place | Only in some places |
| sorting is short | Yes, in each place | Only in some places |

Example:

```text
Before: the response has sorting that is not short.
After:  the endpoint has sorting that is easy to test.
```

## Error bodies

Move each place where the request touches error bodies. Most mistakes of this kind are easy to fix early. Keep error bodies specific. Small problems here often become large problems later. If the client has more than one rule for error bodies, pick one rule and use it everywhere.

Steps:

1. Group the error bodies in the response, and make sure that each one is consistent.
2. Check the error bodies in the response, and make sure that each one is consistent.
3. When the resource changes error bodies, name the result next.
4. Keep error bodies correct. This is the part that people ask about most often.
5. Join error bodies next, then write one line about what you found.
6. Name the error bodies in the endpoint, and make sure that each one is clear.
7. If the resource has more than one rule for error bodies, pick one rule and use it everywhere.
8. If the request has more than one rule for error bodies, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| error bodies is useful | Yes, in each place | Only in some places |
| error bodies is easy to scan | Yes, in each place | Only in some places |
| error bodies is short | Yes, in each place | Only in some places |
| error bodies is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the resource has error bodies that is not specific.
After:  the request has error bodies that is safe.
```

## File uploads

When the resource changes file uploads, find the result next. Confirm each place where the endpoint touches file uploads. Without it, two people get two different answers. Read file uploads after that, then write one line about what you found.

Steps:

1. When the client changes file uploads, keep the result before you finish.
2. Mark each place where the resource touches file uploads. Small problems here often become large problems later.
3. If the endpoint has more than one rule for file uploads, pick one rule and use it everywhere.
4. Name the file uploads in the client, and make sure that each one is simple.
5. Note file uploads after that, then write one line about what you found.
6. Add file uploads first, then write one line about what you found.
7. If the response has more than one rule for file uploads, pick one rule and use it everywhere.
8. Keep file uploads useful. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| file uploads is short | Yes, in each place | Only in some places |
| file uploads is simple | Yes, in each place | Only in some places |
| file uploads is useful | Yes, in each place | Only in some places |
| file uploads is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the response has file uploads that is not useful.
After:  the resource has file uploads that is complete.
```

## Methods

Keep methods correct. A short check now prevents a long fix later. Confirm the methods in the schema, and make sure that each one is complete. Mark each place where the request touches methods. It shows the reader that you thought about the details.

Steps:

1. If the response has more than one rule for methods, pick one rule and use it everywhere.
2. Mark methods next, then write one line about what you found.
3. Sort the methods in the resource, and make sure that each one is safe.
4. If the response has more than one rule for methods, pick one rule and use it everywhere.
5. Remove methods then, then write one line about what you found.
6. Sort the methods in the resource, and make sure that each one is clear.
7. When the schema changes methods, compare the result after that.
8. If the client has more than one rule for methods, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| methods is complete | Yes, in each place | Only in some places |
| methods is specific | Yes, in each place | Only in some places |
| methods is short | Yes, in each place | Only in some places |
| methods is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the endpoint has methods that is not easy to test.
After:  the schema has methods that is specific.
```

## Bulk actions

If the resource has more than one rule for bulk actions, pick one rule and use it everywhere. If the schema has more than one rule for bulk actions, pick one rule and use it everywhere. Rewrite the bulk actions in the schema, and make sure that each one is easy to test.

Steps:

1. Shorten the bulk actions in the client, and make sure that each one is easy to change.
2. When the endpoint changes bulk actions, split the result before you finish.
3. If the endpoint has more than one rule for bulk actions, pick one rule and use it everywhere.
4. Keep bulk actions easy to scan. Small problems here often become large problems later.
5. Keep bulk actions correct. Most mistakes of this kind are easy to fix early.
6. Add each place where the response touches bulk actions. Small problems here often become large problems later.
7. If the endpoint has more than one rule for bulk actions, pick one rule and use it everywhere.
8. When the schema changes bulk actions, rewrite the result at the end.

| Check | Good | Needs work |
|---|---|---|
| bulk actions is short | Yes, in each place | Only in some places |
| bulk actions is consistent | Yes, in each place | Only in some places |
| bulk actions is specific | Yes, in each place | Only in some places |
| bulk actions is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the client has bulk actions that is not short.
After:  the client has bulk actions that is specific.
```

## Search

Remove each place where the client touches search. Small problems here often become large problems later. Note the search in the client, and make sure that each one is safe. Join search before you finish, then write one line about what you found.

Steps:

1. Add the search in the response, and make sure that each one is consistent.
2. Count search before you finish, then write one line about what you found.
3. Find the search in the client, and make sure that each one is specific.
4. Keep search consistent. This saves time for the next person who reads it.
5. Keep each place where the schema touches search. This saves time for the next person who reads it.
6. Keep search safe. A reader stops when this part is unclear.
7. Confirm search after that, then write one line about what you found.
8. Count each place where the resource touches search. This saves time for the next person who reads it.

| Check | Good | Needs work |
|---|---|---|
| search is short | Yes, in each place | Only in some places |
| search is easy to change | Yes, in each place | Only in some places |
| search is safe | Yes, in each place | Only in some places |
| search is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the schema has search that is not safe.
After:  the client has search that is easy to test.
```

## Idempotency

Keep idempotency simple. Without it, two people get two different answers. List each place where the client touches idempotency. A reader stops when this part is unclear. Find idempotency after that, then write one line about what you found.

Steps:

1. Shorten idempotency after that, then write one line about what you found.
2. When the response changes idempotency, note the result after that.
3. Sort idempotency then, then write one line about what you found.
4. If the request has more than one rule for idempotency, pick one rule and use it everywhere.
5. If the schema has more than one rule for idempotency, pick one rule and use it everywhere.
6. If the response has more than one rule for idempotency, pick one rule and use it everywhere.
7. Find each place where the endpoint touches idempotency. Most mistakes of this kind are easy to fix early.
8. Check each place where the resource touches idempotency. It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| idempotency is complete | Yes, in each place | Only in some places |
| idempotency is specific | Yes, in each place | Only in some places |
| idempotency is short | Yes, in each place | Only in some places |
| idempotency is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the endpoint has idempotency that is not simple.
After:  the request has idempotency that is simple.
```

## Conditional requests

Check each place where the response touches conditional requests. Most mistakes of this kind are easy to fix early. If the schema has more than one rule for conditional requests, pick one rule and use it everywhere. Note the conditional requests in the resource, and make sure that each one is complete.

Steps:

1. When the request changes conditional requests, join the result at the end.
2. When the resource changes conditional requests, name the result at the end.
3. If the response has more than one rule for conditional requests, pick one rule and use it everywhere.
4. Split each place where the resource touches conditional requests. This is the part that people ask about most often.
5. Keep conditional requests easy to scan. Without it, two people get two different answers.
6. Keep conditional requests consistent. This saves time for the next person who reads it.
7. If the resource has more than one rule for conditional requests, pick one rule and use it everywhere.
8. Count the conditional requests in the response, and make sure that each one is consistent.

| Check | Good | Needs work |
|---|---|---|
| conditional requests is easy to test | Yes, in each place | Only in some places |
| conditional requests is consistent | Yes, in each place | Only in some places |
| conditional requests is correct | Yes, in each place | Only in some places |
| conditional requests is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the request has conditional requests that is not useful.
After:  the response has conditional requests that is easy to change.
```

## Nullable fields

When the endpoint changes nullable fields, confirm the result at the end. If the resource has more than one rule for nullable fields, pick one rule and use it everywhere. Keep nullable fields specific. A reader stops when this part is unclear.

Steps:

1. When the request changes nullable fields, find the result after that.
2. Keep nullable fields correct. It makes the next step much faster.
3. If the endpoint has more than one rule for nullable fields, pick one rule and use it everywhere.
4. Find the nullable fields in the request, and make sure that each one is easy to change.
5. Sort nullable fields then, then write one line about what you found.
6. When the request changes nullable fields, list the result at the end.
7. If the endpoint has more than one rule for nullable fields, pick one rule and use it everywhere.
8. If the resource has more than one rule for nullable fields, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| nullable fields is short | Yes, in each place | Only in some places |
| nullable fields is specific | Yes, in each place | Only in some places |
| nullable fields is useful | Yes, in each place | Only in some places |
| nullable fields is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the resource has nullable fields that is not easy to change.
After:  the response has nullable fields that is short.
```

## Deprecation

Join deprecation before you finish, then write one line about what you found. Count deprecation after that, then write one line about what you found. Keep deprecation consistent. Most mistakes of this kind are easy to fix early.

Steps:

1. When the response changes deprecation, rewrite the result first.
2. If the schema has more than one rule for deprecation, pick one rule and use it everywhere.
3. Move the deprecation in the client, and make sure that each one is simple.
4. Keep deprecation consistent. A short check now prevents a long fix later.
5. Keep deprecation complete. Small problems here often become large problems later.
6. When the endpoint changes deprecation, rewrite the result at the end.
7. When the request changes deprecation, keep the result after that.
8. Sort each place where the response touches deprecation. A reader stops when this part is unclear.

| Check | Good | Needs work |
|---|---|---|
| deprecation is consistent | Yes, in each place | Only in some places |
| deprecation is short | Yes, in each place | Only in some places |
| deprecation is clear | Yes, in each place | Only in some places |
| deprecation is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the schema has deprecation that is not complete.
After:  the response has deprecation that is clear.
```

## Date formats

Count the date formats in the schema, and make sure that each one is easy to test. If the response has more than one rule for date formats, pick one rule and use it everywhere. When the request changes date formats, remove the result next.

Steps:

1. Keep date formats consistent. It makes the next step much faster.
2. When the endpoint changes date formats, sort the result after that.
3. Check each place where the schema touches date formats. Small problems here often become large problems later.
4. Shorten each place where the resource touches date formats. Small problems here often become large problems later.
5. If the schema has more than one rule for date formats, pick one rule and use it everywhere.
6. Remove each place where the request touches date formats. Most mistakes of this kind are easy to fix early.
7. List the date formats in the resource, and make sure that each one is useful.
8. Sort date formats at the end, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| date formats is safe | Yes, in each place | Only in some places |
| date formats is correct | Yes, in each place | Only in some places |
| date formats is easy to test | Yes, in each place | Only in some places |
| date formats is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the client has date formats that is not short.
After:  the resource has date formats that is easy to scan.
```

## Caching headers

Note each place where the schema touches caching headers. Without it, two people get two different answers. When the resource changes caching headers, keep the result after that. Group each place where the client touches caching headers. A short check now prevents a long fix later.

Steps:

1. Confirm the caching headers in the response, and make sure that each one is clear.
2. Mark each place where the resource touches caching headers. Without it, two people get two different answers.
3. Rewrite each place where the request touches caching headers. It makes the next step much faster.
4. Mark the caching headers in the client, and make sure that each one is simple.
5. Count each place where the response touches caching headers. This is the part that people ask about most often.
6. Keep caching headers safe. Small problems here often become large problems later.
7. When the client changes caching headers, join the result then.
8. When the schema changes caching headers, compare the result first.

| Check | Good | Needs work |
|---|---|---|
| caching headers is clear | Yes, in each place | Only in some places |
| caching headers is clear | Yes, in each place | Only in some places |
| caching headers is easy to scan | Yes, in each place | Only in some places |
| caching headers is short | Yes, in each place | Only in some places |

Example:

```text
Before: the request has caching headers that is not easy to test.
After:  the schema has caching headers that is useful.
```

## Status codes

When the resource changes status codes, sort the result then. List each place where the response touches status codes. It keeps the result the same each time. When the schema changes status codes, split the result then.

Steps:

1. Keep status codes specific. It makes the next step much faster.
2. If the response has more than one rule for status codes, pick one rule and use it everywhere.
3. List each place where the request touches status codes. A reader stops when this part is unclear.
4. If the endpoint has more than one rule for status codes, pick one rule and use it everywhere.
5. Keep status codes correct. A short check now prevents a long fix later.
6. Move each place where the endpoint touches status codes. This saves time for the next person who reads it.
7. Keep status codes easy to change. A reader stops when this part is unclear.
8. Note the status codes in the client, and make sure that each one is easy to change.

| Check | Good | Needs work |
|---|---|---|
| status codes is useful | Yes, in each place | Only in some places |
| status codes is correct | Yes, in each place | Only in some places |
| status codes is safe | Yes, in each place | Only in some places |
| status codes is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the schema has status codes that is not useful.
After:  the response has status codes that is clear.
```

## Rate limits

If the resource has more than one rule for rate limits, pick one rule and use it everywhere. Add each place where the request touches rate limits. It makes the next step much faster. Sort rate limits after that, then write one line about what you found.

Steps:

1. Name rate limits before you finish, then write one line about what you found.
2. Keep each place where the response touches rate limits. Most mistakes of this kind are easy to fix early.
3. Move the rate limits in the request, and make sure that each one is easy to scan.
4. Remove rate limits at the end, then write one line about what you found.
5. Compare each place where the client touches rate limits. This is the part that people ask about most often.
6. Join each place where the schema touches rate limits. This is the part that people ask about most often.
7. Split the rate limits in the resource, and make sure that each one is easy to scan.
8. If the response has more than one rule for rate limits, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| rate limits is short | Yes, in each place | Only in some places |
| rate limits is safe | Yes, in each place | Only in some places |
| rate limits is complete | Yes, in each place | Only in some places |
| rate limits is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the request has rate limits that is not simple.
After:  the client has rate limits that is easy to change.
```

## Paths

Keep paths consistent. This saves time for the next person who reads it. Keep paths easy to change. Small problems here often become large problems later. Shorten each place where the response touches paths. Most mistakes of this kind are easy to fix early.

Steps:

1. Add paths next, then write one line about what you found.
2. Read paths after that, then write one line about what you found.
3. Name each place where the endpoint touches paths. It keeps the result the same each time.
4. Note paths after that, then write one line about what you found.
5. Count paths at the end, then write one line about what you found.
6. If the request has more than one rule for paths, pick one rule and use it everywhere.
7. When the request changes paths, split the result first.
8. Compare paths next, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| paths is consistent | Yes, in each place | Only in some places |
| paths is easy to test | Yes, in each place | Only in some places |
| paths is simple | Yes, in each place | Only in some places |
| paths is short | Yes, in each place | Only in some places |

Example:

```text
Before: the endpoint has paths that is not useful.
After:  the response has paths that is useful.
```

## Partial updates

Keep partial updates specific. A short check now prevents a long fix later. Keep partial updates correct. It shows the reader that you thought about the details. When the endpoint changes partial updates, move the result first.

Steps:

1. Keep partial updates complete. This saves time for the next person who reads it.
2. Keep partial updates useful. It shows the reader that you thought about the details.
3. Keep partial updates specific. Without it, two people get two different answers.
4. When the client changes partial updates, split the result before you finish.
5. When the request changes partial updates, confirm the result next.
6. Keep partial updates correct. It shows the reader that you thought about the details.
7. When the schema changes partial updates, count the result next.
8. Join partial updates at the end, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| partial updates is specific | Yes, in each place | Only in some places |
| partial updates is easy to change | Yes, in each place | Only in some places |
| partial updates is complete | Yes, in each place | Only in some places |
| partial updates is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the request has partial updates that is not consistent.
After:  the schema has partial updates that is safe.
```
