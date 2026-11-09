"""Deterministic checks for the fictional sample application records."""

from __future__ import annotations

from datetime import date
from typing import Any, Iterable


def check_completeness(records: Iterable[dict[str, Any]], required_categories: Iterable[str]) -> list[dict[str, Any]]:
    """Return one finding for each required document category that is absent."""
    present = {str(record.get("category", "")).strip() for record in records}
    findings = []
    for category in required_categories:
        if category not in present:
            findings.append({
                "type": "missing_document",
                "severity": "needs_review",
                "message": f"Required document category '{category}' was not found.",
                "evidence": {"category": category},
            })
    return findings


def check_expiry(records: Iterable[dict[str, Any]], as_of: date | None = None) -> list[dict[str, Any]]:
    """Flag records whose ISO expiry date is earlier than as_of."""
    as_of = as_of or date.today()
    findings = []
    for record in records:
        raw_date = record.get("expiry_date")
        if not raw_date:
            continue
        try:
            expiry = date.fromisoformat(str(raw_date))
        except ValueError:
            findings.append({
                "type": "invalid_expiry_date",
                "severity": "manual_review",
                "message": "The expiry date could not be parsed as YYYY-MM-DD.",
                "evidence": {"record_id": record.get("record_id"), "filename": record.get("filename"), "value": raw_date},
            })
            continue
        if expiry < as_of:
            findings.append({
                "type": "expired_document",
                "severity": "needs_review",
                "message": f"The document expiry date ({expiry.isoformat()}) is before {as_of.isoformat()}.",
                "evidence": {"record_id": record.get("record_id"), "filename": record.get("filename"), "expiry_date": expiry.isoformat()},
            })
    return findings


def check_field_consistency(records: Iterable[dict[str, Any]], fields: Iterable[str] = ("institution_name",)) -> list[dict[str, Any]]:
    """Flag fields with more than one non-empty value within a dossier."""
    records = list(records)
    findings = []
    for field in fields:
        values = {}
        for record in records:
            value = record.get(field)
            if value is not None and str(value).strip():
                values.setdefault(str(value).strip(), []).append(record.get("record_id") or record.get("filename"))
        if len(values) > 1:
            findings.append({
                "type": "field_mismatch",
                "severity": "manual_review",
                "message": f"Different values were found for '{field}'.",
                "evidence": {"field": field, "values_and_sources": values},
            })
    return findings


def check_exact_duplicates(records: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Flag repeated SHA-256 values supplied by the ingestion stage.

    This function does not calculate hashes from files; it compares hashes
    that an upstream, trusted file-ingestion step has already calculated.
    """
    sources_by_hash: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        raw_hash = record.get("sha256")
        if not raw_hash:
            continue
        value = str(raw_hash).strip().lower()
        if value:
            sources_by_hash.setdefault(value, []).append({
                "record_id": record.get("record_id"),
                "filename": record.get("filename"),
            })

    findings = []
    for digest, sources in sources_by_hash.items():
        if len(sources) > 1:
            findings.append({
                "type": "exact_duplicate_file",
                "severity": "manual_review",
                "message": "The same SHA-256 value is associated with multiple records.",
                "evidence": {"sha256": digest, "sources": sources},
            })
    return findings


def build_application_report(application: dict[str, Any], required_categories: Iterable[str], as_of: date | None = None) -> dict[str, Any]:
    """Build a transparent report; findings are indicators, not final decisions."""
    records = application.get("records", [])
    findings = []
    findings.extend(check_completeness(records, required_categories))
    findings.extend(check_expiry(records, as_of=as_of))
    findings.extend(check_field_consistency(records))
    findings.extend(check_exact_duplicates(records))
    return {
        "application_id": application.get("application_id", "UNKNOWN"),
        "institution_name": application.get("institution_name"),
        "record_count": len(records),
        "finding_count": len(findings),
        "findings": findings,
        "decision": "human_review_required" if findings else "no_sample_rule_alerts",
        "disclaimer": "This synthetic prototype does not determine fraud or make approval decisions.",
    }
