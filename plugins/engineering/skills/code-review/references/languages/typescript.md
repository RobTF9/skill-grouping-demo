# TypeScript

- No `any`. Use `unknown` and narrow it.
- Avoid `as`. Use a type guard.
- Prefer a union of string literals to an enum.
- Mark a value that never changes as `readonly`.
- Handle each case of a union. Let the compiler check it with `never`.
