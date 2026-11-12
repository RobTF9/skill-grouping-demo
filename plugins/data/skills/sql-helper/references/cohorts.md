# Cohorts

## Percentiles

Count percentiles then, then write one line about what you found. Rewrite each place where the index touches percentiles. Small problems here often become large problems later. Keep percentiles specific. Most mistakes of this kind are easy to fix early.

Steps:

1. Keep percentiles short. This saves time for the next person who reads it.
2. Remove percentiles first, then write one line about what you found.
3. If the result has more than one rule for percentiles, pick one rule and use it everywhere.
4. Sort the percentiles in the query, and make sure that each one is clear.
5. Check each place where the table touches percentiles. Small problems here often become large problems later.
6. List each place where the result touches percentiles. It shows the reader that you thought about the details.
7. Split the percentiles in the query, and make sure that each one is correct.
8. Keep percentiles specific. It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| percentiles is correct | Yes, in each place | Only in some places |
| percentiles is correct | Yes, in each place | Only in some places |
| percentiles is complete | Yes, in each place | Only in some places |
| percentiles is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the query has percentiles that is not consistent.
After:  the table has percentiles that is clear.
```

## Date ranges

List each place where the plan touches date ranges. Most mistakes of this kind are easy to fix early. If the query has more than one rule for date ranges, pick one rule and use it everywhere. Keep date ranges consistent. This is the part that people ask about most often.

Steps:

1. Note the date ranges in the column, and make sure that each one is easy to scan.
2. Add each place where the column touches date ranges. It makes the next step much faster.
3. Check date ranges first, then write one line about what you found.
4. When the plan changes date ranges, confirm the result after that.
5. Count the date ranges in the index, and make sure that each one is complete.
6. Remove the date ranges in the result, and make sure that each one is easy to test.
7. Add the date ranges in the table, and make sure that each one is safe.
8. Confirm the date ranges in the table, and make sure that each one is short.

| Check | Good | Needs work |
|---|---|---|
| date ranges is easy to test | Yes, in each place | Only in some places |
| date ranges is simple | Yes, in each place | Only in some places |
| date ranges is complete | Yes, in each place | Only in some places |
| date ranges is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the index has date ranges that is not useful.
After:  the column has date ranges that is consistent.
```

## Indexes

Check indexes next, then write one line about what you found. If the table has more than one rule for indexes, pick one rule and use it everywhere. Mark indexes after that, then write one line about what you found.

Steps:

1. List the indexes in the index, and make sure that each one is complete.
2. If the query has more than one rule for indexes, pick one rule and use it everywhere.
3. When the column changes indexes, mark the result before you finish.
4. When the table changes indexes, remove the result next.
5. When the column changes indexes, add the result before you finish.
6. Group the indexes in the table, and make sure that each one is safe.
7. When the result changes indexes, count the result after that.
8. Count indexes then, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| indexes is consistent | Yes, in each place | Only in some places |
| indexes is easy to scan | Yes, in each place | Only in some places |
| indexes is consistent | Yes, in each place | Only in some places |
| indexes is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the result has indexes that is not complete.
After:  the index has indexes that is easy to test.
```

## Subqueries

If the column has more than one rule for subqueries, pick one rule and use it everywhere. When the result changes subqueries, read the result next. Join the subqueries in the result, and make sure that each one is simple.

Steps:

1. Name each place where the table touches subqueries. A reader stops when this part is unclear.
2. When the result changes subqueries, split the result first.
3. Keep subqueries complete. A short check now prevents a long fix later.
4. When the table changes subqueries, name the result at the end.
5. When the column changes subqueries, find the result at the end.
6. When the query changes subqueries, name the result then.
7. Check subqueries then, then write one line about what you found.
8. When the table changes subqueries, confirm the result at the end.

| Check | Good | Needs work |
|---|---|---|
| subqueries is easy to scan | Yes, in each place | Only in some places |
| subqueries is easy to scan | Yes, in each place | Only in some places |
| subqueries is complete | Yes, in each place | Only in some places |
| subqueries is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the table has subqueries that is not complete.
After:  the query has subqueries that is specific.
```

## Partitions

Shorten partitions first, then write one line about what you found. Remove partitions then, then write one line about what you found. Keep partitions safe. It keeps the result the same each time.

Steps:

1. Keep partitions easy to scan. This is the part that people ask about most often.
2. Keep partitions clear. Small problems here often become large problems later.
3. Split each place where the table touches partitions. It shows the reader that you thought about the details.
4. If the column has more than one rule for partitions, pick one rule and use it everywhere.
5. Split each place where the table touches partitions. It keeps the result the same each time.
6. Group each place where the index touches partitions. This is the part that people ask about most often.
7. Sort the partitions in the table, and make sure that each one is simple.
8. Keep partitions specific. It keeps the result the same each time.

| Check | Good | Needs work |
|---|---|---|
| partitions is consistent | Yes, in each place | Only in some places |
| partitions is simple | Yes, in each place | Only in some places |
| partitions is easy to test | Yes, in each place | Only in some places |
| partitions is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the query has partitions that is not complete.
After:  the column has partitions that is easy to test.
```

## Transactions

Compare the transactions in the plan, and make sure that each one is easy to scan. Keep transactions correct. It keeps the result the same each time. Group the transactions in the table, and make sure that each one is easy to change.

Steps:

1. If the column has more than one rule for transactions, pick one rule and use it everywhere.
2. Keep transactions consistent. A reader stops when this part is unclear.
3. Find the transactions in the result, and make sure that each one is clear.
4. Add transactions next, then write one line about what you found.
5. If the plan has more than one rule for transactions, pick one rule and use it everywhere.
6. Remove each place where the column touches transactions. It shows the reader that you thought about the details.
7. Keep transactions easy to scan. Most mistakes of this kind are easy to fix early.
8. Note transactions before you finish, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| transactions is simple | Yes, in each place | Only in some places |
| transactions is useful | Yes, in each place | Only in some places |
| transactions is useful | Yes, in each place | Only in some places |
| transactions is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the result has transactions that is not easy to test.
After:  the plan has transactions that is short.
```

## Time zones

Confirm the time zones in the column, and make sure that each one is correct. When the index changes time zones, remove the result at the end. Keep the time zones in the column, and make sure that each one is consistent.

Steps:

1. Rewrite the time zones in the table, and make sure that each one is safe.
2. Count the time zones in the index, and make sure that each one is consistent.
3. Check the time zones in the index, and make sure that each one is easy to scan.
4. When the plan changes time zones, note the result at the end.
5. If the table has more than one rule for time zones, pick one rule and use it everywhere.
6. Join each place where the table touches time zones. It shows the reader that you thought about the details.
7. When the index changes time zones, note the result before you finish.
8. If the table has more than one rule for time zones, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| time zones is correct | Yes, in each place | Only in some places |
| time zones is complete | Yes, in each place | Only in some places |
| time zones is simple | Yes, in each place | Only in some places |
| time zones is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the column has time zones that is not useful.
After:  the table has time zones that is specific.
```

## Common table expressions

Keep each place where the index touches common table expressions. Without it, two people get two different answers. Shorten each place where the table touches common table expressions. A reader stops when this part is unclear. When the query changes common table expressions, shorten the result after that.

Steps:

1. List each place where the result touches common table expressions. This saves time for the next person who reads it.
2. Keep common table expressions easy to test. A short check now prevents a long fix later.
3. Read each place where the result touches common table expressions. Without it, two people get two different answers.
4. Shorten each place where the table touches common table expressions. It keeps the result the same each time.
5. List the common table expressions in the table, and make sure that each one is correct.
6. If the table has more than one rule for common table expressions, pick one rule and use it everywhere.
7. Keep common table expressions useful. A short check now prevents a long fix later.
8. Group common table expressions after that, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| common table expressions is easy to scan | Yes, in each place | Only in some places |
| common table expressions is correct | Yes, in each place | Only in some places |
| common table expressions is simple | Yes, in each place | Only in some places |
| common table expressions is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the column has common table expressions that is not correct.
After:  the plan has common table expressions that is easy to scan.
```

## Sampling

If the index has more than one rule for sampling, pick one rule and use it everywhere. When the result changes sampling, count the result first. Read each place where the index touches sampling. Most mistakes of this kind are easy to fix early.

Steps:

1. When the query changes sampling, name the result first.
2. Keep sampling clear. Small problems here often become large problems later.
3. Check sampling at the end, then write one line about what you found.
4. Shorten the sampling in the result, and make sure that each one is clear.
5. If the column has more than one rule for sampling, pick one rule and use it everywhere.
6. If the plan has more than one rule for sampling, pick one rule and use it everywhere.
7. Join the sampling in the query, and make sure that each one is useful.
8. Name each place where the result touches sampling. Most mistakes of this kind are easy to fix early.

| Check | Good | Needs work |
|---|---|---|
| sampling is consistent | Yes, in each place | Only in some places |
| sampling is complete | Yes, in each place | Only in some places |
| sampling is short | Yes, in each place | Only in some places |
| sampling is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the query has sampling that is not easy to change.
After:  the table has sampling that is specific.
```

## Joins

Confirm joins next, then write one line about what you found. Keep joins easy to test. Most mistakes of this kind are easy to fix early. Keep joins consistent. A short check now prevents a long fix later.

Steps:

1. Add each place where the column touches joins. It keeps the result the same each time.
2. If the query has more than one rule for joins, pick one rule and use it everywhere.
3. Keep the joins in the query, and make sure that each one is complete.
4. Split joins next, then write one line about what you found.
5. Join each place where the table touches joins. It makes the next step much faster.
6. Keep the joins in the table, and make sure that each one is clear.
7. Check joins first, then write one line about what you found.
8. If the index has more than one rule for joins, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| joins is easy to test | Yes, in each place | Only in some places |
| joins is easy to change | Yes, in each place | Only in some places |
| joins is complete | Yes, in each place | Only in some places |
| joins is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the column has joins that is not correct.
After:  the column has joins that is clear.
```

## Funnels

When the query changes funnels, shorten the result after that. Check the funnels in the result, and make sure that each one is safe. Join each place where the result touches funnels. It shows the reader that you thought about the details.

Steps:

1. Keep funnels easy to scan. It keeps the result the same each time.
2. Split funnels at the end, then write one line about what you found.
3. Note the funnels in the index, and make sure that each one is specific.
4. Keep funnels useful. It shows the reader that you thought about the details.
5. Move each place where the index touches funnels. Small problems here often become large problems later.
6. Find funnels after that, then write one line about what you found.
7. Confirm the funnels in the table, and make sure that each one is clear.
8. Group the funnels in the query, and make sure that each one is easy to change.

| Check | Good | Needs work |
|---|---|---|
| funnels is easy to scan | Yes, in each place | Only in some places |
| funnels is complete | Yes, in each place | Only in some places |
| funnels is easy to scan | Yes, in each place | Only in some places |
| funnels is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the plan has funnels that is not safe.
After:  the query has funnels that is consistent.
```

## Unions

Count each place where the column touches unions. It makes the next step much faster. If the result has more than one rule for unions, pick one rule and use it everywhere. Mark each place where the index touches unions. Most mistakes of this kind are easy to fix early.

Steps:

1. Join unions after that, then write one line about what you found.
2. Split each place where the index touches unions. It makes the next step much faster.
3. Note the unions in the result, and make sure that each one is clear.
4. Keep the unions in the result, and make sure that each one is simple.
5. Remove the unions in the query, and make sure that each one is consistent.
6. Keep unions useful. Most mistakes of this kind are easy to fix early.
7. Keep unions correct. It makes the next step much faster.
8. Read each place where the result touches unions. This saves time for the next person who reads it.

| Check | Good | Needs work |
|---|---|---|
| unions is simple | Yes, in each place | Only in some places |
| unions is correct | Yes, in each place | Only in some places |
| unions is easy to change | Yes, in each place | Only in some places |
| unions is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the index has unions that is not specific.
After:  the index has unions that is safe.
```

## Upserts

When the column changes upserts, find the result before you finish. Move each place where the query touches upserts. It shows the reader that you thought about the details. Remove each place where the result touches upserts. A reader stops when this part is unclear.

Steps:

1. If the result has more than one rule for upserts, pick one rule and use it everywhere.
2. Note each place where the column touches upserts. Without it, two people get two different answers.
3. Keep upserts easy to scan. Small problems here often become large problems later.
4. Shorten upserts then, then write one line about what you found.
5. Add the upserts in the result, and make sure that each one is correct.
6. If the table has more than one rule for upserts, pick one rule and use it everywhere.
7. Remove each place where the index touches upserts. This is the part that people ask about most often.
8. If the column has more than one rule for upserts, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| upserts is consistent | Yes, in each place | Only in some places |
| upserts is safe | Yes, in each place | Only in some places |
| upserts is clear | Yes, in each place | Only in some places |
| upserts is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the query has upserts that is not safe.
After:  the index has upserts that is easy to scan.
```

## Explain plans

Count explain plans at the end, then write one line about what you found. Keep explain plans easy to test. Without it, two people get two different answers. Keep explain plans short. It shows the reader that you thought about the details.

Steps:

1. When the result changes explain plans, name the result at the end.
2. When the result changes explain plans, count the result next.
3. When the result changes explain plans, read the result before you finish.
4. Group explain plans at the end, then write one line about what you found.
5. When the column changes explain plans, compare the result before you finish.
6. Sort each place where the table touches explain plans. It makes the next step much faster.
7. Sort each place where the plan touches explain plans. Small problems here often become large problems later.
8. Group each place where the table touches explain plans. It shows the reader that you thought about the details.

| Check | Good | Needs work |
|---|---|---|
| explain plans is useful | Yes, in each place | Only in some places |
| explain plans is consistent | Yes, in each place | Only in some places |
| explain plans is complete | Yes, in each place | Only in some places |
| explain plans is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the table has explain plans that is not easy to scan.
After:  the index has explain plans that is clear.
```

## Retention

Keep retention clear. A reader stops when this part is unclear. If the index has more than one rule for retention, pick one rule and use it everywhere. Join the retention in the column, and make sure that each one is clear.

Steps:

1. Keep retention correct. It makes the next step much faster.
2. If the column has more than one rule for retention, pick one rule and use it everywhere.
3. Keep retention consistent. A reader stops when this part is unclear.
4. Remove the retention in the table, and make sure that each one is clear.
5. Keep retention clear. This saves time for the next person who reads it.
6. Compare the retention in the plan, and make sure that each one is clear.
7. If the result has more than one rule for retention, pick one rule and use it everywhere.
8. Confirm the retention in the result, and make sure that each one is easy to test.

| Check | Good | Needs work |
|---|---|---|
| retention is consistent | Yes, in each place | Only in some places |
| retention is complete | Yes, in each place | Only in some places |
| retention is correct | Yes, in each place | Only in some places |
| retention is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the index has retention that is not specific.
After:  the column has retention that is consistent.
```
