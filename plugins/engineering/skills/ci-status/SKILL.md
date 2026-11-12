---
name: ci-status
description: Get the status of the latest CI run for a branch.
---

# CI status

Find the latest CI run for the branch, then report its status and the failed jobs.

## Get the run

```bash
curl -s -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.github.com/repos/acme/app/actions/runs?branch=$BRANCH&per_page=1"
```

Report the status, the duration and the name of each failed job.
