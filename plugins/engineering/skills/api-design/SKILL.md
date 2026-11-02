---
name: api-design
description: Design a REST endpoint with its path, method, status codes and errors.
---

# API design

Design the endpoint before you write code. Write the design as a short table, then the examples.

## Steps

1. Name the resource as a plural noun: `/invoices`.
2. Pick the method: GET reads, POST creates, PATCH changes, DELETE removes.
3. List each status code that the endpoint returns, and when.
4. Write the error body as [the error notes](references/errors.md) say.
5. Add paging to each list, as [the paging notes](references/paging.md) say.

## Rules

- Never put a verb in a path.
- Return the created object from a POST.
- Accept and return dates in ISO 8601, in UTC.
