# Error notes

Each error has the same body:

```json
{ "code": "invoice_not_found", "message": "No invoice has this id." }
```

- `code` is stable. Clients can rely on it.
- `message` is for people. It can change.
