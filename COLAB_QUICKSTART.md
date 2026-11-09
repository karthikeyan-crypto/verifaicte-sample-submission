# Colab Quick Start

1. Open the public GitHub repository in Google Colab, or clone it in a Colab cell.
2. Open `notebooks/demo.ipynb`.
3. Run the setup, demonstration, and test cells in order. The sample records are fictional.
4. To run tests manually from the repository root:

```python
!python -m unittest discover -s tests -v
```

For Hackathon Mentor AI's repository scanner, set REPOSITORY_URL to this repository's public GitHub URL. The scanner should discover docs/PROBLEM_STATEMENT.md, the README, proposal, architecture, source code, sample JSON, tests, and notebook.
