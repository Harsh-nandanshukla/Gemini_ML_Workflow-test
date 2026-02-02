
#  README.md — Gemini End-to-End ML Evaluation

## Project Overview

This project evaluates whether **Google Gemini** can reliably follow a **strict, end-to-end machine learning workflow** when provided with a detailed task prompt. The focus is **not model performance**, but **instruction adherence**, reproducibility, and artifact generation.

The experiment follows a **prompt-first methodology**:

1. Design a clear task prompt.
2. Write unit tests derived *only* from the prompt.
3. Implement a correct reference solution.
4. Evaluate Gemini using the same prompt and tests.
5. Analyze failures objectively using automated tests.

---

## Objective

To determine whether Gemini can:

* Execute a multi-step ML workflow end-to-end
* Follow explicit file-naming and output requirements
* Produce reproducible, verifiable artifacts without human intervention

---

## Dataset

* File: `fraud_transactions.csv`
* Size: >1 MB
* Rows: >100
* Target column: `Fraud_Label`

The dataset was treated as **read-only** during all experiments.

---

## Prompt-First Design

The task instructions are defined in:

```
prompt.md
```

This file is the **single source of truth**.
All expectations regarding:

* data cleaning
* feature engineering
* model training
* evaluation
* saved artifacts

are explicitly stated in the prompt.

---

## Unit Tests

Unit tests are implemented in:

```
test_notebook.py
```

Key characteristics:

* Tests are written **after** the prompt
* Each test directly corresponds to a requirement in `prompt.md`
* No extra assumptions or hidden variables are tested
* Exactly **5 tests** are used, as per project instructions

The tests validate the existence and correctness of required artifacts such as:

* cleaned dataset
* training-ready dataset
* trained model file
* evaluation report
* review queue output

---

## Reference Solution

A correct reference implementation was created locally to ensure:

* All prompt requirements are achievable
* All unit tests pass under correct execution

This confirms that **test failures are due to Gemini behavior**, not task ambiguity.

---

## Gemini Evaluation (Colab)

The same `prompt.md` was provided to Gemini in a Google Colab environment with:

* no additional guidance
* no clarification
* no intervention

Gemini was allowed to run freely.

### Observed Behavior

* Gemini performed exploratory analysis
* Gemini trained a Logistic Regression model
* Gemini reported evaluation metrics
* Gemini saved files under incorrect names
* Gemini failed to generate required artifacts

---

## Test Results on Gemini Output

All unit tests **failed** when run against Gemini’s output:

* Required CSV files were missing
* Required JSON evaluation report was missing
* Model file was saved with an incorrect name
* Review queue was not generated

These failures were **expected and desired**, as they demonstrate Gemini’s inability to strictly follow end-to-end ML instructions.

---

## Key Conclusion

Although Gemini can perform parts of an ML workflow, it **does not reliably adhere to strict procedural instructions**, particularly regarding:

* reproducibility
* artifact generation
* file naming conventions

This experiment demonstrates the importance of **automated testing** when evaluating LLM-driven data science workflows.

---

## Files Included in Submission

```
experiment/
├── data/
│   └── fraud_transactions.csv
├── prompt.md
├── test_notebook.py
├── requirements.txt
├── README.md
```

Evidence files (screenshots/logs) are included separately as required.

---

## Final Notes

* The prompt was designed **before** writing tests
* Tests were derived **only** from the prompt
* Gemini was evaluated **without assistance**
* Failures were captured objectively using pytest

This methodology ensures a fair, reproducible evaluation of LLM behavior.

---

