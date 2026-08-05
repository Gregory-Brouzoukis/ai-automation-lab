# Document Intake Organizer

A privacy conscious Python prototype that organizes new client matters, compares received documents with a configurable checklist and reports what is still missing.

## Capabilities

1. Reads structured intake records from JSON
2. Supports several matter types
3. Identifies missing documents
4. Marks complete files as ready for review
5. Uses fictional sample data only

## Run

```bash
python app.py
python -m unittest test_app.py
```

## Production direction

A production version could extract document types with AI, send approved reminders and synchronize matter status with a secure case management system. Sensitive documents should be encrypted and processed under a documented retention policy.
