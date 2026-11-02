# Schema notes

| Table | Holds | Key |
|---|---|---|
| teams | One row for each workspace | id |
| members | One row for each teammate in a team | team_id, user_id |
| invoices | One row for each invoice | id |
| events | One row for each product event | id, created_at |
