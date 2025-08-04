import os
import sys
import numpy as np
from dataclasses import dataclass

from sklearn.model_selection import RandomizedSearchCV, StratifiedKFold, ParameterGrid
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline

from src.exception import customException
from src.utills import save_object
from src.logger import logging

@dataclass
class ModelTrainerconfig:
    trained_model_file_path: str = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerconfig()

    def intiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting training and test input data")
            x_train, y_train, x_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                'LogisticRegression': LogisticRegression(max_iter=1000, random_state=42),
                'RandomForest': RandomForestClassifier(random_state=42),
                'XGBoost': XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42),
            }

            params = {
                'LogisticRegression': {
                    'classifier__C': [0.01, 0.1, 1, 10]
                },
                'RandomForest': {
                    'classifier__n_estimators': [100, 150],
                    'classifier__max_depth': [None, 10]
                },
                'XGBoost': {
                    'classifier__n_estimators': [100],
                    'classifier__max_depth': [3, 6]
                },
            }

            best_model_name = None
            best_model = None
            best_score = 0
            best_test_scores = {}

            for model_name, model in models.items():
                logging.info(f"Training and tuning model: {model_name}")

                pipeline = ImbPipeline(steps=[
                    ('smote', SMOTE(random_state=42)),
                    ('classifier', model)
                ])

                search_space = params.get(model_name, {})
                n_iter = min(10, len(ParameterGrid(search_space)))

                grid_search = RandomizedSearchCV(
                    estimator=pipeline,
                    param_distributions=search_space,
                    cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42),
                    scoring='accuracy',
                    n_jobs=-1,
                    verbose=1,
                    n_iter=n_iter,
                    random_state=42
                )

                grid_search.fit(x_train, y_train)
                best_estimator = grid_search.best_estimator_
                y_pred = best_estimator.predict(x_test)

                if hasattr(best_estimator, "predict_proba") and len(np.unique(y_test)) == 2:
                    probas = best_estimator.predict_proba(x_test)[:, 1]
                    roc_auc = roc_auc_score(y_test, probas)
                else:
                    roc_auc = 0

                test_scores = {
                    "accuracy": accuracy_score(y_test, y_pred),
                    "precision": precision_score(y_test, y_pred, average='weighted', zero_division=0),
                    "recall": recall_score(y_test, y_pred, average='weighted'),
                    "f1": f1_score(y_test, y_pred, average='weighted'),
                    "roc_auc": roc_auc
                }

                logging.info(f"{model_name} evaluation scores: {test_scores}")

                if test_scores["accuracy"] > best_score:
                    best_score = test_scores["accuracy"]
                    best_model_name = model_name
                    best_model = best_estimator
                    best_test_scores = test_scores

            if best_model is None:
                raise customException("No suitable model was selected.", sys)

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            logging.info(f"Best model: {best_model_name} with accuracy: {best_score}")
            logging.info(f"Evaluation metrics: {best_test_scores}")

            return {
                "best_model_name": best_model_name,
                "accuracy": best_score,
                "test_scores": best_test_scores
            }

        except Exception as e:
            raise customException(e, sys)
