# Email Priority Assistant

A compact Python automation that classifies incoming email messages by business category and priority. It demonstrates the first stage of an AI assisted inbox workflow without connecting to a real mailbox or exposing personal data.

## Capabilities

1. Reads email records from JSON
2. Detects billing, support, sales and scheduling topics
3. Flags time sensitive messages
4. Produces a structured JSON report
5. Includes automated tests

## Run

```bash
python app.py
python -m unittest test_app.py
```

The generated `email_report.json` file is intentionally ignored by Git.

## Production direction

The classification layer can later be replaced with an LLM and connected to Gmail, Outlook, Slack or a CRM. Authentication, audit logs, human approval and data protection controls should be added before production use.
