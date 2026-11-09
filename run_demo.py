"""Run the synthetic VerifAICTE validation demo from the repository root."""

import json
from datetime import date
from pathlib import Path

from src.verifaicte.validation import build_application_report

ROOT = Path(__file__).resolve().parent
CONFIG = json.loads((ROOT / "config" / "required_documents.json").read_text(encoding="utf-8"))
REQUIRED = CONFIG["required_categories"]

for path in sorted((ROOT / "sample_data").glob("application_*.json")):
    application = json.loads(path.read_text(encoding="utf-8"))
    report = build_application_report(application, REQUIRED, as_of=date(2026, 11, 9))
    print(f"\n=== {report['application_id']} ===")
    print(json.dumps(report, indent=2))
