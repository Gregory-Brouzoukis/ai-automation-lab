"""Organize new client matters and generate document checklists."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path


CHECKLISTS = {
    "property_sale": ["Identity document", "Tax identification details", "Property title", "Recent property certificate"],
    "business_setup": ["Identity document", "Business name", "Registered address", "Ownership details"],
    "general_contract": ["Identity document", "Contact details", "Draft agreement", "Supporting documents"],
}


@dataclass(frozen=True)
class IntakeSummary:
    reference: str
    matter_type: str
    missing_documents: list[str]
    status: str


def organize_intake(record: dict) -> IntakeSummary:
    matter_type = record.get("matter_type", "general_contract")
    required = CHECKLISTS.get(matter_type, CHECKLISTS["general_contract"])
    received = {item.lower() for item in record.get("received_documents", [])}
    missing = [item for item in required if item.lower() not in received]
    return IntakeSummary(
        reference=record.get("reference", "UNASSIGNED"),
        matter_type=matter_type,
        missing_documents=missing,
        status="ready_for_review" if not missing else "awaiting_documents",
    )


def process_file(input_path: Path, output_path: Path) -> None:
    records = json.loads(input_path.read_text(encoding="utf-8"))
    summaries = [asdict(organize_intake(record)) for record in records]
    output_path.write_text(json.dumps(summaries, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("sample_intake.json"))
    parser.add_argument("--output", type=Path, default=Path("intake_report.json"))
    args = parser.parse_args()
    process_file(args.input, args.output)
    print(f"Intake report written to {args.output}")


if __name__ == "__main__":
    main()
