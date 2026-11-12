# Schema notes

| Table | Holds | Key |
|---|---|---|
| teams | One row for each workspace | id |
| members | One row for each teammate in a team | team_id, user_id |
| invoices | One row for each invoice | id |
| events | One row for each product event | id, created_at |

## More detail

## Upserts

If the plan has more than one rule for upserts, pick one rule and use it everywhere. Join the upserts in the table, and make sure that each one is useful. Confirm each place where the column touches upserts. It keeps the result the same each time.

Steps:

1. If the index has more than one rule for upserts, pick one rule and use it everywhere.
2. Keep upserts correct. A reader stops when this part is unclear.
3. Join each place where the column touches upserts. Without it, two people get two different answers.
4. Check each place where the table touches upserts. It makes the next step much faster.
5. If the result has more than one rule for upserts, pick one rule and use it everywhere.
6. If the index has more than one rule for upserts, pick one rule and use it everywhere.
7. Note the upserts in the query, and make sure that each one is correct.
8. Move each place where the result touches upserts. It keeps the result the same each time.

| Check | Good | Needs work |
|---|---|---|
| upserts is safe | Yes, in each place | Only in some places |
| upserts is simple | Yes, in each place | Only in some places |
| upserts is useful | Yes, in each place | Only in some places |
| upserts is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the index has upserts that is not specific.
After:  the table has upserts that is specific.
```

## Partitions

Check each place where the query touches partitions. It shows the reader that you thought about the details. If the column has more than one rule for partitions, pick one rule and use it everywhere. Find the partitions in the result, and make sure that each one is easy to test.

Steps:

1. Name partitions at the end, then write one line about what you found.
2. When the column changes partitions, list the result after that.
3. Remove the partitions in the result, and make sure that each one is simple.
4. Keep partitions easy to change. A short check now prevents a long fix later.
5. Keep partitions correct. It keeps the result the same each time.
6. If the column has more than one rule for partitions, pick one rule and use it everywhere.
7. Group each place where the table touches partitions. It makes the next step much faster.
8. Shorten partitions after that, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| partitions is safe | Yes, in each place | Only in some places |
| partitions is easy to test | Yes, in each place | Only in some places |
| partitions is correct | Yes, in each place | Only in some places |
| partitions is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the column has partitions that is not safe.
After:  the result has partitions that is consistent.
```

## Text search

If the result has more than one rule for text search, pick one rule and use it everywhere. If the column has more than one rule for text search, pick one rule and use it everywhere. When the result changes text search, compare the result next.

Steps:

1. Keep text search simple. A reader stops when this part is unclear.
2. List each place where the column touches text search. Most mistakes of this kind are easy to fix early.
3. Compare text search before you finish, then write one line about what you found.
4. Find text search at the end, then write one line about what you found.
5. When the table changes text search, count the result next.
6. When the table changes text search, keep the result before you finish.
7. Shorten each place where the result touches text search. It makes the next step much faster.
8. When the plan changes text search, confirm the result at the end.

| Check | Good | Needs work |
|---|---|---|
| text search is easy to scan | Yes, in each place | Only in some places |
| text search is safe | Yes, in each place | Only in some places |
| text search is correct | Yes, in each place | Only in some places |
| text search is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the index has text search that is not easy to test.
After:  the query has text search that is complete.
```

## Common table expressions

Split common table expressions before you finish, then write one line about what you found. When the table changes common table expressions, group the result then. When the query changes common table expressions, add the result then.

Steps:

1. List common table expressions at the end, then write one line about what you found.
2. If the query has more than one rule for common table expressions, pick one rule and use it everywhere.
3. Shorten each place where the plan touches common table expressions. This saves time for the next person who reads it.
4. Rewrite each place where the index touches common table expressions. It keeps the result the same each time.
5. Name common table expressions after that, then write one line about what you found.
6. Name common table expressions before you finish, then write one line about what you found.
7. Join common table expressions first, then write one line about what you found.
8. If the query has more than one rule for common table expressions, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| common table expressions is short | Yes, in each place | Only in some places |
| common table expressions is simple | Yes, in each place | Only in some places |
| common table expressions is easy to change | Yes, in each place | Only in some places |
| common table expressions is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the result has common table expressions that is not short.
After:  the index has common table expressions that is complete.
```

## Group by

When the column changes group by, check the result first. If the table has more than one rule for group by, pick one rule and use it everywhere. Find each place where the index touches group by. A reader stops when this part is unclear.

Steps:

1. When the plan changes group by, move the result then.
2. If the result has more than one rule for group by, pick one rule and use it everywhere.
3. If the index has more than one rule for group by, pick one rule and use it everywhere.
4. Name the group by in the table, and make sure that each one is specific.
5. Split each place where the column touches group by. Small problems here often become large problems later.
6. Check the group by in the query, and make sure that each one is easy to test.
7. Name group by first, then write one line about what you found.
8. If the query has more than one rule for group by, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| group by is simple | Yes, in each place | Only in some places |
| group by is easy to test | Yes, in each place | Only in some places |
| group by is easy to test | Yes, in each place | Only in some places |
| group by is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the table has group by that is not easy to change.
After:  the index has group by that is correct.
```

## Cohorts

Shorten each place where the query touches cohorts. Most mistakes of this kind are easy to fix early. Keep cohorts easy to change. A reader stops when this part is unclear. If the table has more than one rule for cohorts, pick one rule and use it everywhere.

Steps:

1. Group cohorts first, then write one line about what you found.
2. Add each place where the index touches cohorts. A reader stops when this part is unclear.
3. Mark each place where the table touches cohorts. A reader stops when this part is unclear.
4. When the result changes cohorts, keep the result after that.
5. Move each place where the index touches cohorts. Small problems here often become large problems later.
6. If the result has more than one rule for cohorts, pick one rule and use it everywhere.
7. When the query changes cohorts, remove the result after that.
8. If the index has more than one rule for cohorts, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| cohorts is correct | Yes, in each place | Only in some places |
| cohorts is correct | Yes, in each place | Only in some places |
| cohorts is specific | Yes, in each place | Only in some places |
| cohorts is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the plan has cohorts that is not simple.
After:  the query has cohorts that is easy to change.
```

## Locks

When the column changes locks, confirm the result after that. Mark the locks in the result, and make sure that each one is clear. If the query has more than one rule for locks, pick one rule and use it everywhere.

Steps:

1. When the column changes locks, add the result after that.
2. Group each place where the plan touches locks. This saves time for the next person who reads it.
3. If the table has more than one rule for locks, pick one rule and use it everywhere.
4. Keep locks specific. It makes the next step much faster.
5. Keep locks easy to scan. It keeps the result the same each time.
6. Shorten locks before you finish, then write one line about what you found.
7. When the column changes locks, join the result first.
8. If the plan has more than one rule for locks, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| locks is consistent | Yes, in each place | Only in some places |
| locks is clear | Yes, in each place | Only in some places |
| locks is consistent | Yes, in each place | Only in some places |
| locks is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the index has locks that is not easy to scan.
After:  the plan has locks that is clear.
```

## Joins

Check each place where the index touches joins. It makes the next step much faster. When the result changes joins, remove the result then. When the result changes joins, sort the result after that.

Steps:

1. Find joins first, then write one line about what you found.
2. Find joins after that, then write one line about what you found.
3. Keep joins consistent. Small problems here often become large problems later.
4. Keep joins consistent. Small problems here often become large problems later.
5. Name joins next, then write one line about what you found.
6. When the column changes joins, mark the result then.
7. Keep joins consistent. It makes the next step much faster.
8. Read joins first, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| joins is easy to scan | Yes, in each place | Only in some places |
| joins is correct | Yes, in each place | Only in some places |
| joins is safe | Yes, in each place | Only in some places |
| joins is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the index has joins that is not short.
After:  the table has joins that is easy to test.
```

## Window functions

When the result changes window functions, shorten the result then. If the query has more than one rule for window functions, pick one rule and use it everywhere. Keep window functions correct. It makes the next step much faster.

Steps:

1. Keep window functions simple. This is the part that people ask about most often.
2. If the result has more than one rule for window functions, pick one rule and use it everywhere.
3. Keep window functions short. This is the part that people ask about most often.
4. Keep window functions clear. It shows the reader that you thought about the details.
5. Keep window functions complete. It makes the next step much faster.
6. Sort the window functions in the plan, and make sure that each one is consistent.
7. List the window functions in the table, and make sure that each one is short.
8. Count window functions then, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| window functions is correct | Yes, in each place | Only in some places |
| window functions is simple | Yes, in each place | Only in some places |
| window functions is easy to change | Yes, in each place | Only in some places |
| window functions is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the plan has window functions that is not specific.
After:  the query has window functions that is clear.
```

## Date ranges

When the index changes date ranges, split the result next. Keep date ranges short. Most mistakes of this kind are easy to fix early. Move each place where the result touches date ranges. This saves time for the next person who reads it.

Steps:

1. Keep date ranges specific. A short check now prevents a long fix later.
2. Compare each place where the table touches date ranges. A reader stops when this part is unclear.
3. Find each place where the table touches date ranges. Without it, two people get two different answers.
4. If the query has more than one rule for date ranges, pick one rule and use it everywhere.
5. Rewrite date ranges then, then write one line about what you found.
6. Name the date ranges in the result, and make sure that each one is clear.
7. Mark each place where the query touches date ranges. Most mistakes of this kind are easy to fix early.
8. Shorten the date ranges in the result, and make sure that each one is short.

| Check | Good | Needs work |
|---|---|---|
| date ranges is complete | Yes, in each place | Only in some places |
| date ranges is easy to change | Yes, in each place | Only in some places |
| date ranges is correct | Yes, in each place | Only in some places |
| date ranges is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the index has date ranges that is not clear.
After:  the query has date ranges that is easy to test.
```
