# Paging notes

- Use a cursor, not an offset, for each list that can grow.
- Return `nextCursor` as null on the last page.
- Cap the page size at 100.
