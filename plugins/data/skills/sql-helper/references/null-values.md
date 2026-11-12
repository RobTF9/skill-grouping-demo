# Null values

## Partitions

When the query changes partitions, read the result after that. Shorten partitions then, then write one line about what you found. Sort each place where the plan touches partitions. Small problems here often become large problems later.

Steps:

1. When the plan changes partitions, compare the result first.
2. Shorten the partitions in the plan, and make sure that each one is useful.
3. Add the partitions in the plan, and make sure that each one is clear.
4. Note the partitions in the table, and make sure that each one is specific.
5. If the plan has more than one rule for partitions, pick one rule and use it everywhere.
6. Sort each place where the plan touches partitions. It shows the reader that you thought about the details.
7. Group partitions at the end, then write one line about what you found.
8. When the column changes partitions, remove the result before you finish.

| Check | Good | Needs work |
|---|---|---|
| partitions is complete | Yes, in each place | Only in some places |
| partitions is complete | Yes, in each place | Only in some places |
| partitions is consistent | Yes, in each place | Only in some places |
| partitions is easy to scan | Yes, in each place | Only in some places |

Example:

```text
Before: the plan has partitions that is not easy to test.
After:  the plan has partitions that is consistent.
```

## Unions

Note unions before you finish, then write one line about what you found. Move unions before you finish, then write one line about what you found. If the query has more than one rule for unions, pick one rule and use it everywhere.

Steps:

1. If the result has more than one rule for unions, pick one rule and use it everywhere.
2. Keep unions easy to scan. A short check now prevents a long fix later.
3. If the table has more than one rule for unions, pick one rule and use it everywhere.
4. Keep unions correct. It shows the reader that you thought about the details.
5. When the query changes unions, remove the result at the end.
6. Rewrite unions next, then write one line about what you found.
7. Count each place where the query touches unions. Small problems here often become large problems later.
8. Split each place where the result touches unions. Small problems here often become large problems later.

| Check | Good | Needs work |
|---|---|---|
| unions is short | Yes, in each place | Only in some places |
| unions is useful | Yes, in each place | Only in some places |
| unions is easy to scan | Yes, in each place | Only in some places |
| unions is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the table has unions that is not easy to test.
After:  the result has unions that is easy to change.
```

## Explain plans

Keep explain plans short. It keeps the result the same each time. Find the explain plans in the result, and make sure that each one is clear. Keep explain plans specific. It shows the reader that you thought about the details.

Steps:

1. If the column has more than one rule for explain plans, pick one rule and use it everywhere.
2. Keep explain plans specific. A short check now prevents a long fix later.
3. Join the explain plans in the plan, and make sure that each one is easy to test.
4. When the query changes explain plans, join the result next.
5. When the index changes explain plans, count the result next.
6. Remove explain plans at the end, then write one line about what you found.
7. Find the explain plans in the index, and make sure that each one is safe.
8. Join the explain plans in the result, and make sure that each one is easy to test.

| Check | Good | Needs work |
|---|---|---|
| explain plans is easy to test | Yes, in each place | Only in some places |
| explain plans is useful | Yes, in each place | Only in some places |
| explain plans is safe | Yes, in each place | Only in some places |
| explain plans is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the index has explain plans that is not specific.
After:  the plan has explain plans that is easy to scan.
```

## Date ranges

Split each place where the column touches date ranges. It makes the next step much faster. Keep date ranges easy to scan. Without it, two people get two different answers. Note date ranges after that, then write one line about what you found.

Steps:

1. Confirm the date ranges in the column, and make sure that each one is complete.
2. Mark each place where the query touches date ranges. Small problems here often become large problems later.
3. When the result changes date ranges, rewrite the result next.
4. Mark each place where the plan touches date ranges. It makes the next step much faster.
5. If the plan has more than one rule for date ranges, pick one rule and use it everywhere.
6. Join each place where the query touches date ranges. It keeps the result the same each time.
7. List date ranges at the end, then write one line about what you found.
8. Keep date ranges consistent. It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| date ranges is short | Yes, in each place | Only in some places |
| date ranges is safe | Yes, in each place | Only in some places |
| date ranges is correct | Yes, in each place | Only in some places |
| date ranges is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the column has date ranges that is not simple.
After:  the plan has date ranges that is correct.
```

## Sampling

Mark each place where the query touches sampling. It makes the next step much faster. When the table changes sampling, split the result after that. Check each place where the result touches sampling. A reader stops when this part is unclear.

Steps:

1. Count each place where the result touches sampling. Without it, two people get two different answers.
2. Keep sampling easy to change. This is the part that people ask about most often.
3. Keep sampling simple. It makes the next step much faster.
4. When the column changes sampling, remove the result then.
5. When the result changes sampling, check the result first.
6. When the table changes sampling, compare the result at the end.
7. If the query has more than one rule for sampling, pick one rule and use it everywhere.
8. Keep sampling consistent. It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| sampling is consistent | Yes, in each place | Only in some places |
| sampling is easy to test | Yes, in each place | Only in some places |
| sampling is complete | Yes, in each place | Only in some places |
| sampling is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the plan has sampling that is not useful.
After:  the query has sampling that is safe.
```

## Cohorts

Shorten cohorts at the end, then write one line about what you found. Shorten cohorts after that, then write one line about what you found. Rewrite cohorts before you finish, then write one line about what you found.

Steps:

1. Sort each place where the table touches cohorts. It keeps the result the same each time.
2. Keep cohorts clear. Without it, two people get two different answers.
3. Name cohorts before you finish, then write one line about what you found.
4. Note cohorts after that, then write one line about what you found.
5. When the query changes cohorts, mark the result then.
6. Note each place where the table touches cohorts. Small problems here often become large problems later.
7. Check the cohorts in the index, and make sure that each one is clear.
8. Name the cohorts in the result, and make sure that each one is specific.

| Check | Good | Needs work |
|---|---|---|
| cohorts is specific | Yes, in each place | Only in some places |
| cohorts is easy to change | Yes, in each place | Only in some places |
| cohorts is useful | Yes, in each place | Only in some places |
| cohorts is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the column has cohorts that is not easy to change.
After:  the plan has cohorts that is specific.
```

## Joins

Mark joins at the end, then write one line about what you found. Keep joins short. It shows the reader that you thought about the details. Keep joins first, then write one line about what you found.

Steps:

1. When the result changes joins, rewrite the result before you finish.
2. Keep joins easy to test. It makes the next step much faster.
3. When the plan changes joins, shorten the result at the end.
4. Keep joins easy to test. Without it, two people get two different answers.
5. Read the joins in the index, and make sure that each one is correct.
6. If the result has more than one rule for joins, pick one rule and use it everywhere.
7. Group the joins in the query, and make sure that each one is clear.
8. If the index has more than one rule for joins, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| joins is safe | Yes, in each place | Only in some places |
| joins is easy to scan | Yes, in each place | Only in some places |
| joins is simple | Yes, in each place | Only in some places |
| joins is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the column has joins that is not complete.
After:  the column has joins that is complete.
```

## Window functions

Add each place where the result touches window functions. This saves time for the next person who reads it. Move each place where the table touches window functions. Most mistakes of this kind are easy to fix early. When the index changes window functions, read the result before you finish.

Steps:

1. When the query changes window functions, count the result after that.
2. Read window functions then, then write one line about what you found.
3. If the column has more than one rule for window functions, pick one rule and use it everywhere.
4. If the result has more than one rule for window functions, pick one rule and use it everywhere.
5. Split the window functions in the column, and make sure that each one is complete.
6. Group each place where the query touches window functions. A short check now prevents a long fix later.
7. Split each place where the query touches window functions. It shows the reader that you thought about the details.
8. Group each place where the query touches window functions. This saves time for the next person who reads it.

| Check | Good | Needs work |
|---|---|---|
| window functions is clear | Yes, in each place | Only in some places |
| window functions is useful | Yes, in each place | Only in some places |
| window functions is clear | Yes, in each place | Only in some places |
| window functions is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the plan has window functions that is not easy to scan.
After:  the query has window functions that is useful.
```

## Funnels

If the index has more than one rule for funnels, pick one rule and use it everywhere. Check funnels after that, then write one line about what you found. Move funnels after that, then write one line about what you found.

Steps:

1. Find the funnels in the result, and make sure that each one is short.
2. If the column has more than one rule for funnels, pick one rule and use it everywhere.
3. Read funnels then, then write one line about what you found.
4. When the plan changes funnels, name the result then.
5. List funnels at the end, then write one line about what you found.
6. If the query has more than one rule for funnels, pick one rule and use it everywhere.
7. Keep funnels clear. A short check now prevents a long fix later.
8. When the result changes funnels, confirm the result first.

| Check | Good | Needs work |
|---|---|---|
| funnels is easy to change | Yes, in each place | Only in some places |
| funnels is easy to change | Yes, in each place | Only in some places |
| funnels is easy to test | Yes, in each place | Only in some places |
| funnels is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the result has funnels that is not complete.
After:  the query has funnels that is easy to change.
```

## Time zones

When the column changes time zones, find the result next. Confirm time zones then, then write one line about what you found. Keep time zones useful. Small problems here often become large problems later.

Steps:

1. When the query changes time zones, move the result first.
2. If the plan has more than one rule for time zones, pick one rule and use it everywhere.
3. When the column changes time zones, list the result before you finish.
4. Keep time zones simple. It makes the next step much faster.
5. Keep time zones safe. Small problems here often become large problems later.
6. When the table changes time zones, rewrite the result after that.
7. Join time zones after that, then write one line about what you found.
8. When the column changes time zones, join the result then.

| Check | Good | Needs work |
|---|---|---|
| time zones is easy to scan | Yes, in each place | Only in some places |
| time zones is easy to scan | Yes, in each place | Only in some places |
| time zones is complete | Yes, in each place | Only in some places |
| time zones is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the plan has time zones that is not clear.
After:  the table has time zones that is easy to change.
```

## Locks

If the query has more than one rule for locks, pick one rule and use it everywhere. Keep locks specific. It shows the reader that you thought about the details. If the index has more than one rule for locks, pick one rule and use it everywhere.

Steps:

1. If the result has more than one rule for locks, pick one rule and use it everywhere.
2. Note locks before you finish, then write one line about what you found.
3. Join locks then, then write one line about what you found.
4. Keep locks clear. A short check now prevents a long fix later.
5. When the plan changes locks, split the result after that.
6. Confirm locks then, then write one line about what you found.
7. Note locks after that, then write one line about what you found.
8. Compare each place where the plan touches locks. Most mistakes of this kind are easy to fix early.

| Check | Good | Needs work |
|---|---|---|
| locks is clear | Yes, in each place | Only in some places |
| locks is easy to change | Yes, in each place | Only in some places |
| locks is complete | Yes, in each place | Only in some places |
| locks is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the index has locks that is not clear.
After:  the result has locks that is clear.
```

## JSON columns

When the table changes JSON columns, join the result after that. Name each place where the result touches JSON columns. A short check now prevents a long fix later. Sort each place where the column touches JSON columns. It makes the next step much faster.

Steps:

1. Note the JSON columns in the query, and make sure that each one is useful.
2. If the plan has more than one rule for JSON columns, pick one rule and use it everywhere.
3. Keep JSON columns specific. It keeps the result the same each time.
4. If the plan has more than one rule for JSON columns, pick one rule and use it everywhere.
5. If the table has more than one rule for JSON columns, pick one rule and use it everywhere.
6. Name JSON columns after that, then write one line about what you found.
7. If the column has more than one rule for JSON columns, pick one rule and use it everywhere.
8. Name the JSON columns in the query, and make sure that each one is useful.

| Check | Good | Needs work |
|---|---|---|
| JSON columns is short | Yes, in each place | Only in some places |
| JSON columns is useful | Yes, in each place | Only in some places |
| JSON columns is consistent | Yes, in each place | Only in some places |
| JSON columns is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the index has JSON columns that is not consistent.
After:  the column has JSON columns that is simple.
```

## Common table expressions

Keep common table expressions correct. It shows the reader that you thought about the details. Rewrite the common table expressions in the result, and make sure that each one is useful. If the column has more than one rule for common table expressions, pick one rule and use it everywhere.

Steps:

1. Shorten common table expressions then, then write one line about what you found.
2. Count the common table expressions in the plan, and make sure that each one is specific.
3. Compare the common table expressions in the result, and make sure that each one is correct.
4. Keep common table expressions at the end, then write one line about what you found.
5. If the plan has more than one rule for common table expressions, pick one rule and use it everywhere.
6. Add each place where the result touches common table expressions. Without it, two people get two different answers.
7. When the column changes common table expressions, remove the result before you finish.
8. When the plan changes common table expressions, find the result next.

| Check | Good | Needs work |
|---|---|---|
| common table expressions is easy to change | Yes, in each place | Only in some places |
| common table expressions is easy to change | Yes, in each place | Only in some places |
| common table expressions is useful | Yes, in each place | Only in some places |
| common table expressions is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the table has common table expressions that is not easy to test.
After:  the plan has common table expressions that is useful.
```

## Null values

Keep null values simple. This is the part that people ask about most often. Check the null values in the plan, and make sure that each one is simple. When the plan changes null values, list the result first.

Steps:

1. Keep null values easy to test. This is the part that people ask about most often.
2. Move null values after that, then write one line about what you found.
3. Mark each place where the index touches null values. It keeps the result the same each time.
4. Keep null values easy to change. A reader stops when this part is unclear.
5. Read each place where the query touches null values. It keeps the result the same each time.
6. If the index has more than one rule for null values, pick one rule and use it everywhere.
7. If the index has more than one rule for null values, pick one rule and use it everywhere.
8. Mark null values next, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| null values is short | Yes, in each place | Only in some places |
| null values is clear | Yes, in each place | Only in some places |
| null values is safe | Yes, in each place | Only in some places |
| null values is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the plan has null values that is not correct.
After:  the index has null values that is clear.
```

## Retention

Sort retention next, then write one line about what you found. If the result has more than one rule for retention, pick one rule and use it everywhere. Keep retention specific. Most mistakes of this kind are easy to fix early.

Steps:

1. List the retention in the plan, and make sure that each one is short.
2. If the result has more than one rule for retention, pick one rule and use it everywhere.
3. Compare each place where the query touches retention. It makes the next step much faster.
4. Add the retention in the index, and make sure that each one is consistent.
5. Sort retention then, then write one line about what you found.
6. Name each place where the column touches retention. This is the part that people ask about most often.
7. When the plan changes retention, name the result at the end.
8. Keep retention specific. It makes the next step much faster.

| Check | Good | Needs work |
|---|---|---|
| retention is easy to change | Yes, in each place | Only in some places |
| retention is correct | Yes, in each place | Only in some places |
| retention is easy to test | Yes, in each place | Only in some places |
| retention is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the index has retention that is not useful.
After:  the index has retention that is consistent.
```

## Percentiles

Mark each place where the result touches percentiles. Without it, two people get two different answers. Keep percentiles complete. A reader stops when this part is unclear. Keep percentiles short. It makes the next step much faster.

Steps:

1. When the index changes percentiles, join the result after that.
2. Keep percentiles easy to change. Without it, two people get two different answers.
3. Confirm each place where the plan touches percentiles. It keeps the result the same each time.
4. Keep percentiles easy to test. Without it, two people get two different answers.
5. Group the percentiles in the plan, and make sure that each one is simple.
6. Keep percentiles useful. It makes the next step much faster.
7. Keep percentiles useful. Small problems here often become large problems later.
8. Find each place where the table touches percentiles. It shows the reader that you thought about the details.

| Check | Good | Needs work |
|---|---|---|
| percentiles is complete | Yes, in each place | Only in some places |
| percentiles is easy to change | Yes, in each place | Only in some places |
| percentiles is complete | Yes, in each place | Only in some places |
| percentiles is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the query has percentiles that is not simple.
After:  the column has percentiles that is specific.
```

## Indexes

Confirm each place where the table touches indexes. Small problems here often become large problems later. If the query has more than one rule for indexes, pick one rule and use it everywhere. If the table has more than one rule for indexes, pick one rule and use it everywhere.

Steps:

1. Note indexes at the end, then write one line about what you found.
2. Check the indexes in the result, and make sure that each one is simple.
3. Note each place where the query touches indexes. This is the part that people ask about most often.
4. If the column has more than one rule for indexes, pick one rule and use it everywhere.
5. If the plan has more than one rule for indexes, pick one rule and use it everywhere.
6. When the plan changes indexes, name the result after that.
7. If the plan has more than one rule for indexes, pick one rule and use it everywhere.
8. List indexes first, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| indexes is simple | Yes, in each place | Only in some places |
| indexes is useful | Yes, in each place | Only in some places |
| indexes is useful | Yes, in each place | Only in some places |
| indexes is short | Yes, in each place | Only in some places |

Example:

```text
Before: the column has indexes that is not easy to test.
After:  the index has indexes that is specific.
```

## Subqueries

When the table changes subqueries, check the result at the end. Group the subqueries in the column, and make sure that each one is clear. Split the subqueries in the plan, and make sure that each one is easy to scan.

Steps:

1. Mark the subqueries in the query, and make sure that each one is consistent.
2. When the index changes subqueries, compare the result then.
3. When the query changes subqueries, sort the result at the end.
4. Read the subqueries in the plan, and make sure that each one is easy to scan.
5. Group the subqueries in the index, and make sure that each one is consistent.
6. Keep subqueries safe. This saves time for the next person who reads it.
7. List subqueries after that, then write one line about what you found.
8. If the query has more than one rule for subqueries, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| subqueries is easy to scan | Yes, in each place | Only in some places |
| subqueries is safe | Yes, in each place | Only in some places |
| subqueries is easy to test | Yes, in each place | Only in some places |
| subqueries is specific | Yes, in each place | Only in some places |

Example:

```text
Before: the column has subqueries that is not short.
After:  the plan has subqueries that is easy to scan.
```

## Group by

If the plan has more than one rule for group by, pick one rule and use it everywhere. Mark each place where the column touches group by. It keeps the result the same each time. Find each place where the result touches group by. Small problems here often become large problems later.

Steps:

1. Split the group by in the table, and make sure that each one is easy to test.
2. If the query has more than one rule for group by, pick one rule and use it everywhere.
3. Name group by first, then write one line about what you found.
4. Keep group by short. Without it, two people get two different answers.
5. Split each place where the plan touches group by. A reader stops when this part is unclear.
6. When the table changes group by, shorten the result first.
7. Confirm each place where the table touches group by. Small problems here often become large problems later.
8. If the query has more than one rule for group by, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| group by is specific | Yes, in each place | Only in some places |
| group by is complete | Yes, in each place | Only in some places |
| group by is clear | Yes, in each place | Only in some places |
| group by is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the query has group by that is not easy to test.
After:  the plan has group by that is complete.
```
