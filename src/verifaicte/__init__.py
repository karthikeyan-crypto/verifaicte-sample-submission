"""Small, synthetic VerifAICTE validation prototype."""

from .validation import (
    check_completeness,
    check_expiry,
    check_field_consistency,
    build_application_report,
)

__all__ = [
    "check_completeness",
    "check_expiry",
    "check_field_consistency",
    "build_application_report",
]
