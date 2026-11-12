# Error notes

Each error has the same body:

```json
{ "code": "invoice_not_found", "message": "No invoice has this id." }
```

- `code` is stable. Clients can rely on it.
- `message` is for people. It can change.

## More detail

## Caching headers

Keep caching headers simple. Most mistakes of this kind are easy to fix early. If the request has more than one rule for caching headers, pick one rule and use it everywhere. Join the caching headers in the endpoint, and make sure that each one is short.

Steps:

1. If the client has more than one rule for caching headers, pick one rule and use it everywhere.
2. If the schema has more than one rule for caching headers, pick one rule and use it everywhere.
3. Keep caching headers consistent. A reader stops when this part is unclear.
4. Read each place where the response touches caching headers. It keeps the result the same each time.
5. If the response has more than one rule for caching headers, pick one rule and use it everywhere.
6. Note the caching headers in the schema, and make sure that each one is easy to scan.
7. If the endpoint has more than one rule for caching headers, pick one rule and use it everywhere.
8. When the resource changes caching headers, name the result next.

| Check | Good | Needs work |
|---|---|---|
| caching headers is easy to test | Yes, in each place | Only in some places |
| caching headers is simple | Yes, in each place | Only in some places |
| caching headers is specific | Yes, in each place | Only in some places |
| caching headers is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the request has caching headers that is not correct.
After:  the endpoint has caching headers that is consistent.
```

## Search

Keep search simple. Most mistakes of this kind are easy to fix early. Mark search then, then write one line about what you found. When the resource changes search, find the result after that.

Steps:

1. When the endpoint changes search, read the result after that.
2. Join search at the end, then write one line about what you found.
3. Count search next, then write one line about what you found.
4. Check each place where the schema touches search. It makes the next step much faster.
5. Keep search easy to scan. This is the part that people ask about most often.
6. If the resource has more than one rule for search, pick one rule and use it everywhere.
7. When the schema changes search, group the result first.
8. Find each place where the request touches search. It shows the reader that you thought about the details.

| Check | Good | Needs work |
|---|---|---|
| search is safe | Yes, in each place | Only in some places |
| search is correct | Yes, in each place | Only in some places |
| search is short | Yes, in each place | Only in some places |
| search is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the response has search that is not specific.
After:  the resource has search that is easy to change.
```

## Conditional requests

When the schema changes conditional requests, keep the result then. Keep conditional requests complete. Most mistakes of this kind are easy to fix early. Sort each place where the response touches conditional requests. Most mistakes of this kind are easy to fix early.

Steps:

1. When the schema changes conditional requests, shorten the result then.
2. Count conditional requests before you finish, then write one line about what you found.
3. Rewrite the conditional requests in the response, and make sure that each one is clear.
4. Shorten the conditional requests in the response, and make sure that each one is easy to test.
5. Mark the conditional requests in the request, and make sure that each one is complete.
6. Sort conditional requests first, then write one line about what you found.
7. Keep conditional requests simple. This saves time for the next person who reads it.
8. Move the conditional requests in the request, and make sure that each one is short.

| Check | Good | Needs work |
|---|---|---|
| conditional requests is consistent | Yes, in each place | Only in some places |
| conditional requests is clear | Yes, in each place | Only in some places |
| conditional requests is complete | Yes, in each place | Only in some places |
| conditional requests is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the client has conditional requests that is not complete.
After:  the request has conditional requests that is easy to test.
```

## Bulk actions

Name the bulk actions in the client, and make sure that each one is correct. Keep bulk actions easy to scan. A reader stops when this part is unclear. Rewrite each place where the response touches bulk actions. This is the part that people ask about most often.

Steps:

1. Keep bulk actions simple. It shows the reader that you thought about the details.
2. Read the bulk actions in the response, and make sure that each one is simple.
3. Split bulk actions at the end, then write one line about what you found.
4. When the response changes bulk actions, keep the result after that.
5. If the request has more than one rule for bulk actions, pick one rule and use it everywhere.
6. If the request has more than one rule for bulk actions, pick one rule and use it everywhere.
7. If the client has more than one rule for bulk actions, pick one rule and use it everywhere.
8. Sort bulk actions first, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| bulk actions is clear | Yes, in each place | Only in some places |
| bulk actions is clear | Yes, in each place | Only in some places |
| bulk actions is clear | Yes, in each place | Only in some places |
| bulk actions is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the schema has bulk actions that is not simple.
After:  the request has bulk actions that is consistent.
```

## IDs

If the response has more than one rule for IDs, pick one rule and use it everywhere. Add each place where the schema touches IDs. A reader stops when this part is unclear. Count IDs after that, then write one line about what you found.

Steps:

1. Note the IDs in the endpoint, and make sure that each one is simple.
2. Read each place where the resource touches IDs. It makes the next step much faster.
3. Count each place where the request touches IDs. Small problems here often become large problems later.
4. Mark each place where the endpoint touches IDs. It shows the reader that you thought about the details.
5. Note IDs before you finish, then write one line about what you found.
6. Shorten each place where the client touches IDs. It shows the reader that you thought about the details.
7. When the client changes IDs, move the result after that.
8. Group each place where the client touches IDs. Most mistakes of this kind are easy to fix early.

| Check | Good | Needs work |
|---|---|---|
| IDs is complete | Yes, in each place | Only in some places |
| IDs is consistent | Yes, in each place | Only in some places |
| IDs is easy to test | Yes, in each place | Only in some places |
| IDs is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the resource has IDs that is not easy to test.
After:  the client has IDs that is easy to test.
```

## Partial updates

Find each place where the schema touches partial updates. Small problems here often become large problems later. When the schema changes partial updates, rewrite the result then. If the request has more than one rule for partial updates, pick one rule and use it everywhere.

Steps:

1. Add each place where the response touches partial updates. Without it, two people get two different answers.
2. Move the partial updates in the schema, and make sure that each one is complete.
3. List each place where the resource touches partial updates. It keeps the result the same each time.
4. Move each place where the schema touches partial updates. A short check now prevents a long fix later.
5. Name the partial updates in the request, and make sure that each one is correct.
6. Sort each place where the client touches partial updates. This saves time for the next person who reads it.
7. When the request changes partial updates, remove the result at the end.
8. Keep partial updates specific. It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| partial updates is specific | Yes, in each place | Only in some places |
| partial updates is correct | Yes, in each place | Only in some places |
| partial updates is consistent | Yes, in each place | Only in some places |
| partial updates is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the response has partial updates that is not complete.
After:  the response has partial updates that is complete.
```

## Field names

If the client has more than one rule for field names, pick one rule and use it everywhere. If the client has more than one rule for field names, pick one rule and use it everywhere. Confirm the field names in the endpoint, and make sure that each one is specific.

Steps:

1. Add field names first, then write one line about what you found.
2. If the response has more than one rule for field names, pick one rule and use it everywhere.
3. Shorten the field names in the endpoint, and make sure that each one is simple.
4. Join each place where the endpoint touches field names. A short check now prevents a long fix later.
5. When the schema changes field names, mark the result at the end.
6. If the schema has more than one rule for field names, pick one rule and use it everywhere.
7. When the resource changes field names, add the result first.
8. Keep field names complete. A short check now prevents a long fix later.

| Check | Good | Needs work |
|---|---|---|
| field names is easy to scan | Yes, in each place | Only in some places |
| field names is easy to test | Yes, in each place | Only in some places |
| field names is complete | Yes, in each place | Only in some places |
| field names is short | Yes, in each place | Only in some places |

Example:

```text
Before: the schema has field names that is not easy to scan.
After:  the resource has field names that is useful.
```

## File uploads

Rewrite the file uploads in the request, and make sure that each one is correct. Keep file uploads easy to test. It makes the next step much faster. Name each place where the resource touches file uploads. Without it, two people get two different answers.

Steps:

1. Group each place where the client touches file uploads. It shows the reader that you thought about the details.
2. Keep file uploads easy to change. A reader stops when this part is unclear.
3. Remove file uploads first, then write one line about what you found.
4. If the client has more than one rule for file uploads, pick one rule and use it everywhere.
5. Move file uploads before you finish, then write one line about what you found.
6. When the schema changes file uploads, group the result then.
7. Keep each place where the resource touches file uploads. This saves time for the next person who reads it.
8. If the client has more than one rule for file uploads, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| file uploads is complete | Yes, in each place | Only in some places |
| file uploads is clear | Yes, in each place | Only in some places |
| file uploads is safe | Yes, in each place | Only in some places |
| file uploads is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the schema has file uploads that is not correct.
After:  the endpoint has file uploads that is easy to change.
```

## Filters

If the endpoint has more than one rule for filters, pick one rule and use it everywhere. If the client has more than one rule for filters, pick one rule and use it everywhere. If the client has more than one rule for filters, pick one rule and use it everywhere.

Steps:

1. When the schema changes filters, compare the result first.
2. Check the filters in the resource, and make sure that each one is useful.
3. If the response has more than one rule for filters, pick one rule and use it everywhere.
4. If the request has more than one rule for filters, pick one rule and use it everywhere.
5. Read filters first, then write one line about what you found.
6. Read each place where the endpoint touches filters. A short check now prevents a long fix later.
7. Check filters next, then write one line about what you found.
8. Sort each place where the resource touches filters. It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| filters is complete | Yes, in each place | Only in some places |
| filters is specific | Yes, in each place | Only in some places |
| filters is safe | Yes, in each place | Only in some places |
| filters is short | Yes, in each place | Only in some places |

Example:

```text
Before: the response has filters that is not useful.
After:  the response has filters that is complete.
```

## Nullable fields

Keep nullable fields easy to scan. This is the part that people ask about most often. Keep nullable fields complete. It keeps the result the same each time. When the endpoint changes nullable fields, compare the result before you finish.

Steps:

1. If the client has more than one rule for nullable fields, pick one rule and use it everywhere.
2. Keep nullable fields safe. It makes the next step much faster.
3. Split the nullable fields in the schema, and make sure that each one is complete.
4. Split each place where the schema touches nullable fields. Small problems here often become large problems later.
5. Remove each place where the response touches nullable fields. Small problems here often become large problems later.
6. When the resource changes nullable fields, group the result after that.
7. When the response changes nullable fields, find the result next.
8. When the request changes nullable fields, shorten the result next.

| Check | Good | Needs work |
|---|---|---|
| nullable fields is consistent | Yes, in each place | Only in some places |
| nullable fields is easy to scan | Yes, in each place | Only in some places |
| nullable fields is short | Yes, in each place | Only in some places |
| nullable fields is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the resource has nullable fields that is not short.
After:  the client has nullable fields that is clear.
```

## Date formats

Split each place where the schema touches date formats. Most mistakes of this kind are easy to fix early. Read each place where the resource touches date formats. Small problems here often become large problems later. Find date formats after that, then write one line about what you found.

Steps:

1. Name each place where the response touches date formats. This is the part that people ask about most often.
2. If the request has more than one rule for date formats, pick one rule and use it everywhere.
3. Read the date formats in the request, and make sure that each one is complete.
4. Count date formats first, then write one line about what you found.
5. Shorten the date formats in the schema, and make sure that each one is easy to change.
6. When the endpoint changes date formats, add the result first.
7. If the response has more than one rule for date formats, pick one rule and use it everywhere.
8. List date formats at the end, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| date formats is useful | Yes, in each place | Only in some places |
| date formats is clear | Yes, in each place | Only in some places |
| date formats is specific | Yes, in each place | Only in some places |
| date formats is short | Yes, in each place | Only in some places |

Example:

```text
Before: the schema has date formats that is not easy to test.
After:  the schema has date formats that is easy to test.
```

## Error bodies

When the resource changes error bodies, count the result next. If the client has more than one rule for error bodies, pick one rule and use it everywhere. If the client has more than one rule for error bodies, pick one rule and use it everywhere.

Steps:

1. If the endpoint has more than one rule for error bodies, pick one rule and use it everywhere.
2. Keep error bodies easy to scan. Without it, two people get two different answers.
3. Keep error bodies complete. It shows the reader that you thought about the details.
4. Confirm each place where the endpoint touches error bodies. This is the part that people ask about most often.
5. Add the error bodies in the endpoint, and make sure that each one is simple.
6. If the request has more than one rule for error bodies, pick one rule and use it everywhere.
7. When the resource changes error bodies, name the result after that.
8. If the resource has more than one rule for error bodies, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| error bodies is consistent | Yes, in each place | Only in some places |
| error bodies is easy to test | Yes, in each place | Only in some places |
| error bodies is safe | Yes, in each place | Only in some places |
| error bodies is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the client has error bodies that is not simple.
After:  the schema has error bodies that is complete.
```

## Rate limits

Find each place where the resource touches rate limits. Most mistakes of this kind are easy to fix early. When the request changes rate limits, note the result before you finish. Compare rate limits first, then write one line about what you found.

Steps:

1. If the request has more than one rule for rate limits, pick one rule and use it everywhere.
2. Shorten the rate limits in the response, and make sure that each one is short.
3. When the response changes rate limits, keep the result first.
4. Confirm each place where the schema touches rate limits. It makes the next step much faster.
5. If the request has more than one rule for rate limits, pick one rule and use it everywhere.
6. Move each place where the endpoint touches rate limits. A short check now prevents a long fix later.
7. When the client changes rate limits, compare the result after that.
8. When the endpoint changes rate limits, keep the result first.

| Check | Good | Needs work |
|---|---|---|
| rate limits is safe | Yes, in each place | Only in some places |
| rate limits is consistent | Yes, in each place | Only in some places |
| rate limits is easy to change | Yes, in each place | Only in some places |
| rate limits is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the endpoint has rate limits that is not simple.
After:  the client has rate limits that is short.
```
