"""Route customer messages and prepare safe response suggestions."""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path


ROUTES = {
    "technical_support": {"error", "broken", "login", "website", "technical"},
    "sales": {"price", "quote", "cost", "service", "proposal"},
    "appointments": {"appointment", "meeting", "available", "schedule"},
}

REPLIES = {
    "technical_support": "Thank you for reporting this issue. We have recorded the details and will review them shortly.",
    "sales": "Thank you for your interest. We will review your request and contact you with the relevant information.",
    "appointments": "Thank you for your message. We will check availability and confirm the next suitable time.",
    "general": "Thank you for contacting us. Your message has been received and will be reviewed shortly.",
}


@dataclass(frozen=True)
class RoutedMessage:
    customer: str
    route: str
    priority: str
    suggested_reply: str
    requires_human_review: bool = True


def route_message(row: dict[str, str]) -> RoutedMessage:
    text = row.get("message", "").lower()
    scores = {route: sum(term in text for term in terms) for route, terms in ROUTES.items()}
    route = max(scores, key=scores.get)
    if scores[route] == 0:
        route = "general"
    priority = "high" if any(term in text for term in ("urgent", "today", "immediately")) else "normal"
    return RoutedMessage(
        customer=row.get("customer", "Unknown customer"),
        route=route,
        priority=priority,
        suggested_reply=REPLIES[route],
    )


def process_csv(input_path: Path, output_path: Path) -> None:
    with input_path.open(encoding="utf-8", newline="") as source:
        results = [asdict(route_message(row)) for row in csv.DictReader(source)]
    output_path.write_text(json.dumps(results, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("sample_messages.csv"))
    parser.add_argument("--output", type=Path, default=Path("routing_report.json"))
    args = parser.parse_args()
    process_csv(args.input, args.output)
    print(f"Routing report written to {args.output}")


if __name__ == "__main__":
    main()
