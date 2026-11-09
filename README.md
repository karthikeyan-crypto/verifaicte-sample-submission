# VerifAICTE — Sample Hackathon Submission

> **Demo repository for testing Hackathon Mentor AI's GitHub Repository Scanner.**
> This is a synthetic sample project, not an official SIH submission and not a production compliance tool.

## Project overview

VerifAICTE is a proposed AI-assisted document-scrutiny system for organizing institutional application documents and highlighting possible gaps, expired records, cross-document inconsistencies, and duplicate files. It presents findings with evidence so that an authorized reviewer can inspect the original documents.

The system is designed as decision support. It does not determine fraud, approve or reject an application, or replace an authorized human reviewer.

## Problem statement location

The project brief is included in [docs/PROBLEM_STATEMENT.md](docs/PROBLEM_STATEMENT.md). The solution proposal and architecture are also included inside this repository so a repository-scanning system can discover them without relying on external attachments.

## Repository structure

```text
.
├── README.md
├── docs/
│   ├── PROBLEM_STATEMENT.md
│   ├── SOLUTION_PROPOSAL.md
│   └── ARCHITECTURE.md
├── config/
│   └── required_documents.json
├── sample_data/
│   ├── application_001.json
│   └── application_002.json
├── src/verifaicte/
│   ├── __init__.py
│   └── validation.py
├── tests/
│   └── test_validation.py
├── notebooks/
│   └── demo.ipynb
├── run_demo.py
└── requirements.txt
```

## Quick start

The initial demo uses only the Python standard library.

```bash
python run_demo.py
python -m unittest discover -s tests -v
```

For Google Colab, open [notebooks/demo.ipynb](notebooks/demo.ipynb). See [COLAB_QUICKSTART.md](COLAB_QUICKSTART.md) for the upload/clone steps.

## Current prototype scope

- Checks whether configured document categories are present.
- Flags expired documents using their supplied expiry dates.
- Compares selected fields across synthetic application records.
- Flags records that share the same precomputed SHA-256 hash.
- Generates a JSON report containing findings and source record identifiers.

## Not implemented yet

OCR, document classification training, PDF digital-signature verification, image forensics, semantic search, external AICTE/issuer integrations, user authentication, and a production reviewer dashboard are not implemented in this sample. Duplicate checking only compares SHA-256 values supplied in the sample records; a production ingestion component must calculate hashes from the actual files. Any future external integration requires permission and suitable credentials.

## Sample data and privacy

All records in `sample_data/` are fictional. Do not upload real institutional records, identity documents, or personal information to this demo repository.

## Disclaimer

This repository exists to test repository discovery and text extraction. Its sample checks are illustrative and must not be used to make real compliance decisions.
