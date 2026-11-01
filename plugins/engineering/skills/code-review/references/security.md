# Safety notes

## Input

- Treat every value from a request, a file or a message as untrusted.
- Check the type, the length and the range of each value.
- Reject a value that fails the check. Do not try to fix it.

## Queries

- Use parameters for every value in a query.
- Never build a table name or a column name from user input.
- Limit each query that a user can start.

## Access

- Each endpoint names the scope that it needs.
- Check access on the server, never only in the browser.
- A user who cannot see a record gets a 404, not a 403, so the record stays hidden.

## Secrets

- A secret lives in the secret store, never in the code.
- A secret never goes into a log, an error or a fixture.
- Rotate a secret that was in a commit, even for a minute.

## Files

- Check the size and the type of each upload.
- Store uploads outside the web root.
- Never run a file that a user uploaded.
