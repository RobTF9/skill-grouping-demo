# Test notes

- A bug fix comes with a test that fails before the fix.
- Test behaviour, not the inside of a function.
- One reason to fail for each test.
- Name the test as a sentence: "sends one email for each invoice".
- Use a fake clock, not a sleep.
- Build test data with a small factory, not a large fixture file.
- Keep each test independent. Order must not matter.
