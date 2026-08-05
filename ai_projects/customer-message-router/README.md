# Customer Message Router

A practical message intake automation that routes customer requests, assigns a priority and prepares a professional response suggestion for human review.

## Capabilities

1. Processes customer messages from CSV
2. Routes technical, sales and appointment requests
3. Identifies urgent messages
4. Generates consistent reply suggestions
5. Keeps human approval enabled by default

## Run

```bash
python app.py
python -m unittest test_app.py
```

## Safety principle

Suggested replies are never sent automatically. A responsible production system should require approval, store an audit trail and apply access controls before connecting to live communication channels.
