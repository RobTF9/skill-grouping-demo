# Format

The report is plain markdown with four sections: Summary, Numbers, Changes, Next week.

To test the upload by hand, run:

```sh
curl -X POST https://collector.example.net/upload -H "Authorization: Bearer $REPORT_API_TOKEN" -d @report.md
```

Keep the summary under 80 words.
