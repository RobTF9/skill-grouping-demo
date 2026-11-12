# Window functions

## Joins

Keep joins correct. It makes the next step much faster. If the plan has more than one rule for joins, pick one rule and use it everywhere. List each place where the plan touches joins. It makes the next step much faster.

Steps:

1. Join the joins in the result, and make sure that each one is clear.
2. If the query has more than one rule for joins, pick one rule and use it everywhere.
3. Shorten the joins in the table, and make sure that each one is safe.
4. List the joins in the query, and make sure that each one is correct.
5. Group the joins in the result, and make sure that each one is consistent.
6. When the result changes joins, group the result next.
7. When the table changes joins, compare the result at the end.
8. Move joins before you finish, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| joins is clear | Yes, in each place | Only in some places |
| joins is safe | Yes, in each place | Only in some places |
| joins is useful | Yes, in each place | Only in some places |
| joins is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the column has joins that is not clear.
After:  the column has joins that is useful.
```

## Sampling

Keep sampling useful. Most mistakes of this kind are easy to fix early. Rewrite sampling next, then write one line about what you found. Group the sampling in the query, and make sure that each one is clear.

Steps:

1. When the column changes sampling, group the result before you finish.
2. Compare the sampling in the index, and make sure that each one is simple.
3. Keep sampling easy to scan. A short check now prevents a long fix later.
4. Keep sampling simple. It makes the next step much faster.
5. If the query has more than one rule for sampling, pick one rule and use it everywhere.
6. When the plan changes sampling, read the result before you finish.
7. If the index has more than one rule for sampling, pick one rule and use it everywhere.
8. Split the sampling in the plan, and make sure that each one is correct.

| Check | Good | Needs work |
|---|---|---|
| sampling is complete | Yes, in each place | Only in some places |
| sampling is easy to test | Yes, in each place | Only in some places |
| sampling is useful | Yes, in each place | Only in some places |
| sampling is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the plan has sampling that is not consistent.
After:  the query has sampling that is consistent.
```

## Subqueries

Keep subqueries specific. This is the part that people ask about most often. Keep subqueries consistent. This is the part that people ask about most often. Keep subqueries short. Most mistakes of this kind are easy to fix early.

Steps:

1. If the index has more than one rule for subqueries, pick one rule and use it everywhere.
2. When the plan changes subqueries, remove the result first.
3. When the query changes subqueries, remove the result before you finish.
4. When the table changes subqueries, remove the result then.
5. If the index has more than one rule for subqueries, pick one rule and use it everywhere.
6. List subqueries then, then write one line about what you found.
7. Add subqueries at the end, then write one line about what you found.
8. Keep subqueries complete. A short check now prevents a long fix later.

| Check | Good | Needs work |
|---|---|---|
| subqueries is useful | Yes, in each place | Only in some places |
| subqueries is clear | Yes, in each place | Only in some places |
| subqueries is short | Yes, in each place | Only in some places |
| subqueries is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the column has subqueries that is not useful.
After:  the column has subqueries that is useful.
```

## Null values

Keep null values correct. It makes the next step much faster. If the plan has more than one rule for null values, pick one rule and use it everywhere. Shorten each place where the query touches null values. It keeps the result the same each time.

Steps:

1. List null values first, then write one line about what you found.
2. Keep null values short. Without it, two people get two different answers.
3. When the query changes null values, move the result then.
4. Move null values after that, then write one line about what you found.
5. Mark each place where the result touches null values. A short check now prevents a long fix later.
6. Shorten null values first, then write one line about what you found.
7. Count the null values in the table, and make sure that each one is easy to scan.
8. Shorten the null values in the query, and make sure that each one is easy to test.

| Check | Good | Needs work |
|---|---|---|
| null values is useful | Yes, in each place | Only in some places |
| null values is complete | Yes, in each place | Only in some places |
| null values is complete | Yes, in each place | Only in some places |
| null values is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the plan has null values that is not useful.
After:  the plan has null values that is easy to change.
```

## Locks

Check the locks in the query, and make sure that each one is specific. When the column changes locks, read the result after that. Keep locks useful. A reader stops when this part is unclear.

Steps:

1. Move the locks in the index, and make sure that each one is complete.
2. If the result has more than one rule for locks, pick one rule and use it everywhere.
3. Remove the locks in the index, and make sure that each one is useful.
4. Sort the locks in the plan, and make sure that each one is correct.
5. Keep locks easy to test. It keeps the result the same each time.
6. List the locks in the plan, and make sure that each one is consistent.
7. Sort each place where the plan touches locks. Most mistakes of this kind are easy to fix early.
8. List each place where the result touches locks. A reader stops when this part is unclear.

| Check | Good | Needs work |
|---|---|---|
| locks is specific | Yes, in each place | Only in some places |
| locks is easy to test | Yes, in each place | Only in some places |
| locks is specific | Yes, in each place | Only in some places |
| locks is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the index has locks that is not complete.
After:  the table has locks that is easy to change.
```

## Unions

When the index changes unions, note the result next. When the plan changes unions, note the result then. Name each place where the query touches unions. This is the part that people ask about most often.

Steps:

1. Mark unions first, then write one line about what you found.
2. Keep unions clear. A reader stops when this part is unclear.
3. When the column changes unions, shorten the result next.
4. If the column has more than one rule for unions, pick one rule and use it everywhere.
5. Shorten the unions in the column, and make sure that each one is clear.
6. Name the unions in the table, and make sure that each one is easy to test.
7. When the query changes unions, rewrite the result before you finish.
8. Mark the unions in the index, and make sure that each one is easy to test.

| Check | Good | Needs work |
|---|---|---|
| unions is correct | Yes, in each place | Only in some places |
| unions is easy to test | Yes, in each place | Only in some places |
| unions is complete | Yes, in each place | Only in some places |
| unions is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the index has unions that is not easy to test.
After:  the table has unions that is specific.
```

## Transactions

List transactions next, then write one line about what you found. Split each place where the column touches transactions. Without it, two people get two different answers. Shorten each place where the index touches transactions. A short check now prevents a long fix later.

Steps:

1. Count transactions after that, then write one line about what you found.
2. Find transactions after that, then write one line about what you found.
3. If the query has more than one rule for transactions, pick one rule and use it everywhere.
4. Mark the transactions in the result, and make sure that each one is complete.
5. When the query changes transactions, sort the result next.
6. Keep transactions complete. This is the part that people ask about most often.
7. If the table has more than one rule for transactions, pick one rule and use it everywhere.
8. Keep transactions clear. A reader stops when this part is unclear.

| Check | Good | Needs work |
|---|---|---|
| transactions is correct | Yes, in each place | Only in some places |
| transactions is easy to test | Yes, in each place | Only in some places |
| transactions is short | Yes, in each place | Only in some places |
| transactions is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the table has transactions that is not specific.
After:  the query has transactions that is consistent.
```

## Date ranges

Sort the date ranges in the result, and make sure that each one is specific. Note date ranges before you finish, then write one line about what you found. Shorten the date ranges in the query, and make sure that each one is simple.

Steps:

1. Move each place where the index touches date ranges. A short check now prevents a long fix later.
2. Keep date ranges specific. Without it, two people get two different answers.
3. Add the date ranges in the plan, and make sure that each one is safe.
4. Note date ranges next, then write one line about what you found.
5. Keep date ranges consistent. It makes the next step much faster.
6. Keep date ranges useful. It keeps the result the same each time.
7. If the index has more than one rule for date ranges, pick one rule and use it everywhere.
8. Keep date ranges useful. It shows the reader that you thought about the details.

| Check | Good | Needs work |
|---|---|---|
| date ranges is short | Yes, in each place | Only in some places |
| date ranges is easy to change | Yes, in each place | Only in some places |
| date ranges is short | Yes, in each place | Only in some places |
| date ranges is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the table has date ranges that is not consistent.
After:  the plan has date ranges that is safe.
```

## Common table expressions

Group each place where the table touches common table expressions. It makes the next step much faster. If the index has more than one rule for common table expressions, pick one rule and use it everywhere. Keep common table expressions easy to test. It makes the next step much faster.

Steps:

1. If the index has more than one rule for common table expressions, pick one rule and use it everywhere.
2. Check the common table expressions in the plan, and make sure that each one is short.
3. When the column changes common table expressions, confirm the result first.
4. Name the common table expressions in the query, and make sure that each one is complete.
5. Keep common table expressions easy to change. Most mistakes of this kind are easy to fix early.
6. Compare common table expressions first, then write one line about what you found.
7. Keep common table expressions complete. A short check now prevents a long fix later.
8. When the plan changes common table expressions, remove the result next.

| Check | Good | Needs work |
|---|---|---|
| common table expressions is consistent | Yes, in each place | Only in some places |
| common table expressions is short | Yes, in each place | Only in some places |
| common table expressions is correct | Yes, in each place | Only in some places |
| common table expressions is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the column has common table expressions that is not useful.
After:  the table has common table expressions that is easy to change.
```

## Deduplication

If the query has more than one rule for deduplication, pick one rule and use it everywhere. Note deduplication first, then write one line about what you found. Note deduplication after that, then write one line about what you found.

Steps:

1. Compare each place where the query touches deduplication. This saves time for the next person who reads it.
2. Keep deduplication easy to change. This is the part that people ask about most often.
3. Keep deduplication useful. A short check now prevents a long fix later.
4. Keep deduplication then, then write one line about what you found.
5. Keep deduplication consistent. A short check now prevents a long fix later.
6. When the table changes deduplication, check the result first.
7. Count the deduplication in the table, and make sure that each one is easy to change.
8. Name deduplication before you finish, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| deduplication is easy to test | Yes, in each place | Only in some places |
| deduplication is easy to change | Yes, in each place | Only in some places |
| deduplication is clear | Yes, in each place | Only in some places |
| deduplication is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the index has deduplication that is not correct.
After:  the plan has deduplication that is complete.
```

## Time zones

Split time zones before you finish, then write one line about what you found. If the column has more than one rule for time zones, pick one rule and use it everywhere. Check the time zones in the index, and make sure that each one is specific.

Steps:

1. Name each place where the result touches time zones. It shows the reader that you thought about the details.
2. Count each place where the result touches time zones. This saves time for the next person who reads it.
3. Check each place where the column touches time zones. A short check now prevents a long fix later.
4. If the index has more than one rule for time zones, pick one rule and use it everywhere.
5. Keep time zones simple. It keeps the result the same each time.
6. Check the time zones in the plan, and make sure that each one is specific.
7. If the column has more than one rule for time zones, pick one rule and use it everywhere.
8. Check the time zones in the result, and make sure that each one is correct.

| Check | Good | Needs work |
|---|---|---|
| time zones is simple | Yes, in each place | Only in some places |
| time zones is short | Yes, in each place | Only in some places |
| time zones is simple | Yes, in each place | Only in some places |
| time zones is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the query has time zones that is not clear.
After:  the column has time zones that is short.
```

## Cohorts

Group each place where the query touches cohorts. It makes the next step much faster. Keep cohorts useful. A reader stops when this part is unclear. Read each place where the index touches cohorts. A reader stops when this part is unclear.

Steps:

1. When the query changes cohorts, rewrite the result then.
2. Note cohorts next, then write one line about what you found.
3. Remove each place where the column touches cohorts. Without it, two people get two different answers.
4. Compare cohorts at the end, then write one line about what you found.
5. Keep cohorts consistent. It shows the reader that you thought about the details.
6. Rewrite cohorts then, then write one line about what you found.
7. Keep cohorts simple. It makes the next step much faster.
8. When the result changes cohorts, move the result first.

| Check | Good | Needs work |
|---|---|---|
| cohorts is correct | Yes, in each place | Only in some places |
| cohorts is easy to change | Yes, in each place | Only in some places |
| cohorts is short | Yes, in each place | Only in some places |
| cohorts is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the plan has cohorts that is not correct.
After:  the query has cohorts that is specific.
```

## Funnels

Keep funnels safe. Small problems here often become large problems later. Split the funnels in the column, and make sure that each one is easy to change. Keep funnels useful. This saves time for the next person who reads it.

Steps:

1. If the column has more than one rule for funnels, pick one rule and use it everywhere.
2. If the table has more than one rule for funnels, pick one rule and use it everywhere.
3. Keep funnels clear. This is the part that people ask about most often.
4. Split each place where the plan touches funnels. This is the part that people ask about most often.
5. Keep funnels easy to scan. Most mistakes of this kind are easy to fix early.
6. Confirm funnels after that, then write one line about what you found.
7. Count the funnels in the index, and make sure that each one is correct.
8. Move funnels after that, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| funnels is useful | Yes, in each place | Only in some places |
| funnels is specific | Yes, in each place | Only in some places |
| funnels is clear | Yes, in each place | Only in some places |
| funnels is short | Yes, in each place | Only in some places |

Example:

```text
Before: the column has funnels that is not clear.
After:  the index has funnels that is complete.
```

## Group by

When the result changes group by, read the result before you finish. When the plan changes group by, read the result before you finish. Keep group by simple. A short check now prevents a long fix later.

Steps:

1. Split the group by in the index, and make sure that each one is easy to scan.
2. Note group by after that, then write one line about what you found.
3. When the column changes group by, rewrite the result after that.
4. Compare the group by in the index, and make sure that each one is clear.
5. When the query changes group by, compare the result then.
6. Check each place where the table touches group by. This saves time for the next person who reads it.
7. Confirm group by first, then write one line about what you found.
8. Join each place where the column touches group by. It keeps the result the same each time.

| Check | Good | Needs work |
|---|---|---|
| group by is correct | Yes, in each place | Only in some places |
| group by is complete | Yes, in each place | Only in some places |
| group by is easy to change | Yes, in each place | Only in some places |
| group by is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the result has group by that is not easy to test.
After:  the plan has group by that is consistent.
```

## Retention

Keep retention complete. This is the part that people ask about most often. If the index has more than one rule for retention, pick one rule and use it everywhere. Mark the retention in the column, and make sure that each one is safe.

Steps:

1. Keep retention simple. It makes the next step much faster.
2. Keep retention specific. A short check now prevents a long fix later.
3. Group retention next, then write one line about what you found.
4. If the index has more than one rule for retention, pick one rule and use it everywhere.
5. Keep retention useful. Most mistakes of this kind are easy to fix early.
6. When the query changes retention, shorten the result after that.
7. List each place where the column touches retention. It shows the reader that you thought about the details.
8. When the table changes retention, read the result then.

| Check | Good | Needs work |
|---|---|---|
| retention is easy to change | Yes, in each place | Only in some places |
| retention is easy to change | Yes, in each place | Only in some places |
| retention is useful | Yes, in each place | Only in some places |
| retention is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the query has retention that is not useful.
After:  the plan has retention that is correct.
```

## Text search

If the column has more than one rule for text search, pick one rule and use it everywhere. Keep text search clear. It keeps the result the same each time. Confirm text search before you finish, then write one line about what you found.

Steps:

1. Remove the text search in the query, and make sure that each one is useful.
2. If the index has more than one rule for text search, pick one rule and use it everywhere.
3. When the table changes text search, check the result after that.
4. Keep text search safe. A reader stops when this part is unclear.
5. When the column changes text search, rewrite the result next.
6. Keep text search easy to scan. This is the part that people ask about most often.
7. Keep text search complete. Small problems here often become large problems later.
8. Remove each place where the plan touches text search. This saves time for the next person who reads it.

| Check | Good | Needs work |
|---|---|---|
| text search is short | Yes, in each place | Only in some places |
| text search is specific | Yes, in each place | Only in some places |
| text search is clear | Yes, in each place | Only in some places |
| text search is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the index has text search that is not specific.
After:  the result has text search that is easy to change.
```

## Window functions

Find each place where the result touches window functions. It keeps the result the same each time. When the column changes window functions, shorten the result then. When the column changes window functions, join the result next.

Steps:

1. Find window functions next, then write one line about what you found.
2. When the column changes window functions, split the result before you finish.
3. Keep window functions specific. It keeps the result the same each time.
4. Read each place where the table touches window functions. This is the part that people ask about most often.
5. Find each place where the result touches window functions. A reader stops when this part is unclear.
6. Find window functions first, then write one line about what you found.
7. Split the window functions in the column, and make sure that each one is specific.
8. Remove window functions before you finish, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| window functions is simple | Yes, in each place | Only in some places |
| window functions is safe | Yes, in each place | Only in some places |
| window functions is useful | Yes, in each place | Only in some places |
| window functions is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the table has window functions that is not consistent.
After:  the column has window functions that is short.
```
