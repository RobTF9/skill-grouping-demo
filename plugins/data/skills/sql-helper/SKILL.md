---
name: sql-helper
description: Write and explain SQL queries for a Postgres database.
---

# SQL helper

Write the query, then explain it in plain words, one clause at a time.

## Steps

1. Ask which tables the question needs, when it is not clear.
2. Write the query with one clause on each line.
3. Use the column names of [the schema notes](references/schema.md).
4. Add a `LIMIT` to each query that returns rows.
5. Explain what each join does and why it is there.

## Rules

- Never write `SELECT *` in a query that someone will keep.
- Prefer a CTE to a nested subquery when the query has more than two steps.
- Name each CTE for what it holds: `active_teams`, not `t1`.
- Use `COALESCE` for each sum that can be empty.

## Speed

Read [the speed notes](references/performance.md) before you suggest an index.
