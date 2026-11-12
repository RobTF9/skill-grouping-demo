# Speed notes

- Filter on an indexed column first.
- Read the plan with `EXPLAIN ANALYZE` before you add an index.
- A partial index helps when most queries filter on one value.
- Group by the smallest set of columns that answers the question.

## More detail

## Window functions

Check window functions at the end, then write one line about what you found. When the index changes window functions, shorten the result first. Join the window functions in the query, and make sure that each one is short.

Steps:

1. If the result has more than one rule for window functions, pick one rule and use it everywhere.
2. If the query has more than one rule for window functions, pick one rule and use it everywhere.
3. Keep window functions safe. Small problems here often become large problems later.
4. Note the window functions in the table, and make sure that each one is specific.
5. Confirm window functions before you finish, then write one line about what you found.
6. When the index changes window functions, name the result after that.
7. Check each place where the index touches window functions. It shows the reader that you thought about the details.
8. If the index has more than one rule for window functions, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| window functions is simple | Yes, in each place | Only in some places |
| window functions is consistent | Yes, in each place | Only in some places |
| window functions is useful | Yes, in each place | Only in some places |
| window functions is useful | Yes, in each place | Only in some places |

Example:

```text
Before: the plan has window functions that is not easy to change.
After:  the index has window functions that is short.
```

## Explain plans

Check explain plans next, then write one line about what you found. If the table has more than one rule for explain plans, pick one rule and use it everywhere. When the plan changes explain plans, group the result after that.

Steps:

1. When the table changes explain plans, check the result after that.
2. Read the explain plans in the query, and make sure that each one is easy to test.
3. Rewrite explain plans next, then write one line about what you found.
4. Keep explain plans correct. It shows the reader that you thought about the details.
5. Keep explain plans useful. It keeps the result the same each time.
6. Mark the explain plans in the query, and make sure that each one is consistent.
7. Compare the explain plans in the result, and make sure that each one is complete.
8. Add the explain plans in the query, and make sure that each one is easy to change.

| Check | Good | Needs work |
|---|---|---|
| explain plans is useful | Yes, in each place | Only in some places |
| explain plans is useful | Yes, in each place | Only in some places |
| explain plans is complete | Yes, in each place | Only in some places |
| explain plans is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the result has explain plans that is not easy to change.
After:  the index has explain plans that is consistent.
```

## Upserts

Keep upserts consistent. A short check now prevents a long fix later. Keep upserts easy to test. A reader stops when this part is unclear. Keep upserts easy to test. Without it, two people get two different answers.

Steps:

1. Add upserts at the end, then write one line about what you found.
2. Find the upserts in the result, and make sure that each one is correct.
3. If the column has more than one rule for upserts, pick one rule and use it everywhere.
4. Keep upserts complete. It makes the next step much faster.
5. Keep upserts short. It shows the reader that you thought about the details.
6. Mark the upserts in the result, and make sure that each one is easy to scan.
7. Sort upserts then, then write one line about what you found.
8. Group each place where the result touches upserts. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| upserts is complete | Yes, in each place | Only in some places |
| upserts is correct | Yes, in each place | Only in some places |
| upserts is complete | Yes, in each place | Only in some places |
| upserts is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the index has upserts that is not correct.
After:  the index has upserts that is easy to change.
```

## Joins

Move joins after that, then write one line about what you found. When the column changes joins, keep the result after that. Count joins after that, then write one line about what you found.

Steps:

1. Keep joins easy to change. A short check now prevents a long fix later.
2. If the query has more than one rule for joins, pick one rule and use it everywhere.
3. Join each place where the index touches joins. It keeps the result the same each time.
4. If the query has more than one rule for joins, pick one rule and use it everywhere.
5. If the result has more than one rule for joins, pick one rule and use it everywhere.
6. If the index has more than one rule for joins, pick one rule and use it everywhere.
7. When the table changes joins, note the result first.
8. When the plan changes joins, rewrite the result at the end.

| Check | Good | Needs work |
|---|---|---|
| joins is short | Yes, in each place | Only in some places |
| joins is complete | Yes, in each place | Only in some places |
| joins is clear | Yes, in each place | Only in some places |
| joins is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the result has joins that is not safe.
After:  the plan has joins that is correct.
```

## Group by

Split each place where the query touches group by. It makes the next step much faster. When the index changes group by, add the result then. Split the group by in the table, and make sure that each one is short.

Steps:

1. When the query changes group by, read the result first.
2. Compare group by before you finish, then write one line about what you found.
3. If the index has more than one rule for group by, pick one rule and use it everywhere.
4. When the plan changes group by, count the result after that.
5. List group by then, then write one line about what you found.
6. Group each place where the result touches group by. This is the part that people ask about most often.
7. Add each place where the column touches group by. This saves time for the next person who reads it.
8. When the index changes group by, sort the result then.

| Check | Good | Needs work |
|---|---|---|
| group by is easy to change | Yes, in each place | Only in some places |
| group by is easy to change | Yes, in each place | Only in some places |
| group by is easy to change | Yes, in each place | Only in some places |
| group by is safe | Yes, in each place | Only in some places |

Example:

```text
Before: the table has group by that is not correct.
After:  the table has group by that is short.
```

## Null values

Shorten the null values in the table, and make sure that each one is short. When the result changes null values, group the result first. Mark null values after that, then write one line about what you found.

Steps:

1. Shorten null values before you finish, then write one line about what you found.
2. Confirm null values first, then write one line about what you found.
3. Rewrite null values after that, then write one line about what you found.
4. Check each place where the table touches null values. This saves time for the next person who reads it.
5. Read null values then, then write one line about what you found.
6. If the index has more than one rule for null values, pick one rule and use it everywhere.
7. Group each place where the column touches null values. It keeps the result the same each time.
8. Check each place where the query touches null values. Most mistakes of this kind are easy to fix early.

| Check | Good | Needs work |
|---|---|---|
| null values is correct | Yes, in each place | Only in some places |
| null values is specific | Yes, in each place | Only in some places |
| null values is simple | Yes, in each place | Only in some places |
| null values is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the column has null values that is not short.
After:  the result has null values that is simple.
```

## Text search

Split the text search in the result, and make sure that each one is clear. Remove the text search in the index, and make sure that each one is easy to test. If the table has more than one rule for text search, pick one rule and use it everywhere.

Steps:

1. Check text search next, then write one line about what you found.
2. Remove the text search in the table, and make sure that each one is safe.
3. Check text search then, then write one line about what you found.
4. Join each place where the index touches text search. A reader stops when this part is unclear.
5. When the query changes text search, add the result before you finish.
6. Keep text search easy to scan. Without it, two people get two different answers.
7. If the query has more than one rule for text search, pick one rule and use it everywhere.
8. When the column changes text search, list the result after that.

| Check | Good | Needs work |
|---|---|---|
| text search is clear | Yes, in each place | Only in some places |
| text search is useful | Yes, in each place | Only in some places |
| text search is correct | Yes, in each place | Only in some places |
| text search is correct | Yes, in each place | Only in some places |

Example:

```text
Before: the table has text search that is not useful.
After:  the index has text search that is specific.
```

## Common table expressions

Sort the common table expressions in the plan, and make sure that each one is easy to change. Split common table expressions first, then write one line about what you found. Keep common table expressions useful. Small problems here often become large problems later.

Steps:

1. When the query changes common table expressions, add the result then.
2. When the table changes common table expressions, group the result after that.
3. Keep common table expressions consistent. This is the part that people ask about most often.
4. Keep the common table expressions in the plan, and make sure that each one is useful.
5. Rewrite common table expressions before you finish, then write one line about what you found.
6. Move the common table expressions in the column, and make sure that each one is consistent.
7. Check common table expressions after that, then write one line about what you found.
8. Move the common table expressions in the table, and make sure that each one is simple.

| Check | Good | Needs work |
|---|---|---|
| common table expressions is easy to change | Yes, in each place | Only in some places |
| common table expressions is consistent | Yes, in each place | Only in some places |
| common table expressions is useful | Yes, in each place | Only in some places |
| common table expressions is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the index has common table expressions that is not simple.
After:  the column has common table expressions that is consistent.
```

## JSON columns

Keep JSON columns useful. This saves time for the next person who reads it. Keep JSON columns easy to test. It shows the reader that you thought about the details. Keep JSON columns consistent. Without it, two people get two different answers.

Steps:

1. Check the JSON columns in the index, and make sure that each one is easy to scan.
2. Sort the JSON columns in the index, and make sure that each one is consistent.
3. Keep JSON columns useful. This saves time for the next person who reads it.
4. Remove JSON columns at the end, then write one line about what you found.
5. When the plan changes JSON columns, rewrite the result at the end.
6. Keep JSON columns simple. Most mistakes of this kind are easy to fix early.
7. Add the JSON columns in the plan, and make sure that each one is safe.
8. Note JSON columns after that, then write one line about what you found.

| Check | Good | Needs work |
|---|---|---|
| JSON columns is clear | Yes, in each place | Only in some places |
| JSON columns is safe | Yes, in each place | Only in some places |
| JSON columns is useful | Yes, in each place | Only in some places |
| JSON columns is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the plan has JSON columns that is not useful.
After:  the query has JSON columns that is easy to change.
```

## Date ranges

When the query changes date ranges, check the result next. Move the date ranges in the column, and make sure that each one is consistent. When the plan changes date ranges, move the result first.

Steps:

1. When the plan changes date ranges, name the result before you finish.
2. When the table changes date ranges, name the result before you finish.
3. Compare each place where the result touches date ranges. This saves time for the next person who reads it.
4. Keep date ranges short. Without it, two people get two different answers.
5. If the column has more than one rule for date ranges, pick one rule and use it everywhere.
6. Find the date ranges in the plan, and make sure that each one is easy to change.
7. Keep date ranges safe. This saves time for the next person who reads it.
8. Name each place where the column touches date ranges. It shows the reader that you thought about the details.

| Check | Good | Needs work |
|---|---|---|
| date ranges is specific | Yes, in each place | Only in some places |
| date ranges is clear | Yes, in each place | Only in some places |
| date ranges is safe | Yes, in each place | Only in some places |
| date ranges is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the index has date ranges that is not easy to scan.
After:  the index has date ranges that is safe.
```
