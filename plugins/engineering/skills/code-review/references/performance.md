# Speed notes

- Measure before you change code for speed. Put the numbers in the pull request.
- One query for a list, not one for each item.
- Add an index for each new filter on a large table.
- Stream a large file. Do not read it into memory.
- Put a limit on each list that a user controls.
- A cache needs a size limit, an expiry and an owner.
- Avoid work in a render function. Compute it once, outside.
- Debounce input that starts a request.
