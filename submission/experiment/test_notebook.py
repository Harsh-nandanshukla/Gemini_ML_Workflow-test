from pathlib import Path
import json
import joblib
import pandas as pd


BASE_DIR = Path(".")


CLEANED_CSV = BASE_DIR / "cleaned_data.csv"
READY_CSV = BASE_DIR / "ready_to_train_data.csv"
MODEL_PATH = BASE_DIR / "fraud_model.joblib"
EVAL_REPORT = BASE_DIR / "eval_report.json"
REVIEW_QUEUE = BASE_DIR / "review_queue.csv"


# -------------------------------------------------
# Test 1: cleaned_data.csv exists and has no duplicates
# -------------------------------------------------
def test_cleaned_data_exists_and_no_duplicates():
    assert CLEANED_CSV.exists(), "cleaned_data.csv does not exist"

    df = pd.read_csv(CLEANED_CSV)
    assert df.duplicated().sum() == 0, "cleaned_data.csv contains duplicate rows"


# -------------------------------------------------
# Test 2: ready_to_train_data.csv exists and is non-empty
# -------------------------------------------------
def test_ready_to_train_data_exists():
    assert READY_CSV.exists(), "ready_to_train_data.csv does not exist"

    df = pd.read_csv(READY_CSV)
    assert len(df) > 0, "ready_to_train_data.csv is empty"


# -------------------------------------------------
# Test 3: model artifact exists and is loadable
# -------------------------------------------------
def test_model_artifact_loadable():
    assert MODEL_PATH.exists(), "fraud_model.joblib does not exist"

    model = joblib.load(MODEL_PATH)
    assert model is not None, "Loaded model is None"


# -------------------------------------------------
# Test 4: eval_report.json exists and contains required keys
# -------------------------------------------------
def test_eval_report_contents():
    assert EVAL_REPORT.exists(), "eval_report.json does not exist"

    with open(EVAL_REPORT, "r") as f:
        report = json.load(f)

    for key in ["precision", "recall", "f1_score"]:
        assert key in report, f"Missing key in eval_report.json: {key}"
        assert isinstance(report[key], (int, float)), f"{key} is not numeric"


# -------------------------------------------------
# Test 5: review_queue.csv exists and has exactly 200 rows
# -------------------------------------------------
def test_review_queue_size():
    assert REVIEW_QUEUE.exists(), "review_queue.csv does not exist"

    df = pd.read_csv(REVIEW_QUEUE)
    assert len(df) == 200, "review_queue.csv does not contain exactly 200 rows"
