# Checklist

Use this list for every review. Tick each line in your summary comment.

- Tests cover the change, and they fail without it.
- Names say what the code does, not how it does it.
- Each new function has one job.
- Errors are handled or passed on, never swallowed.
- Inputs from users are checked before use.
- Queries use parameters.
- New endpoints check access.
- Logs carry no secrets and no personal data.
- Loops do not run a query each time.
- Lists from users have a limit.
- Public functions have a short comment that says why they exist.
- The change log names the change, when users can see it.
