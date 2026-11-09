import unittest
from datetime import date

from src.verifaicte.validation import (
    check_completeness,
    check_expiry,
    check_field_consistency,
    check_exact_duplicates,
)


class ValidationTests(unittest.TestCase):
    def test_missing_category_is_reported(self):
        findings = check_completeness([{"category": "application_form"}], ["application_form", "certificate"])
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["type"], "missing_document")

    def test_expired_document_is_reported(self):
        records = [{"record_id": "D1", "expiry_date": "2024-01-01"}]
        findings = check_expiry(records, as_of=date(2026, 11, 9))
        self.assertEqual(findings[0]["type"], "expired_document")

    def test_conflicting_institution_names_are_reported(self):
        records = [
            {"record_id": "D1", "institution_name": "College A"},
            {"record_id": "D2", "institution_name": "College B"},
        ]
        findings = check_field_consistency(records)
        self.assertEqual(findings[0]["type"], "field_mismatch")

    def test_repeated_sha256_is_reported_as_duplicate(self):
        records = [
            {"record_id": "D1", "filename": "a.pdf", "sha256": "abc123"},
            {"record_id": "D2", "filename": "b.pdf", "sha256": "ABC123"},
            {"record_id": "D3", "filename": "c.pdf", "sha256": "different"},
        ]
        findings = check_exact_duplicates(records)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["type"], "exact_duplicate_file")
        self.assertEqual(len(findings[0]["evidence"]["sources"]), 2)


if __name__ == "__main__":
    unittest.main()
