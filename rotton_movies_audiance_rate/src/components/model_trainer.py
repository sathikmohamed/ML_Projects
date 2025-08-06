import os
import sys
import numpy as np
from dataclasses import dataclass

from sklearn.model_selection import RandomizedSearchCV, KFold, ParameterGrid
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

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
                'LinearRegression': LinearRegression(),
                'Ridge': Ridge(random_state=42),
                'Lasso': Lasso(random_state=42),
                'RandomForest': RandomForestRegressor(random_state=42),
                'XGBoost': XGBRegressor(random_state=42, eval_metric='rmse', use_label_encoder=False),
            }

            params = {
                'LinearRegression': {},  # no hyperparams for basic LR
                'Ridge': {
                    'alpha': [0.1, 1.0, 10.0]
                },
                'Lasso': {
                    'alpha': [0.01, 0.1, 1.0]
                },
                'RandomForest': {
                    'n_estimators': [100, 150],
                    'max_depth': [None, 10]
                },
                'XGBoost': {
                    'n_estimators': [100],
                    'max_depth': [3, 6]
                },
            }

            best_model_name = None
            best_model = None
            best_score = float('-inf')  # for R2 score, higher is better
            best_test_scores = {}

            for model_name, model in models.items():
                logging.info(f"Training and tuning model: {model_name}")

                search_space = params.get(model_name, {})
                n_iter = min(10, len(ParameterGrid(search_space))) if search_space else 1

                # No pipeline or SMOTE here since regression and no oversampling
                grid_search = RandomizedSearchCV(
                    estimator=model,
                    param_distributions=search_space,
                    cv=KFold(n_splits=5, shuffle=True, random_state=42),
                    scoring='r2',
                    n_jobs=-1,
                    verbose=1,
                    n_iter=n_iter,
                    random_state=42
                )

                grid_search.fit(x_train, y_train)
                best_estimator = grid_search.best_estimator_
                y_pred = best_estimator.predict(x_test)

                test_scores = {
                    "r2_score": r2_score(y_test, y_pred),
                    "mse": mean_squared_error(y_test, y_pred),
                    "mae": mean_absolute_error(y_test, y_pred)
                }

                logging.info(f"{model_name} evaluation scores: {test_scores}")

                if test_scores["r2_score"] > best_score:
                    best_score = test_scores["r2_score"]
                    best_model_name = model_name
                    best_model = best_estimator
                    best_test_scores = test_scores

            if best_model is None:
                raise customException("No suitable model was selected.", sys)

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            logging.info(f"Best model: {best_model_name} with R2 score: {best_score}")
            logging.info(f"Evaluation metrics: {best_test_scores}")

            return {
                "best_model_name": best_model_name,
                "r2_score": best_score,
                "test_scores": best_test_scores
            }

        except Exception as e:
            raise customException(e, sys)
