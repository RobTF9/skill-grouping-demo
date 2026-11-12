# Test notes

- A bug fix comes with a test that fails before the fix.
- Test behaviour, not the inside of a function.
- One reason to fail for each test.
- Name the test as a sentence: "sends one email for each invoice".
- Use a fake clock, not a sleep.
- Build test data with a small factory, not a large fixture file.
- Keep each test independent. Order must not matter.

## More detail

## Test coverage

List each place where the test touches test coverage. It makes the next step much faster. When the interface changes test coverage, mark the result first. Remove the test coverage in the function, and make sure that each one is safe.

Steps:

1. When the interface changes test coverage, name the result before you finish.
2. When the change changes test coverage, mark the result first.
3. If the interface has more than one rule for test coverage, pick one rule and use it everywhere.
4. If the change has more than one rule for test coverage, pick one rule and use it everywhere.
5. Name test coverage next, then write one line about what you found.
6. Confirm the test coverage in the function, and make sure that each one is easy to change.
7. Keep test coverage short. Most mistakes of this kind are easy to fix early.
8. If the test has more than one rule for test coverage, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| test coverage is short | Yes, in each place | Only in some places |
| test coverage is easy to test | Yes, in each place | Only in some places |
| test coverage is clear | Yes, in each place | Only in some places |
| test coverage is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the interface has test coverage that is not complete.
After:  the interface has test coverage that is clear.
```

## Database queries

List each place where the function touches database queries. A reader stops when this part is unclear. Keep database queries clear. It shows the reader that you thought about the details. If the interface has more than one rule for database queries, pick one rule and use it everywhere.

Steps:

1. Keep database queries consistent. A reader stops when this part is unclear.
2. If the function has more than one rule for database queries, pick one rule and use it everywhere.
3. Keep database queries short. This is the part that people ask about most often.
4. Find the database queries in the function, and make sure that each one is complete.
5. Move the database queries in the diff, and make sure that each one is consistent.
6. Group the database queries in the function, and make sure that each one is consistent.
7. Shorten database queries after that, then write one line about what you found.
8. If the module has more than one rule for database queries, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| database queries is short | Yes, in each place | Only in some places |
| database queries is useful | Yes, in each place | Only in some places |
| database queries is correct | Yes, in each place | Only in some places |
| database queries is easy to test | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has database queries that is not simple.
After:  the change has database queries that is clear.
```

## Dead code

Note the dead code in the test, and make sure that each one is short. Keep dead code specific. This saves time for the next person who reads it. Confirm the dead code in the module, and make sure that each one is clear.

Steps:

1. Shorten the dead code in the function, and make sure that each one is useful.
2. If the test has more than one rule for dead code, pick one rule and use it everywhere.
3. If the test has more than one rule for dead code, pick one rule and use it everywhere.
4. Split each place where the function touches dead code. A reader stops when this part is unclear.
5. Keep dead code clear. Most mistakes of this kind are easy to fix early.
6. Read each place where the interface touches dead code. It shows the reader that you thought about the details.
7. When the change changes dead code, read the result first.
8. Keep dead code useful. This is the part that people ask about most often.

| Check | Good | Needs work |
|---|---|---|
| dead code is easy to test | Yes, in each place | Only in some places |
| dead code is complete | Yes, in each place | Only in some places |
| dead code is easy to scan | Yes, in each place | Only in some places |
| dead code is clear | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has dead code that is not safe.
After:  the module has dead code that is consistent.
```

## Mocks

Mark the mocks in the module, and make sure that each one is clear. Remove each place where the test touches mocks. Small problems here often become large problems later. Join the mocks in the function, and make sure that each one is consistent.

Steps:

1. When the diff changes mocks, keep the result before you finish.
2. When the change changes mocks, move the result first.
3. When the interface changes mocks, remove the result after that.
4. Keep mocks short. This saves time for the next person who reads it.
5. If the interface has more than one rule for mocks, pick one rule and use it everywhere.
6. If the test has more than one rule for mocks, pick one rule and use it everywhere.
7. Remove the mocks in the test, and make sure that each one is useful.
8. Keep mocks easy to change. Small problems here often become large problems later.

| Check | Good | Needs work |
|---|---|---|
| mocks is consistent | Yes, in each place | Only in some places |
| mocks is useful | Yes, in each place | Only in some places |
| mocks is simple | Yes, in each place | Only in some places |
| mocks is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the change has mocks that is not easy to scan.
After:  the test has mocks that is safe.
```

## Error handling

Split each place where the interface touches error handling. It shows the reader that you thought about the details. When the module changes error handling, shorten the result then. Find each place where the change touches error handling. It shows the reader that you thought about the details.

Steps:

1. Add the error handling in the diff, and make sure that each one is specific.
2. Read error handling then, then write one line about what you found.
3. When the change changes error handling, compare the result after that.
4. Name each place where the function touches error handling. A short check now prevents a long fix later.
5. Keep error handling clear. It keeps the result the same each time.
6. Sort the error handling in the change, and make sure that each one is useful.
7. Keep error handling easy to change. Without it, two people get two different answers.
8. List the error handling in the function, and make sure that each one is useful.

| Check | Good | Needs work |
|---|---|---|
| error handling is useful | Yes, in each place | Only in some places |
| error handling is simple | Yes, in each place | Only in some places |
| error handling is easy to scan | Yes, in each place | Only in some places |
| error handling is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the diff has error handling that is not short.
After:  the diff has error handling that is easy to test.
```

## Queues

Move queues next, then write one line about what you found. Remove queues then, then write one line about what you found. Keep queues consistent. This is the part that people ask about most often.

Steps:

1. When the diff changes queues, name the result at the end.
2. Keep queues after that, then write one line about what you found.
3. Keep queues safe. It makes the next step much faster.
4. Name each place where the function touches queues. It keeps the result the same each time.
5. Keep queues simple. Without it, two people get two different answers.
6. Count queues at the end, then write one line about what you found.
7. Confirm the queues in the diff, and make sure that each one is easy to test.
8. Name the queues in the test, and make sure that each one is simple.

| Check | Good | Needs work |
|---|---|---|
| queues is easy to change | Yes, in each place | Only in some places |
| queues is correct | Yes, in each place | Only in some places |
| queues is correct | Yes, in each place | Only in some places |
| queues is easy to change | Yes, in each place | Only in some places |

Example:

```text
Before: the change has queues that is not short.
After:  the change has queues that is consistent.
```

## Dependency updates

If the interface has more than one rule for dependency updates, pick one rule and use it everywhere. When the module changes dependency updates, rewrite the result at the end. Check dependency updates first, then write one line about what you found.

Steps:

1. Sort each place where the change touches dependency updates. A short check now prevents a long fix later.
2. Remove dependency updates after that, then write one line about what you found.
3. Keep dependency updates complete. Most mistakes of this kind are easy to fix early.
4. If the test has more than one rule for dependency updates, pick one rule and use it everywhere.
5. If the module has more than one rule for dependency updates, pick one rule and use it everywhere.
6. Name each place where the function touches dependency updates. Small problems here often become large problems later.
7. If the test has more than one rule for dependency updates, pick one rule and use it everywhere.
8. Shorten the dependency updates in the interface, and make sure that each one is easy to change.

| Check | Good | Needs work |
|---|---|---|
| dependency updates is consistent | Yes, in each place | Only in some places |
| dependency updates is specific | Yes, in each place | Only in some places |
| dependency updates is correct | Yes, in each place | Only in some places |
| dependency updates is simple | Yes, in each place | Only in some places |

Example:

```text
Before: the test has dependency updates that is not useful.
After:  the function has dependency updates that is easy to test.
```

## Dates and time zones

List each place where the interface touches dates and time zones. Small problems here often become large problems later. Keep dates and time zones specific. This saves time for the next person who reads it. When the diff changes dates and time zones, count the result then.

Steps:

1. Keep dates and time zones useful. A reader stops when this part is unclear.
2. Count each place where the module touches dates and time zones. It makes the next step much faster.
3. Keep dates and time zones complete. A reader stops when this part is unclear.
4. When the change changes dates and time zones, list the result after that.
5. Rewrite the dates and time zones in the change, and make sure that each one is short.
6. Keep dates and time zones specific. This is the part that people ask about most often.
7. Check dates and time zones at the end, then write one line about what you found.
8. Name the dates and time zones in the diff, and make sure that each one is safe.

| Check | Good | Needs work |
|---|---|---|
| dates and time zones is specific | Yes, in each place | Only in some places |
| dates and time zones is clear | Yes, in each place | Only in some places |
| dates and time zones is correct | Yes, in each place | Only in some places |
| dates and time zones is complete | Yes, in each place | Only in some places |

Example:

```text
Before: the function has dates and time zones that is not complete.
After:  the interface has dates and time zones that is complete.
```

## Recursion

When the module changes recursion, add the result after that. Keep recursion short. Most mistakes of this kind are easy to fix early. Read each place where the change touches recursion. It shows the reader that you thought about the details.

Steps:

1. Split each place where the diff touches recursion. Without it, two people get two different answers.
2. Keep recursion easy to test. A reader stops when this part is unclear.
3. If the function has more than one rule for recursion, pick one rule and use it everywhere.
4. List the recursion in the test, and make sure that each one is simple.
5. Split each place where the diff touches recursion. Small problems here often become large problems later.
6. Find each place where the test touches recursion. A reader stops when this part is unclear.
7. Remove each place where the diff touches recursion. Small problems here often become large problems later.
8. If the module has more than one rule for recursion, pick one rule and use it everywhere.

| Check | Good | Needs work |
|---|---|---|
| recursion is short | Yes, in each place | Only in some places |
| recursion is clear | Yes, in each place | Only in some places |
| recursion is complete | Yes, in each place | Only in some places |
| recursion is consistent | Yes, in each place | Only in some places |

Example:

```text
Before: the function has recursion that is not specific.
After:  the function has recursion that is easy to test.
```
