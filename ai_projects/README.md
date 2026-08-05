# AI Automation Projects

This collection contains three small, working Python automations built around practical business workflows.

## Projects

| Project | Purpose | Input | Output |
| --- | --- | --- | --- |
| Email Priority Assistant | Classifies business email by category and urgency | JSON | Priority report |
| Customer Message Router | Routes customer requests and suggests reviewed replies | CSV | Routing report |
| Document Intake Organizer | Checks incoming matters for missing documents | JSON | Intake report |

## Design principles

1. Clear and maintainable Python
2. No external dependency required
3. Fictional sample data only
4. Human review before external communication
5. Simple tests for core behavior
6. Clear path from prototype to production

## Quick validation

Run each project's test suite from its own directory:

```bash
python -m unittest test_app.py
```

These prototypes demonstrate workflow design and automation fundamentals. They do not connect to live accounts, send messages or process real personal data.
