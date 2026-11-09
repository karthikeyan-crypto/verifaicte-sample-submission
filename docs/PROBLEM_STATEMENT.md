# Project Problem Statement — VerifAICTE

**Document type:** Team-authored sample problem brief for repository-scanner testing  
**Status:** Illustrative project brief; not a verbatim official SIH problem statement

## Background

Institutional applications may contain many supporting documents, including forms, certificates, declarations, faculty records, and infrastructure evidence. Reviewers may need to check whether required documents are present, whether dates and validity periods are acceptable, and whether important details agree across several files.

## Problem

Manual review can be repetitive and time-consuming. Information may be distributed across PDFs, scans, presentations, and spreadsheets. A reviewer may have difficulty finding missing items, expired records, inconsistent institution details, or duplicated supporting files. Findings are also harder to verify when the system does not show which source document supports an alert.

## Objective

Develop an AI-assisted document-scrutiny workflow that organizes submitted files, extracts selected information, applies transparent validation rules, flags possible inconsistencies or duplicates, and links each finding to its source evidence.

## Expected capabilities

1. Classify common application document types.
2. Extract readable text and selected fields from digital or scanned documents.
3. Check document completeness and configured validity dates.
4. Compare selected fields across documents in the same application.
5. Identify exact duplicate files and provide a basis for later similarity checks.
6. Produce an evidence-linked report for human review.

## Constraints and responsible use

- Begin with fictional or appropriately anonymized test records.
- Low-confidence extraction must be marked for manual review.
- A mismatch or duplicate is an alert for investigation, not proof of fraud.
- Unavailable external sources must not be treated as verification success or failure.
- The system must not make final approval or rejection decisions.
- Any connection to official systems or issuer databases requires authorization.

## Success evaluation

Evaluate the prototype using labelled synthetic cases that include missing documents, expired dates, inconsistent fields, and exact duplicate files. Report precision, recall, false-positive rate, extraction accuracy, and review time only after running reproducible tests. No performance result is claimed by this sample repository.
