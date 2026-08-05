"""Classify incoming email messages by urgency and business category."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path


URGENT_TERMS = {"urgent", "immediately", "deadline", "overdue", "failed", "today"}
CATEGORY_TERMS = {
    "billing": {"invoice", "payment", "refund", "receipt"},
    "support": {"error", "problem", "issue", "failed", "help"},
    "sales": {"quote", "pricing", "proposal", "demo"},
    "scheduling": {"appointment", "meeting", "schedule", "availability"},
}


@dataclass(frozen=True)
class EmailResult:
    subject: str
    sender: str
    category: str
    priority: str
    confidence: float


def classify_email(message: dict[str, str]) -> EmailResult:
    text = f"{message.get('subject', '')} {message.get('body', '')}".lower()
    category_scores = {
        category: sum(term in text for term in terms)
        for category, terms in CATEGORY_TERMS.items()
    }
    category = max(category_scores, key=category_scores.get)
    best_score = category_scores[category]
    if best_score == 0:
        category = "general"

    urgent_matches = sum(term in text for term in URGENT_TERMS)
    priority = "high" if urgent_matches else "normal"
    confidence = min(0.98, 0.55 + best_score * 0.12 + urgent_matches * 0.1)

    return EmailResult(
        subject=message.get("subject", "No subject"),
        sender=message.get("sender", "Unknown sender"),
        category=category,
        priority=priority,
        confidence=round(confidence, 2),
    )


def process_file(input_path: Path, output_path: Path) -> None:
    messages = json.loads(input_path.read_text(encoding="utf-8"))
    results = [asdict(classify_email(message)) for message in messages]
    output_path.write_text(json.dumps(results, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("sample_emails.json"))
    parser.add_argument("--output", type=Path, default=Path("email_report.json"))
    args = parser.parse_args()
    process_file(args.input, args.output)
    print(f"Report written to {args.output}")


if __name__ == "__main__":
    main()
