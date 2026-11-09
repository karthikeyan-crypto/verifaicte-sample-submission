# Architecture

```text
Application dossier
       |
       v
File inventory + SHA-256
       |
       v
Document type identification
       |
       v
Text extraction / OCR (future)
       |
       v
Field extraction with source references
       |
       v
Completeness + expiry + consistency rules
       |
       v
Duplicate screening
       |
       v
Evidence-linked review report
       |
       v
Human reviewer decision
```

## Proposed components

- **Ingestion:** file validation, safe storage, and metadata inventory.
- **Extraction:** PDF text extraction and OCR for scanned files.
- **Classification:** baseline TF-IDF + Logistic Regression after collecting labelled examples.
- **Validation:** versioned, configurable rules; deterministic checks are preferred where possible.
- **Duplicate detection:** SHA-256 for exact duplicates; optional image/text similarity in a later phase.
- **Reporting:** JSON/API output and a reviewer-facing interface.

## Trust boundaries

Submitted files are untrusted input. The prototype does not execute submitted code or macros. Production deployment would need authentication, access control, malware scanning, encryption, retention rules, and an audit trail.
