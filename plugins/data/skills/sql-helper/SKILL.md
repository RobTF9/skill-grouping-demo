---
name: sql-helper
description: Write and explain SQL queries for a Postgres database.
---

# SQL helper

Write the query, then explain it in plain words, one clause at a time.

## Percentiles

List each place where the plan touches percentiles. This is the part that people ask about most often. Join the percentiles in the table, and make sure that each one is consistent. Count each place where the column touches percentiles. This is the part that people ask about most often.

Steps:

1. Sort each place where the column touches percentiles. It keeps the result the same each time.
2. Name each place where the query touches percentiles. This is the part that people ask about most often.
3. Keep percentiles clear. This is the part that people ask about most often.
4. Keep percentiles clear. A reader stops when this part is unclear.
5. Split percentiles then, then write one line about what you found.
6. Count percentiles at the end, then write one line about what you found.
7. Shorten percentiles after that, then write one line about what you found.
8. If the column has more than one rule for percentiles, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| percentiles is useful | Yes, in each place | Only in some places |
| percentiles is easy to scan | Yes, in each place | Only in some places |
| percentiles is short | Yes, in each place | Only in some places |
| percentiles is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the query has percentiles that is not consistent.
After:  the index has percentiles that is useful.
```

## Sampling

Split the sampling in the table, and make sure that each one is consistent. Shorten each place where the table touches sampling. This is the part that people ask about most often. Check each place where the result touches sampling. A short check now prevents a long fix later.

Steps:

1. Remove the sampling in the column, and make sure that each one is clear.
2. Keep each place where the table touches sampling. A reader stops when this part is unclear.
3. List the sampling in the result, and make sure that each one is specific.
4. Keep sampling clear. A reader stops when this part is unclear.
5. Rewrite the sampling in the index, and make sure that each one is safe.
6. Check sampling first, then write one line about what you found.
7. Keep sampling easy to scan. It makes the next step much faster.
8. If the result has more than one rule for sampling, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| sampling is easy to test | Yes, in each place | Only in some places |
| sampling is easy to scan | Yes, in each place | Only in some places |
| sampling is clear | Yes, in each place | Only in some places |
| sampling is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the query has sampling that is not correct.
After:  the table has sampling that is easy to scan.
```

## Funnels

When the result changes funnels, read the result first. List funnels before you finish, then write one line about what you found. Keep funnels easy to test. This saves time for the next person who reads it.

Steps:

1. Add the funnels in the column, and make sure that each one is easy to scan.
2. If the column has more than one rule for funnels, pick one rule and use it everywhere.
3. Keep funnels clear. A reader stops when this part is unclear.
4. Sort the funnels in the query, and make sure that each one is specific.
5. Name each place where the plan touches funnels. Without it, two people get two different answers.
6. List the funnels in the plan, and make sure that each one is complete.
7. Split funnels after that, then write one line about what you found.
8. If the column has more than one rule for funnels, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| funnels is easy to change | Yes, in each place | Only in some places |
| funnels is useful | Yes, in each place | Only in some places |
| funnels is consistent | Yes, in each place | Only in some places |
| funnels is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the column has funnels that is not safe.
After:  the table has funnels that is clear.
```

## Partitions

When the table changes partitions, compare the result after that. Keep partitions first, then write one line about what you found. If the column has more than one rule for partitions, pick one rule and use it everywhere.

Steps:

1. Keep partitions complete. This is the part that people ask about most often.
2. Keep partitions easy to change. A short check now prevents a long fix later.
3. Keep partitions correct. It keeps the result the same each time.
4. Join each place where the query touches partitions. A reader stops when this part is unclear.
5. Keep partitions useful. Most mistakes of this kind are easy to fix early.
6. Name partitions then, then write one line about what you found.
7. Keep partitions simple. It shows the reader that you thought about the details.
8. Join partitions first, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| partitions is easy to change | Yes, in each place | Only in some places |
| partitions is clear | Yes, in each place | Only in some places |
| partitions is consistent | Yes, in each place | Only in some places |
| partitions is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the table has partitions that is not useful.
After:  the index has partitions that is simple.
```

## Text search

Keep text search complete. This is the part that people ask about most often. Note text search at the end, then write one line about what you found. Keep text search easy to test. Small problems here often become large problems later.

Steps:

1. When the index changes text search, rewrite the result at the end.
2. Join the text search in the plan, and make sure that each one is correct.
3. When the index changes text search, list the result at the end.
4. Confirm each place where the index touches text search. Without it, two people get two different answers.
5. Read the text search in the column, and make sure that each one is easy to scan.
6. Confirm text search next, then write one line about what you found.
7. Name each place where the plan touches text search. Most mistakes of this kind are easy to fix early.
8. Move text search first, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| text search is short | Yes, in each place | Only in some places |
| text search is specific | Yes, in each place | Only in some places |
| text search is easy to scan | Yes, in each place | Only in some places |
| text search is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the plan has text search that is not simple.
After:  the table has text search that is short.
```

## Joins

Split the joins in the query, and make sure that each one is simple. Mark joins at the end, then write one line about what you found. Move each place where the index touches joins. Small problems here often become large problems later.

Steps:

1. Keep joins easy to test. Without it, two people get two different answers.
2. Shorten joins next, then write one line about what you found.
3. When the index changes joins, add the result after that.
4. If the column has more than one rule for joins, pick one rule and use it everywhere.
5. Compare the joins in the query, and make sure that each one is simple.
6. If the table has more than one rule for joins, pick one rule and use it everywhere.
7. Add each place where the plan touches joins. A short check now prevents a long fix later.
8. Name the joins in the query, and make sure that each one is simple.

| Check | Good | Needs work |
|---|---|---|
| joins is complete | Yes, in each place | Only in some places |
| joins is easy to change | Yes, in each place | Only in some places |
| joins is simple | Yes, in each place | Only in some places |
| joins is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the result has joins that is not easy to scan.
After:  the result has joins that is safe.
```

## Upserts

Count each place where the index touches upserts. This is the part that people ask about most often. Note each place where the result touches upserts. This is the part that people ask about most often. Group the upserts in the query, and make sure that each one is clear.

Steps:

1. Split each place where the table touches upserts. It keeps the result the same each time.
2. When the query changes upserts, split the result then.
3. Count the upserts in the query, and make sure that each one is easy to test.
4. Keep upserts at the end, then write one line about what you found.
5. When the plan changes upserts, move the result before you finish.
6. If the column has more than one rule for upserts, pick one rule and use it everywhere.
7. Join the upserts in the query, and make sure that each one is specific.
8. Keep upserts correct. Small problems here often become large problems later.

| Check | Good | Needs work |
|---|---|---|
| upserts is easy to scan | Yes, in each place | Only in some places |
| upserts is consistent | Yes, in each place | Only in some places |
| upserts is useful | Yes, in each place | Only in some places |
| upserts is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the query has upserts that is not simple.
After:  the plan has upserts that is complete.
```

## Unions

Mark unions after that, then write one line about what you found. Confirm unions then, then write one line about what you found. Split unions next, then write one line about what you found.

Steps:

1. If the query has more than one rule for unions, pick one rule and use it everywhere.
2. When the result changes unions, list the result before you finish.
3. When the result changes unions, confirm the result at the end.
4. Move each place where the query touches unions. A reader stops when this part is unclear.
5. Join the unions in the column, and make sure that each one is specific.
6. If the index has more than one rule for unions, pick one rule and use it everywhere.
7. Mark unions before you finish, then write one line about what you found.
8. Join the unions in the table, and make sure that each one is consistent.

| Check | Good | Needs work |
|---|---|---|
| unions is simple | Yes, in each place | Only in some places |
| unions is clear | Yes, in each place | Only in some places |
| unions is easy to scan | Yes, in each place | Only in some places |
| unions is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the table has unions that is not easy to scan.
After:  the query has unions that is consistent.
```

## Indexes

If the plan has more than one rule for indexes, pick one rule and use it everywhere. Find each place where the table touches indexes. It shows the reader that you thought about the details. Keep indexes short. This is the part that people ask about most often.

Steps:

1. Read indexes next, then write one line about what you found.
2. Join each place where the query touches indexes. Most mistakes of this kind are easy to fix early.
3. Add the indexes in the table, and make sure that each one is correct.
4. Name the indexes in the query, and make sure that each one is safe.
5. Keep indexes safe. A reader stops when this part is unclear.
6. Move the indexes in the result, and make sure that each one is useful.
7. Compare indexes after that, then write one line about what you found.
8. If the index has more than one rule for indexes, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| indexes is useful | Yes, in each place | Only in some places |
| indexes is easy to change | Yes, in each place | Only in some places |
| indexes is easy to scan | Yes, in each place | Only in some places |
| indexes is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the index has indexes that is not specific.
After:  the table has indexes that is complete.
```

## Time zones

Keep time zones safe. Without it, two people get two different answers. If the plan has more than one rule for time zones, pick one rule and use it everywhere. If the table has more than one rule for time zones, pick one rule and use it everywhere.

Steps:

1. When the column changes time zones, move the result next.
2. Add time zones after that, then write one line about what you found.
3. Keep time zones safe. It shows the reader that you thought about the details.
4. Group the time zones in the query, and make sure that each one is safe.
5. Confirm each place where the result touches time zones. This is the part that people ask about most often.
6. Note the time zones in the index, and make sure that each one is easy to test.
7. Mark time zones next, then write one line about what you found.
8. Read time zones next, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| time zones is simple | Yes, in each place | Only in some places |
| time zones is consistent | Yes, in each place | Only in some places |
| time zones is useful | Yes, in each place | Only in some places |
| time zones is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the table has time zones that is not safe.
After:  the column has time zones that is safe.
```

## Deduplication

Keep deduplication short. It shows the reader that you thought about the details. Add deduplication first, then write one line about what you found. When the plan changes deduplication, sort the result after that.

Steps:

1. Keep deduplication short. This saves time for the next person who reads it.
2. Keep deduplication easy to test. Most mistakes of this kind are easy to fix early.
3. If the table has more than one rule for deduplication, pick one rule and use it everywhere.
4. When the result changes deduplication, add the result after that.
5. If the column has more than one rule for deduplication, pick one rule and use it everywhere.
6. Keep deduplication at the end, then write one line about what you found.
7. Confirm the deduplication in the query, and make sure that each one is complete.
8. If the index has more than one rule for deduplication, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| deduplication is useful | Yes, in each place | Only in some places |
| deduplication is short | Yes, in each place | Only in some places |
| deduplication is complete | Yes, in each place | Only in some places |
| deduplication is short | Yes, in each place | Only in some places |

Example:

```text
Before: the column has deduplication that is not easy to change.
After:  the result has deduplication that is specific.
```

## Subqueries

If the plan has more than one rule for subqueries, pick one rule and use it everywhere. Mark the subqueries in the column, and make sure that each one is complete. Add subqueries after that, then write one line about what you found.

Steps:

1. Rewrite the subqueries in the plan, and make sure that each one is correct.
2. When the table changes subqueries, add the result first.
3. Split each place where the column touches subqueries. Without it, two people get two different answers.
4. Mark each place where the column touches subqueries. This is the part that people ask about most often.
5. If the result has more than one rule for subqueries, pick one rule and use it everywhere.
6. If the table has more than one rule for subqueries, pick one rule and use it everywhere.
7. Check each place where the query touches subqueries. It keeps the result the same each time.
8. Name each place where the table touches subqueries. A reader stops when this part is unclear.

| Check | Good | Needs work |
|---|---|---|
| subqueries is specific | Yes, in each place | Only in some places |
| subqueries is easy to test | Yes, in each place | Only in some places |
| subqueries is complete | Yes, in each place | Only in some places |
| subqueries is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the index has subqueries that is not easy to test.
After:  the result has subqueries that is correct.
```

## Transactions

Compare each place where the result touches transactions. Without it, two people get two different answers. Split transactions after that, then write one line about what you found. Read each place where the query touches transactions. A reader stops when this part is unclear.

Steps:

1. If the plan has more than one rule for transactions, pick one rule and use it everywhere.
2. Note the transactions in the query, and make sure that each one is easy to test.
3. If the plan has more than one rule for transactions, pick one rule and use it everywhere.
4. Keep transactions clear. A short check now prevents a long fix later.
5. When the table changes transactions, join the result after that.
6. Keep transactions clear. It keeps the result the same each time.
7. Mark each place where the query touches transactions. This is the part that people ask about most often.
8. If the plan has more than one rule for transactions, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| transactions is correct | Yes, in each place | Only in some places |
| transactions is clear | Yes, in each place | Only in some places |
| transactions is specific | Yes, in each place | Only in some places |
| transactions is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the plan has transactions that is not short.
After:  the plan has transactions that is easy to scan.
```

## Explain plans

Keep explain plans easy to change. This saves time for the next person who reads it. Add explain plans then, then write one line about what you found. When the column changes explain plans, rewrite the result after that.

Steps:

1. When the result changes explain plans, group the result first.
2. Keep each place where the table touches explain plans. Small problems here often become large problems later.
3. Split explain plans at the end, then write one line about what you found.
4. Note the explain plans in the column, and make sure that each one is safe.
5. Note explain plans after that, then write one line about what you found.
6. Check explain plans after that, then write one line about what you found.
7. When the column changes explain plans, split the result before you finish.
8. If the query has more than one rule for explain plans, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| explain plans is simple | Yes, in each place | Only in some places |
| explain plans is clear | Yes, in each place | Only in some places |
| explain plans is easy to change | Yes, in each place | Only in some places |
| explain plans is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the plan has explain plans that is not useful.
After:  the query has explain plans that is complete.
```

## Cohorts

Count each place where the column touches cohorts. Small problems here often become large problems later. Compare cohorts at the end, then write one line about what you found. When the column changes cohorts, remove the result before you finish.

Steps:

1. Shorten the cohorts in the query, and make sure that each one is complete.
2. When the index changes cohorts, check the result then.
3. Remove cohorts before you finish, then write one line about what you found.
4. Keep cohorts easy to change. It shows the reader that you thought about the details.
5. Name each place where the table touches cohorts. It makes the next step much faster.
6. If the column has more than one rule for cohorts, pick one rule and use it everywhere.
7. Check each place where the index touches cohorts. Small problems here often become large problems later.
8. Mark each place where the plan touches cohorts. It keeps the result the same each time.

| Check | Good | Needs work |
|---|---|---|
| cohorts is clear | Yes, in each place | Only in some places |
| cohorts is correct | Yes, in each place | Only in some places |
| cohorts is easy to change | Yes, in each place | Only in some places |
| cohorts is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the plan has cohorts that is not easy to test.
After:  the result has cohorts that is short.
```

## Counts

Shorten each place where the table touches counts. A short check now prevents a long fix later. If the index has more than one rule for counts, pick one rule and use it everywhere. Split counts after that, then write one line about what you found.

Steps:

1. When the plan changes counts, remove the result after that.
2. Shorten counts first, then write one line about what you found.
3. Mark counts after that, then write one line about what you found.
4. Add the counts in the plan, and make sure that each one is complete.
5. When the plan changes counts, note the result then.
6. If the result has more than one rule for counts, pick one rule and use it everywhere.
7. Remove each place where the table touches counts. This is the part that people ask about most often.
8. Read each place where the column touches counts. It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| counts is useful | Yes, in each place | Only in some places |
| counts is simple | Yes, in each place | Only in some places |
| counts is safe | Yes, in each place | Only in some places |
| counts is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the query has counts that is not short.
After:  the table has counts that is complete.
```

## JSON columns

List each place where the plan touches JSON columns. Small problems here often become large problems later. Keep JSON columns easy to scan. Most mistakes of this kind are easy to fix early. Name each place where the query touches JSON columns. Without it, two people get two different answers.

Steps:

1. Shorten the JSON columns in the table, and make sure that each one is correct.
2. If the table has more than one rule for JSON columns, pick one rule and use it everywhere.
3. Keep JSON columns easy to scan. This saves time for the next person who reads it.
4. Find each place where the result touches JSON columns. A short check now prevents a long fix later.
5. Keep JSON columns useful. Without it, two people get two different answers.
6. Check JSON columns first, then write one line about what you found.
7. Keep the JSON columns in the plan, and make sure that each one is consistent.
8. When the column changes JSON columns, shorten the result then.

| Check | Good | Needs work |
|---|---|---|
| JSON columns is easy to change | Yes, in each place | Only in some places |
| JSON columns is safe | Yes, in each place | Only in some places |
| JSON columns is correct | Yes, in each place | Only in some places |
| JSON columns is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the column has JSON columns that is not consistent.
After:  the result has JSON columns that is complete.
```

## Common table expressions

Split the common table expressions in the index, and make sure that each one is short. If the result has more than one rule for common table expressions, pick one rule and use it everywhere. Name the common table expressions in the column, and make sure that each one is consistent.

Steps:

1. When the index changes common table expressions, name the result next.
2. When the query changes common table expressions, note the result next.
3. Find each place where the index touches common table expressions. Small problems here often become large problems later.
4. Check common table expressions next, then write one line about what you found.
5. When the column changes common table expressions, group the result next.
6. When the plan changes common table expressions, name the result next.
7. When the index changes common table expressions, rewrite the result after that.
8. When the index changes common table expressions, name the result before you finish.

| Check | Good | Needs work |
|---|---|---|
| common table expressions is simple | Yes, in each place | Only in some places |
| common table expressions is safe | Yes, in each place | Only in some places |
| common table expressions is consistent | Yes, in each place | Only in some places |
| common table expressions is short | Yes, in each place | Only in some places |

Example:

```text
Before: the plan has common table expressions that is not specific.
After:  the column has common table expressions that is useful.
```

## Group by

Keep each place where the table touches group by. Small problems here often become large problems later. Keep each place where the result touches group by. It makes the next step much faster. Move group by after that, then write one line about what you found.

Steps:

1. When the index changes group by, read the result next.
2. Mark group by then, then write one line about what you found.
3. Name group by next, then write one line about what you found.
4. Name group by at the end, then write one line about what you found.
5. When the result changes group by, count the result first.
6. Group group by then, then write one line about what you found.
7. If the query has more than one rule for group by, pick one rule and use it everywhere.
8. When the table changes group by, note the result after that.

| Check | Good | Needs work |
|---|---|---|
| group by is safe | Yes, in each place | Only in some places |
| group by is easy to change | Yes, in each place | Only in some places |
| group by is specific | Yes, in each place | Only in some places |
| group by is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the column has group by that is not easy to scan.
After:  the query has group by that is useful.
```

## Locks

If the index has more than one rule for locks, pick one rule and use it everywhere. Read each place where the index touches locks. This saves time for the next person who reads it. List locks before you finish, then write one line about what you found.

Steps:

1. When the query changes locks, shorten the result before you finish.
2. Remove locks next, then write one line about what you found.
3. Rewrite each place where the table touches locks. Most mistakes of this kind are easy to fix early.
4. When the column changes locks, split the result then.
5. Keep locks easy to test. This is the part that people ask about most often.
6. When the query changes locks, mark the result then.
7. Keep locks useful. A reader stops when this part is unclear.
8. Confirm each place where the table touches locks. It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| locks is safe | Yes, in each place | Only in some places |
| locks is safe | Yes, in each place | Only in some places |
| locks is easy to scan | Yes, in each place | Only in some places |
| locks is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the query has locks that is not safe.
After:  the index has locks that is consistent.
```

## Null values

If the table has more than one rule for null values, pick one rule and use it everywhere. Move each place where the index touches null values. Without it, two people get two different answers. When the column changes null values, add the result at the end.

Steps:

1. When the index changes null values, group the result next.
2. Join each place where the plan touches null values. Small problems here often become large problems later.
3. Find null values after that, then write one line about what you found.
4. Mark null values then, then write one line about what you found.
5. Keep null values clear. Most mistakes of this kind are easy to fix early.
6. If the result has more than one rule for null values, pick one rule and use it everywhere.
7. Rewrite each place where the plan touches null values. It makes the next step much faster.
8. Compare null values then, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| null values is easy to change | Yes, in each place | Only in some places |
| null values is short | Yes, in each place | Only in some places |
| null values is easy to scan | Yes, in each place | Only in some places |
| null values is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the table has null values that is not easy to test.
After:  the plan has null values that is easy to change.
```

## Window functions

If the column has more than one rule for window functions, pick one rule and use it everywhere. Move each place where the plan touches window functions. Most mistakes of this kind are easy to fix early. Keep window functions easy to scan. This is the part that people ask about most often.

Steps:

1. Note each place where the plan touches window functions. Most mistakes of this kind are easy to fix early.
2. If the query has more than one rule for window functions, pick one rule and use it everywhere.
3. Shorten each place where the table touches window functions. This saves time for the next person who reads it.
4. Count the window functions in the column, and make sure that each one is clear.
5. Keep window functions easy to test. It shows the reader that you thought about the details.
6. Mark the window functions in the column, and make sure that each one is correct.
7. Remove each place where the table touches window functions. It makes the next step much faster.
8. Keep window functions useful. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| window functions is useful | Yes, in each place | Only in some places |
| window functions is simple | Yes, in each place | Only in some places |
| window functions is safe | Yes, in each place | Only in some places |
| window functions is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the column has window functions that is not safe.
After:  the plan has window functions that is safe.
```

## Date ranges

Rewrite each place where the table touches date ranges. Small problems here often become large problems later. When the index changes date ranges, name the result next. Sort each place where the result touches date ranges. This is the part that people ask about most often.

Steps:

1. Keep date ranges safe. A reader stops when this part is unclear.
2. Keep date ranges correct. It keeps the result the same each time.
3. If the column has more than one rule for date ranges, pick one rule and use it everywhere.
4. Confirm each place where the column touches date ranges. It keeps the result the same each time.
5. When the query changes date ranges, remove the result after that.
6. Count each place where the query touches date ranges. Most mistakes of this kind are easy to fix early.
7. Join the date ranges in the index, and make sure that each one is simple.
8. List date ranges after that, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| date ranges is complete | Yes, in each place | Only in some places |
| date ranges is easy to scan | Yes, in each place | Only in some places |
| date ranges is short | Yes, in each place | Only in some places |
| date ranges is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the query has date ranges that is not correct.
After:  the table has date ranges that is easy to test.
```

## Retention

Keep retention easy to change. It keeps the result the same each time. Keep retention easy to test. This is the part that people ask about most often. Keep each place where the column touches retention. Without it, two people get two different answers.

Steps:

1. Find the retention in the index, and make sure that each one is specific.
2. If the result has more than one rule for retention, pick one rule and use it everywhere.
3. Compare the retention in the column, and make sure that each one is easy to change.
4. Name retention at the end, then write one line about what you found.
5. If the query has more than one rule for retention, pick one rule and use it everywhere.
6. Rewrite retention at the end, then write one line about what you found.
7. Check retention at the end, then write one line about what you found.
8. If the column has more than one rule for retention, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| retention is specific | Yes, in each place | Only in some places |
| retention is easy to test | Yes, in each place | Only in some places |
| retention is easy to scan | Yes, in each place | Only in some places |
| retention is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the query has retention that is not clear.
After:  the column has retention that is specific.
```

## Date ranges (pass 2)

When the query changes date ranges (pass 2), read the result next. Move date ranges (pass 2) then, then write one line about what you found. Check the date ranges (pass 2) in the column, and make sure that each one is useful.

Steps:

1. Keep date ranges (pass 2) specific. This saves time for the next person who reads it.
2. Group date ranges (pass 2) then, then write one line about what you found.
3. Keep date ranges (pass 2) easy to test. This saves time for the next person who reads it.
4. Name date ranges (pass 2) next, then write one line about what you found.
5. If the result has more than one rule for date ranges (pass 2), pick one rule and use it everywhere.
6. If the index has more than one rule for date ranges (pass 2), pick one rule and use it everywhere.
7. When the result changes date ranges (pass 2), count the result at the end.
8. Confirm each place where the plan touches date ranges (pass 2). A reader stops when this part is unclear.

| Check | Good | Needs work |
|---|---|---|
| date ranges (pass 2) is useful | Yes, in each place | Only in some places |
| date ranges (pass 2) is simple | Yes, in each place | Only in some places |
| date ranges (pass 2) is clear | Yes, in each place | Only in some places |
| date ranges (pass 2) is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the table has date ranges (pass 2) that is not specific.
After:  the table has date ranges (pass 2) that is useful.
```

## Subqueries (pass 2)

Count the subqueries (pass 2) in the result, and make sure that each one is correct. Note each place where the index touches subqueries (pass 2). It keeps the result the same each time. Add the subqueries (pass 2) in the result, and make sure that each one is simple.

Steps:

1. Keep subqueries (pass 2) correct. A short check now prevents a long fix later.
2. List subqueries (pass 2) after that, then write one line about what you found.
3. If the index has more than one rule for subqueries (pass 2), pick one rule and use it everywhere.
4. If the index has more than one rule for subqueries (pass 2), pick one rule and use it everywhere.
5. Confirm each place where the plan touches subqueries (pass 2). It shows the reader that you thought about the details.
6. Find subqueries (pass 2) before you finish, then write one line about what you found.
7. Split the subqueries (pass 2) in the plan, and make sure that each one is easy to test.
8. Remove each place where the query touches subqueries (pass 2). This saves time for the next person who reads it.

| Check | Good | Needs work |
|---|---|---|
| subqueries (pass 2) is short | Yes, in each place | Only in some places |
| subqueries (pass 2) is easy to change | Yes, in each place | Only in some places |
| subqueries (pass 2) is easy to change | Yes, in each place | Only in some places |
| subqueries (pass 2) is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the table has subqueries (pass 2) that is not safe.
After:  the query has subqueries (pass 2) that is correct.
```

## Counts (pass 2)

Group the counts (pass 2) in the index, and make sure that each one is consistent. Compare counts (pass 2) first, then write one line about what you found. Keep counts (pass 2) easy to scan. Without it, two people get two different answers.

Steps:

1. Keep counts (pass 2) useful. A reader stops when this part is unclear.
2. Mark each place where the result touches counts (pass 2). This saves time for the next person who reads it.
3. Note the counts (pass 2) in the result, and make sure that each one is complete.
4. Join the counts (pass 2) in the query, and make sure that each one is specific.
5. Count the counts (pass 2) in the query, and make sure that each one is clear.
6. List each place where the plan touches counts (pass 2). Without it, two people get two different answers.
7. Keep counts (pass 2) short. Small problems here often become large problems later.
8. If the query has more than one rule for counts (pass 2), pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| counts (pass 2) is useful | Yes, in each place | Only in some places |
| counts (pass 2) is complete | Yes, in each place | Only in some places |
| counts (pass 2) is safe | Yes, in each place | Only in some places |
| counts (pass 2) is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the table has counts (pass 2) that is not short.
After:  the index has counts (pass 2) that is simple.
```

## Partitions (pass 2)

Rewrite the partitions (pass 2) in the column, and make sure that each one is specific. Keep partitions (pass 2) simple. This is the part that people ask about most often. If the plan has more than one rule for partitions (pass 2), pick one rule and use it everywhere.

Steps:

1. Keep partitions (pass 2) easy to change. Small problems here often become large problems later.
2. Mark partitions (pass 2) after that, then write one line about what you found.
3. If the query has more than one rule for partitions (pass 2), pick one rule and use it everywhere.
4. Name the partitions (pass 2) in the result, and make sure that each one is short.
5. Keep partitions (pass 2) correct. This saves time for the next person who reads it.
6. When the query changes partitions (pass 2), rewrite the result then.
7. Mark each place where the column touches partitions (pass 2). It shows the reader that you thought about the details.
8. Name each place where the column touches partitions (pass 2). It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| partitions (pass 2) is easy to change | Yes, in each place | Only in some places |
| partitions (pass 2) is correct | Yes, in each place | Only in some places |
| partitions (pass 2) is correct | Yes, in each place | Only in some places |
| partitions (pass 2) is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the column has partitions (pass 2) that is not easy to test.
After:  the query has partitions (pass 2) that is consistent.
```
