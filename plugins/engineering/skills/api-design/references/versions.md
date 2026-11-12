# Versions

## Search

Confirm each place where the client touches search. A reader stops when this part is unclear. Rewrite each place where the request touches search. It shows the reader that you thought about the details. Keep search simple. Small problems here often become large problems later.

Steps:

1. Confirm each place where the resource touches search. It makes the next step much faster.
2. If the client has more than one rule for search, pick one rule and use it everywhere.
3. Move search first, then write one line about what you found.
4. When the endpoint changes search, name the result at the end.
5. If the request has more than one rule for search, pick one rule and use it everywhere.
6. When the response changes search, count the result first.
7. Group search at the end, then write one line about what you found.
8. If the request has more than one rule for search, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| search is short | Yes, in each place | Only in some places |
| search is short | Yes, in each place | Only in some places |
| search is safe | Yes, in each place | Only in some places |
| search is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the endpoint has search that is not correct.
After:  the client has search that is clear.
```

## Long tasks

Keep long tasks easy to test. Small problems here often become large problems later. Shorten the long tasks in the response, and make sure that each one is easy to scan. Move each place where the endpoint touches long tasks. This saves time for the next person who reads it.

Steps:

1. Keep long tasks after that, then write one line about what you found.
2. When the endpoint changes long tasks, sort the result first.
3. Count the long tasks in the schema, and make sure that each one is easy to scan.
4. When the request changes long tasks, remove the result at the end.
5. Remove the long tasks in the request, and make sure that each one is clear.
6. Keep long tasks complete. A short check now prevents a long fix later.
7. If the client has more than one rule for long tasks, pick one rule and use it everywhere.
8. If the request has more than one rule for long tasks, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| long tasks is easy to test | Yes, in each place | Only in some places |
| long tasks is specific | Yes, in each place | Only in some places |
| long tasks is easy to change | Yes, in each place | Only in some places |
| long tasks is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the response has long tasks that is not consistent.
After:  the schema has long tasks that is clear.
```

## Error bodies

When the response changes error bodies, sort the result at the end. If the response has more than one rule for error bodies, pick one rule and use it everywhere. When the client changes error bodies, compare the result at the end.

Steps:

1. Note each place where the client touches error bodies. It keeps the result the same each time.
2. If the schema has more than one rule for error bodies, pick one rule and use it everywhere.
3. Rewrite the error bodies in the request, and make sure that each one is simple.
4. Move the error bodies in the request, and make sure that each one is correct.
5. Keep error bodies useful. A reader stops when this part is unclear.
6. Note error bodies then, then write one line about what you found.
7. If the request has more than one rule for error bodies, pick one rule and use it everywhere.
8. Move each place where the request touches error bodies. Small problems here often become large problems later.

| Check | Good | Needs work |
|---|---|---|
| error bodies is simple | Yes, in each place | Only in some places |
| error bodies is specific | Yes, in each place | Only in some places |
| error bodies is easy to test | Yes, in each place | Only in some places |
| error bodies is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the endpoint has error bodies that is not clear.
After:  the response has error bodies that is specific.
```

## Bulk actions

List each place where the resource touches bulk actions. It shows the reader that you thought about the details. Count each place where the endpoint touches bulk actions. A short check now prevents a long fix later. When the schema changes bulk actions, split the result next.

Steps:

1. When the resource changes bulk actions, list the result first.
2. Read the bulk actions in the schema, and make sure that each one is short.
3. Keep bulk actions correct. Small problems here often become large problems later.
4. Rewrite the bulk actions in the client, and make sure that each one is short.
5. Move each place where the schema touches bulk actions. It makes the next step much faster.
6. Keep bulk actions simple. Without it, two people get two different answers.
7. Keep bulk actions easy to test. It keeps the result the same each time.
8. Sort the bulk actions in the response, and make sure that each one is specific.

| Check | Good | Needs work |
|---|---|---|
| bulk actions is specific | Yes, in each place | Only in some places |
| bulk actions is easy to test | Yes, in each place | Only in some places |
| bulk actions is correct | Yes, in each place | Only in some places |
| bulk actions is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the endpoint has bulk actions that is not short.
After:  the resource has bulk actions that is short.
```

## Nullable fields

Keep nullable fields easy to change. It makes the next step much faster. Mark nullable fields after that, then write one line about what you found. Keep nullable fields first, then write one line about what you found.

Steps:

1. Keep nullable fields next, then write one line about what you found.
2. When the resource changes nullable fields, compare the result then.
3. When the client changes nullable fields, rewrite the result then.
4. Remove nullable fields after that, then write one line about what you found.
5. If the request has more than one rule for nullable fields, pick one rule and use it everywhere.
6. If the response has more than one rule for nullable fields, pick one rule and use it everywhere.
7. Count the nullable fields in the response, and make sure that each one is safe.
8. Sort each place where the response touches nullable fields. It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| nullable fields is easy to change | Yes, in each place | Only in some places |
| nullable fields is clear | Yes, in each place | Only in some places |
| nullable fields is specific | Yes, in each place | Only in some places |
| nullable fields is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the request has nullable fields that is not correct.
After:  the resource has nullable fields that is correct.
```

## Filters

Keep each place where the endpoint touches filters. This saves time for the next person who reads it. Sort each place where the client touches filters. Small problems here often become large problems later. When the endpoint changes filters, shorten the result after that.

Steps:

1. Name the filters in the request, and make sure that each one is simple.
2. Move each place where the schema touches filters. This saves time for the next person who reads it.
3. Keep filters specific. This is the part that people ask about most often.
4. Sort the filters in the endpoint, and make sure that each one is consistent.
5. Rewrite the filters in the endpoint, and make sure that each one is consistent.
6. Move filters after that, then write one line about what you found.
7. Mark filters next, then write one line about what you found.
8. Split filters next, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| filters is complete | Yes, in each place | Only in some places |
| filters is short | Yes, in each place | Only in some places |
| filters is easy to scan | Yes, in each place | Only in some places |
| filters is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the request has filters that is not complete.
After:  the response has filters that is easy to scan.
```

## Date formats

Compare each place where the endpoint touches date formats. This is the part that people ask about most often. Check the date formats in the endpoint, and make sure that each one is short. If the request has more than one rule for date formats, pick one rule and use it everywhere.

Steps:

1. Read date formats at the end, then write one line about what you found.
2. When the schema changes date formats, name the result after that.
3. Add each place where the client touches date formats. Most mistakes of this kind are easy to fix early.
4. Add each place where the client touches date formats. A reader stops when this part is unclear.
5. Keep date formats useful. A reader stops when this part is unclear.
6. Find date formats then, then write one line about what you found.
7. Mark the date formats in the endpoint, and make sure that each one is simple.
8. Check each place where the endpoint touches date formats. This saves time for the next person who reads it.

| Check | Good | Needs work |
|---|---|---|
| date formats is easy to test | Yes, in each place | Only in some places |
| date formats is clear | Yes, in each place | Only in some places |
| date formats is short | Yes, in each place | Only in some places |
| date formats is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the resource has date formats that is not safe.
After:  the resource has date formats that is useful.
```

## Rate limits

If the response has more than one rule for rate limits, pick one rule and use it everywhere. List the rate limits in the endpoint, and make sure that each one is complete. Sort rate limits next, then write one line about what you found.

Steps:

1. If the request has more than one rule for rate limits, pick one rule and use it everywhere.
2. Keep each place where the endpoint touches rate limits. This is the part that people ask about most often.
3. Check rate limits after that, then write one line about what you found.
4. List the rate limits in the request, and make sure that each one is short.
5. Count the rate limits in the request, and make sure that each one is short.
6. Check the rate limits in the client, and make sure that each one is correct.
7. Read the rate limits in the schema, and make sure that each one is short.
8. If the endpoint has more than one rule for rate limits, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| rate limits is simple | Yes, in each place | Only in some places |
| rate limits is correct | Yes, in each place | Only in some places |
| rate limits is easy to change | Yes, in each place | Only in some places |
| rate limits is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the client has rate limits that is not useful.
After:  the client has rate limits that is consistent.
```

## Methods

Keep methods easy to scan. A short check now prevents a long fix later. If the schema has more than one rule for methods, pick one rule and use it everywhere. If the resource has more than one rule for methods, pick one rule and use it everywhere.

Steps:

1. Keep methods easy to change. Most mistakes of this kind are easy to fix early.
2. When the endpoint changes methods, shorten the result first.
3. Compare each place where the schema touches methods. Without it, two people get two different answers.
4. Keep methods specific. It makes the next step much faster.
5. Keep methods easy to test. This is the part that people ask about most often.
6. Note each place where the schema touches methods. It makes the next step much faster.
7. Find methods then, then write one line about what you found.
8. Keep methods correct. A short check now prevents a long fix later.

| Check | Good | Needs work |
|---|---|---|
| methods is correct | Yes, in each place | Only in some places |
| methods is easy to test | Yes, in each place | Only in some places |
| methods is specific | Yes, in each place | Only in some places |
| methods is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the resource has methods that is not useful.
After:  the endpoint has methods that is consistent.
```

## Deprecation

Keep deprecation simple. Without it, two people get two different answers. Add the deprecation in the schema, and make sure that each one is correct. Count deprecation then, then write one line about what you found.

Steps:

1. If the resource has more than one rule for deprecation, pick one rule and use it everywhere.
2. If the resource has more than one rule for deprecation, pick one rule and use it everywhere.
3. Mark each place where the client touches deprecation. This saves time for the next person who reads it.
4. When the response changes deprecation, remove the result at the end.
5. When the request changes deprecation, confirm the result before you finish.
6. Add deprecation after that, then write one line about what you found.
7. Compare each place where the schema touches deprecation. Most mistakes of this kind are easy to fix early.
8. Check each place where the client touches deprecation. Most mistakes of this kind are easy to fix early.

| Check | Good | Needs work |
|---|---|---|
| deprecation is safe | Yes, in each place | Only in some places |
| deprecation is easy to test | Yes, in each place | Only in some places |
| deprecation is specific | Yes, in each place | Only in some places |
| deprecation is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the client has deprecation that is not easy to change.
After:  the client has deprecation that is simple.
```

## Enums

Keep enums simple. It makes the next step much faster. Add the enums in the schema, and make sure that each one is useful. Keep enums short. This saves time for the next person who reads it.

Steps:

1. If the client has more than one rule for enums, pick one rule and use it everywhere.
2. If the endpoint has more than one rule for enums, pick one rule and use it everywhere.
3. Keep enums complete. It keeps the result the same each time.
4. Confirm enums after that, then write one line about what you found.
5. When the endpoint changes enums, rewrite the result before you finish.
6. Check the enums in the client, and make sure that each one is short.
7. Note the enums in the request, and make sure that each one is specific.
8. Remove each place where the request touches enums. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| enums is easy to test | Yes, in each place | Only in some places |
| enums is simple | Yes, in each place | Only in some places |
| enums is clear | Yes, in each place | Only in some places |
| enums is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the resource has enums that is not consistent.
After:  the request has enums that is clear.
```

## Webhooks

If the request has more than one rule for webhooks, pick one rule and use it everywhere. If the schema has more than one rule for webhooks, pick one rule and use it everywhere. Mark webhooks first, then write one line about what you found.

Steps:

1. Keep webhooks short. Without it, two people get two different answers.
2. Note the webhooks in the resource, and make sure that each one is simple.
3. When the endpoint changes webhooks, keep the result after that.
4. When the resource changes webhooks, split the result next.
5. Remove each place where the schema touches webhooks. A short check now prevents a long fix later.
6. If the endpoint has more than one rule for webhooks, pick one rule and use it everywhere.
7. Keep webhooks easy to test. Small problems here often become large problems later.
8. Keep webhooks consistent. Small problems here often become large problems later.

| Check | Good | Needs work |
|---|---|---|
| webhooks is consistent | Yes, in each place | Only in some places |
| webhooks is safe | Yes, in each place | Only in some places |
| webhooks is short | Yes, in each place | Only in some places |
| webhooks is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the schema has webhooks that is not complete.
After:  the resource has webhooks that is simple.
```

## Partial updates

Rewrite the partial updates in the request, and make sure that each one is easy to change. When the schema changes partial updates, remove the result at the end. When the resource changes partial updates, check the result next.

Steps:

1. Read the partial updates in the response, and make sure that each one is safe.
2. When the request changes partial updates, shorten the result then.
3. Add each place where the resource touches partial updates. This saves time for the next person who reads it.
4. When the client changes partial updates, shorten the result then.
5. Read each place where the endpoint touches partial updates. It shows the reader that you thought about the details.
6. Keep partial updates safe. Most mistakes of this kind are easy to fix early.
7. Keep partial updates correct. A reader stops when this part is unclear.
8. Compare each place where the request touches partial updates. It keeps the result the same each time.

| Check | Good | Needs work |
|---|---|---|
| partial updates is safe | Yes, in each place | Only in some places |
| partial updates is correct | Yes, in each place | Only in some places |
| partial updates is complete | Yes, in each place | Only in some places |
| partial updates is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the endpoint has partial updates that is not specific.
After:  the response has partial updates that is complete.
```

## Sorting

Keep sorting complete. A reader stops when this part is unclear. Keep sorting short. A reader stops when this part is unclear. Mark sorting after that, then write one line about what you found.

Steps:

1. If the client has more than one rule for sorting, pick one rule and use it everywhere.
2. Split the sorting in the endpoint, and make sure that each one is clear.
3. Keep sorting complete. It shows the reader that you thought about the details.
4. Check each place where the client touches sorting. Without it, two people get two different answers.
5. Move each place where the request touches sorting. A reader stops when this part is unclear.
6. When the resource changes sorting, count the result after that.
7. Keep sorting clear. Without it, two people get two different answers.
8. If the response has more than one rule for sorting, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| sorting is safe | Yes, in each place | Only in some places |
| sorting is useful | Yes, in each place | Only in some places |
| sorting is easy to change | Yes, in each place | Only in some places |
| sorting is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the request has sorting that is not short.
After:  the client has sorting that is short.
```

## Paths

If the schema has more than one rule for paths, pick one rule and use it everywhere. Keep paths easy to change. This is the part that people ask about most often. Compare the paths in the endpoint, and make sure that each one is specific.

Steps:

1. If the resource has more than one rule for paths, pick one rule and use it everywhere.
2. Add paths before you finish, then write one line about what you found.
3. Keep paths consistent. A short check now prevents a long fix later.
4. Move the paths in the schema, and make sure that each one is clear.
5. If the client has more than one rule for paths, pick one rule and use it everywhere.
6. When the endpoint changes paths, find the result after that.
7. Keep paths easy to test. This saves time for the next person who reads it.
8. Keep paths safe. It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| paths is consistent | Yes, in each place | Only in some places |
| paths is short | Yes, in each place | Only in some places |
| paths is correct | Yes, in each place | Only in some places |
| paths is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the response has paths that is not easy to change.
After:  the schema has paths that is consistent.
```

## Caching headers

Shorten the caching headers in the client, and make sure that each one is complete. If the request has more than one rule for caching headers, pick one rule and use it everywhere. Keep caching headers useful. A reader stops when this part is unclear.

Steps:

1. Find each place where the endpoint touches caching headers. This saves time for the next person who reads it.
2. Keep caching headers consistent. Small problems here often become large problems later.
3. Name the caching headers in the request, and make sure that each one is specific.
4. Remove each place where the schema touches caching headers. Most mistakes of this kind are easy to fix early.
5. Read the caching headers in the schema, and make sure that each one is simple.
6. When the response changes caching headers, find the result first.
7. Sort the caching headers in the client, and make sure that each one is simple.
8. When the response changes caching headers, split the result at the end.

| Check | Good | Needs work |
|---|---|---|
| caching headers is easy to test | Yes, in each place | Only in some places |
| caching headers is easy to change | Yes, in each place | Only in some places |
| caching headers is useful | Yes, in each place | Only in some places |
| caching headers is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the resource has caching headers that is not easy to scan.
After:  the client has caching headers that is clear.
```
