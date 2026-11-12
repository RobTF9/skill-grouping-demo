# Paging notes

- Use a cursor, not an offset, for each list that can grow.
- Return `nextCursor` as null on the last page.
- Cap the page size at 100.

## More detail

## Methods

When the endpoint changes methods, shorten the result next. Add each place where the response touches methods. It keeps the result the same each time. Shorten the methods in the client, and make sure that each one is easy to scan.

Steps:

1. If the request has more than one rule for methods, pick one rule and use it everywhere.
2. Find each place where the schema touches methods. This saves time for the next person who reads it.
3. Count each place where the response touches methods. This is the part that people ask about most often.
4. Keep methods easy to scan. A reader stops when this part is unclear.
5. Find each place where the resource touches methods. This saves time for the next person who reads it.
6. Check each place where the response touches methods. It keeps the result the same each time.
7. When the schema changes methods, rewrite the result before you finish.
8. Keep methods safe. It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| methods is specific | Yes, in each place | Only in some places |
| methods is useful | Yes, in each place | Only in some places |
| methods is easy to test | Yes, in each place | Only in some places |
| methods is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the response has methods that is not easy to test.
After:  the endpoint has methods that is clear.
```

## Sorting

Keep sorting easy to test. A reader stops when this part is unclear. When the resource changes sorting, check the result first. If the response has more than one rule for sorting, pick one rule and use it everywhere.

Steps:

1. Find sorting first, then write one line about what you found.
2. Find sorting first, then write one line about what you found.
3. When the request changes sorting, rewrite the result before you finish.
4. Keep sorting correct. A short check now prevents a long fix later.
5. Find each place where the request touches sorting. It shows the reader that you thought about the details.
6. List the sorting in the response, and make sure that each one is correct.
7. If the client has more than one rule for sorting, pick one rule and use it everywhere.
8. Join sorting next, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| sorting is easy to change | Yes, in each place | Only in some places |
| sorting is consistent | Yes, in each place | Only in some places |
| sorting is short | Yes, in each place | Only in some places |
| sorting is short | Yes, in each place | Only in some places |

Example:

```text
Before: the endpoint has sorting that is not consistent.
After:  the endpoint has sorting that is easy to test.
```

## Versions

If the client has more than one rule for versions, pick one rule and use it everywhere. Keep versions easy to change. It shows the reader that you thought about the details. Keep versions safe. It makes the next step much faster.

Steps:

1. If the schema has more than one rule for versions, pick one rule and use it everywhere.
2. When the response changes versions, remove the result before you finish.
3. Confirm versions next, then write one line about what you found.
4. If the request has more than one rule for versions, pick one rule and use it everywhere.
5. Split versions before you finish, then write one line about what you found.
6. If the request has more than one rule for versions, pick one rule and use it everywhere.
7. Group versions first, then write one line about what you found.
8. Note versions after that, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| versions is short | Yes, in each place | Only in some places |
| versions is specific | Yes, in each place | Only in some places |
| versions is useful | Yes, in each place | Only in some places |
| versions is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the resource has versions that is not safe.
After:  the schema has versions that is clear.
```

## Paths

If the resource has more than one rule for paths, pick one rule and use it everywhere. When the schema changes paths, keep the result first. Keep paths next, then write one line about what you found.

Steps:

1. Group the paths in the response, and make sure that each one is short.
2. Keep paths correct. It shows the reader that you thought about the details.
3. Sort the paths in the client, and make sure that each one is consistent.
4. Sort the paths in the endpoint, and make sure that each one is safe.
5. If the response has more than one rule for paths, pick one rule and use it everywhere.
6. If the resource has more than one rule for paths, pick one rule and use it everywhere.
7. Name paths first, then write one line about what you found.
8. If the request has more than one rule for paths, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| paths is short | Yes, in each place | Only in some places |
| paths is easy to test | Yes, in each place | Only in some places |
| paths is consistent | Yes, in each place | Only in some places |
| paths is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the response has paths that is not easy to scan.
After:  the schema has paths that is easy to change.
```

## Filters

If the response has more than one rule for filters, pick one rule and use it everywhere. If the response has more than one rule for filters, pick one rule and use it everywhere. Join the filters in the client, and make sure that each one is short.

Steps:

1. List each place where the request touches filters. This saves time for the next person who reads it.
2. When the endpoint changes filters, confirm the result before you finish.
3. Confirm filters at the end, then write one line about what you found.
4. Compare filters at the end, then write one line about what you found.
5. Join the filters in the resource, and make sure that each one is easy to scan.
6. If the resource has more than one rule for filters, pick one rule and use it everywhere.
7. Keep filters easy to change. A reader stops when this part is unclear.
8. If the response has more than one rule for filters, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| filters is consistent | Yes, in each place | Only in some places |
| filters is simple | Yes, in each place | Only in some places |
| filters is clear | Yes, in each place | Only in some places |
| filters is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the endpoint has filters that is not correct.
After:  the resource has filters that is easy to change.
```

## Long tasks

Move long tasks then, then write one line about what you found. Mark each place where the endpoint touches long tasks. It makes the next step much faster. Join the long tasks in the response, and make sure that each one is safe.

Steps:

1. Name the long tasks in the client, and make sure that each one is specific.
2. Move each place where the response touches long tasks. This is the part that people ask about most often.
3. When the response changes long tasks, mark the result at the end.
4. When the resource changes long tasks, name the result first.
5. When the schema changes long tasks, find the result before you finish.
6. When the response changes long tasks, split the result next.
7. If the schema has more than one rule for long tasks, pick one rule and use it everywhere.
8. Count the long tasks in the schema, and make sure that each one is correct.

| Check | Good | Needs work |
|---|---|---|
| long tasks is useful | Yes, in each place | Only in some places |
| long tasks is consistent | Yes, in each place | Only in some places |
| long tasks is correct | Yes, in each place | Only in some places |
| long tasks is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the endpoint has long tasks that is not easy to scan.
After:  the response has long tasks that is safe.
```

## Webhooks

Name the webhooks in the request, and make sure that each one is complete. Add webhooks first, then write one line about what you found. Keep webhooks simple. It shows the reader that you thought about the details.

Steps:

1. Mark the webhooks in the schema, and make sure that each one is specific.
2. If the endpoint has more than one rule for webhooks, pick one rule and use it everywhere.
3. When the client changes webhooks, name the result first.
4. Join the webhooks in the request, and make sure that each one is consistent.
5. Name webhooks before you finish, then write one line about what you found.
6. Add each place where the response touches webhooks. This saves time for the next person who reads it.
7. Rewrite webhooks then, then write one line about what you found.
8. Keep webhooks specific. Small problems here often become large problems later.

| Check | Good | Needs work |
|---|---|---|
| webhooks is safe | Yes, in each place | Only in some places |
| webhooks is easy to scan | Yes, in each place | Only in some places |
| webhooks is safe | Yes, in each place | Only in some places |
| webhooks is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the schema has webhooks that is not useful.
After:  the resource has webhooks that is easy to scan.
```

## Bulk actions

Rewrite each place where the response touches bulk actions. Small problems here often become large problems later. Check each place where the response touches bulk actions. This is the part that people ask about most often. Join the bulk actions in the response, and make sure that each one is easy to scan.

Steps:

1. Group each place where the request touches bulk actions. Small problems here often become large problems later.
2. Find the bulk actions in the schema, and make sure that each one is easy to change.
3. Move the bulk actions in the client, and make sure that each one is short.
4. Move bulk actions before you finish, then write one line about what you found.
5. Add each place where the request touches bulk actions. It makes the next step much faster.
6. When the schema changes bulk actions, mark the result before you finish.
7. Compare the bulk actions in the response, and make sure that each one is correct.
8. Remove the bulk actions in the client, and make sure that each one is safe.

| Check | Good | Needs work |
|---|---|---|
| bulk actions is simple | Yes, in each place | Only in some places |
| bulk actions is consistent | Yes, in each place | Only in some places |
| bulk actions is consistent | Yes, in each place | Only in some places |
| bulk actions is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the client has bulk actions that is not simple.
After:  the request has bulk actions that is easy to scan.
```

## Status codes

Add the status codes in the endpoint, and make sure that each one is consistent. Sort status codes next, then write one line about what you found. Keep status codes easy to change. A reader stops when this part is unclear.

Steps:

1. Confirm status codes before you finish, then write one line about what you found.
2. Find the status codes in the schema, and make sure that each one is correct.
3. Keep status codes safe. It keeps the result the same each time.
4. When the schema changes status codes, rewrite the result then.
5. Name status codes then, then write one line about what you found.
6. Sort status codes first, then write one line about what you found.
7. When the resource changes status codes, move the result after that.
8. When the client changes status codes, mark the result before you finish.

| Check | Good | Needs work |
|---|---|---|
| status codes is easy to scan | Yes, in each place | Only in some places |
| status codes is useful | Yes, in each place | Only in some places |
| status codes is complete | Yes, in each place | Only in some places |
| status codes is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the client has status codes that is not useful.
After:  the endpoint has status codes that is specific.
```

## File uploads

Sort each place where the resource touches file uploads. Most mistakes of this kind are easy to fix early. Name the file uploads in the request, and make sure that each one is easy to scan. Confirm the file uploads in the client, and make sure that each one is consistent.

Steps:

1. Keep file uploads easy to scan. Most mistakes of this kind are easy to fix early.
2. Find each place where the schema touches file uploads. It makes the next step much faster.
3. Read each place where the resource touches file uploads. This saves time for the next person who reads it.
4. When the request changes file uploads, join the result then.
5. Add each place where the response touches file uploads. This saves time for the next person who reads it.
6. Join the file uploads in the endpoint, and make sure that each one is short.
7. Read file uploads next, then write one line about what you found.
8. If the schema has more than one rule for file uploads, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| file uploads is consistent | Yes, in each place | Only in some places |
| file uploads is clear | Yes, in each place | Only in some places |
| file uploads is short | Yes, in each place | Only in some places |
| file uploads is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the schema has file uploads that is not easy to change.
After:  the client has file uploads that is short.
```

## Field names

Group the field names in the response, and make sure that each one is clear. If the resource has more than one rule for field names, pick one rule and use it everywhere. Find field names then, then write one line about what you found.

Steps:

1. Keep field names specific. A short check now prevents a long fix later.
2. Note field names then, then write one line about what you found.
3. Read each place where the request touches field names. This saves time for the next person who reads it.
4. Note each place where the endpoint touches field names. This is the part that people ask about most often.
5. Keep field names first, then write one line about what you found.
6. Read field names before you finish, then write one line about what you found.
7. Check field names at the end, then write one line about what you found.
8. Check the field names in the endpoint, and make sure that each one is clear.

| Check | Good | Needs work |
|---|---|---|
| field names is complete | Yes, in each place | Only in some places |
| field names is specific | Yes, in each place | Only in some places |
| field names is easy to scan | Yes, in each place | Only in some places |
| field names is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the resource has field names that is not consistent.
After:  the request has field names that is consistent.
```
