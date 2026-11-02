# Speed notes

- Filter on an indexed column first.
- Read the plan with `EXPLAIN ANALYZE` before you add an index.
- A partial index helps when most queries filter on one value.
- Group by the smallest set of columns that answers the question.
