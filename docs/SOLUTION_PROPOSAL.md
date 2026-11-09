# Solution Proposal

## Overview

VerifAICTE is a modular assistant that processes an application dossier and creates a structured review report. The workflow is designed to keep extracted values, validation rules, and source evidence connected.

## Proposed processing stages

1. **Upload and inventory:** accept permitted files, calculate SHA-256 hashes, record file names and sizes, and reject unsupported or oversized files.
2. **Document identification:** predict a likely document category using a baseline text classifier; allow reviewer correction.
3. **Text and field extraction:** extract text from digital PDFs and use OCR for scans; locate dates, institution identifiers, names, counts, and other configured fields.
4. **Rule checks:** check required categories, configured validity periods, and consistency of selected fields across the same application.
5. **Duplicate screening:** identify exact duplicates with cryptographic hashes. Similarity-based alerts may be added later and must remain reviewable.
6. **Evidence-linked output:** show the finding, source filename, page or region when available, applied rule, extraction confidence, and review status.

## Initial prototype

This sample implements only completeness checks, expiry checks, selected-field comparisons, and JSON report generation. It uses fictional JSON records so the workflow can be tested before OCR and model training are introduced.

## Later phases

- Add PDF text extraction and OCR with confidence handling.
- Train and evaluate document classification using a labelled dataset.
- Add visual similarity checks for document images where legally appropriate.
- Add a reviewer interface, role-based access, and audit events.
- Add authorized external verification connectors only after approval and security review.

## Human oversight

The tool is decision support. Reviewers must inspect the cited source material and resolve uncertain cases. A flagged discrepancy is not a fraud determination.
