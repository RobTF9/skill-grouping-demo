---
name: code-review
description: Review a pull request for correctness, safety, speed and readability.
---

# Code review

Read the whole diff before you write a comment. List bugs first, then risks, then readability issues. Keep each comment short and say why it matters.

## Before you start

- Read the pull request title and description. Say so when they do not match the diff.
- Find the ticket or issue that the change is for. Check that the change does what the ticket asks.
- Look at the size of the change. A change over 400 lines is hard to review well. Ask the author to split it.
- Check the target branch. A change to a release branch needs a second reviewer.

## Order of the review

1. Correctness: does the code do what it claims to do?
2. Safety: can the change leak data, lose data or let a user do more than they may?
3. Speed: does the change add work to a hot path, a loop or a query?
4. Tests: do the tests fail without the change and pass with it?
5. Readability: can the next engineer change this code without fear?
6. Style: only the points that the linter does not catch.

## Correctness

- Follow each new branch of the code. Name the input that reaches it.
- Check each loop for an off-by-one error at the start and at the end.
- Check what happens with an empty list, a null value and a very large value.
- Check that each error is handled or passed on. An empty catch block is a bug.
- Check that dates use one time zone. Mixed time zones give wrong reports.
- Check that money uses whole numbers of the smallest unit, not floats.

## Safety

Read [the safety notes](references/security.md) for the full list. The short version:

- Every input from a user is untrusted until the code checks it.
- Every query uses parameters. Never build a query by joining strings.
- A new endpoint needs an access check. Name the scope that it checks.
- A secret never goes into a log line, an error message or a test fixture.

## Speed

Read [the speed notes](references/performance.md). Ask for numbers when the change touches a hot path.

- A query inside a loop is a problem. Ask for one query for the whole list.
- A list that the user controls needs a limit.
- A cache needs an owner, a size limit and a way to clear it.

## Tests

Read [the test notes](references/testing.md).

- A bug fix comes with a test that fails before the fix.
- A test names the behaviour, not the function.
- A test that sleeps is a slow test and often a flaky one. Ask for a fake clock.

## Readability

Read [the naming notes](references/names.md).

- A function does one thing. Its name says what that thing is.
- A comment says why, not what.
- Dead code goes. Commented-out code goes too.

## Accessibility

For a change to the user interface, read [the accessibility notes](references/accessibility.md).

## Language notes

- TypeScript: [references/languages/typescript.md](references/languages/typescript.md)
- Python: [references/languages/python.md](references/languages/python.md)

## How to write a comment

- Start with the problem, then the fix.
- Mark each comment as a blocker, a suggestion or a question.
- Give a code sample when the fix is not obvious.
- Thank the author for good work. Say what was good, so they do it again.

## When you are done

Approve only when every blocker is fixed. Leave suggestions for the author to decide. Write one summary comment with the blockers, in order.
