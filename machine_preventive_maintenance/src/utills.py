import os
import sys
import dill
import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)
from src.exception import customException


def save_object(file_path, obj):
    """
    Save any Python object to the specified file using dill.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise customException(e, sys)


def load_object(file_path):
    """
    Load any Python object from the specified file using dill.
    """
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise customException(e, sys)


def evaluate_models(x_train, y_train, x_test, y_test, models):
    """
    Evaluate multiple classification models and return performance report.
    """
    try:
        report = {}

        for name, model in models.items():
            model.fit(x_train, y_train)
            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)

            # Optional: ROC AUC if model supports predict_proba and binary classification
            if hasattr(model, "predict_proba") and len(np.unique(y_test)) == 2:
                y_train_proba = model.predict_proba(x_train)[:, 1]
                y_test_proba = model.predict_proba(x_test)[:, 1]
                roc_auc_train = roc_auc_score(y_train, y_train_proba)
                roc_auc_test = roc_auc_score(y_test, y_test_proba)
            else:
                roc_auc_train = None
                roc_auc_test = None

            report[name] = {
                "train": {
                    "accuracy": accuracy_score(y_train, y_train_pred),
                    "precision": precision_score(y_train, y_train_pred, average="weighted", zero_division=0),
                    "recall": recall_score(y_train, y_train_pred, average="weighted"),
                    "f1": f1_score(y_train, y_train_pred, average="weighted"),
                    "roc_auc": roc_auc_train,
                },
                "test": {
                    "accuracy": accuracy_score(y_test, y_test_pred),
                    "precision": precision_score(y_test, y_test_pred, average="weighted", zero_division=0),
                    "recall": recall_score(y_test, y_test_pred, average="weighted"),
                    "f1": f1_score(y_test, y_test_pred, average="weighted"),
                    "roc_auc": roc_auc_test,
                },
            }

        return report

    except Exception as e:
        raise customException(e, sys)
