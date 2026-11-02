# Naming notes

| Kind | Rule | Good | Bad |
|---|---|---|---|
| Function | A verb and an object | `sendInvoice` | `doIt` |
| Boolean | A question | `isActive` | `active2` |
| List | A plural noun | `invoices` | `invoiceList` |
| Count | `count` at the end | `retryCount` | `nRetries` |
| Time | The unit at the end | `timeoutMs` | `timeout` |

- Use the words of the product, not the words of the database.
- A short name is fine for a short scope, such as `i` in a three-line loop.
- Rename a thing when its job changes.
