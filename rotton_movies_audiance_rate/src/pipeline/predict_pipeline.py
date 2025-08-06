import sys
import pandas as pd
from src.exception import customException
from src.utills import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'

            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)

            return preds
        except Exception as e:
            raise customException(e, sys)


class CustomData:
    def __init__(self,
                 movie_title: str,
                 movie_info: str,
                 critics_consensus: str,
                 rating: str,
                 genre: str,
                 directors: str,
                 writers: str,
                 cast: str,
                 in_theaters_date: str,
                 on_streaming_date: str,
                 runtime_in_minutes: int,
                 studio_name: str,
                 tomatometer_status: str,
                 tomatometer_rating: int,
                 tomatometer_count: int,
                 release_year: int,
                 movie_age_years: float,
                 has_critics_consensus: int,
                 primary_genre: str):

        self.movie_title = movie_title
        self.movie_info = movie_info
        self.critics_consensus = critics_consensus
        self.rating = rating
        self.genre = genre
        self.directors = directors
        self.writers = writers
        self.cast = cast
        self.in_theaters_date = in_theaters_date
        self.on_streaming_date = on_streaming_date
        self.runtime_in_minutes = runtime_in_minutes
        self.studio_name = studio_name
        self.tomatometer_status = tomatometer_status
        self.tomatometer_rating = tomatometer_rating
        self.tomatometer_count = tomatometer_count
        self.release_year = release_year
        self.movie_age_years = movie_age_years
        self.has_critics_consensus = has_critics_consensus
        self.primary_genre = primary_genre

    def get_data_as_data_frame(self):
        try:
            data = {
                "movie_title": [self.movie_title],
                "movie_info": [self.movie_info],
                "critics_consensus": [self.critics_consensus],
                "rating": [self.rating],
                "genre": [self.genre],
                "directors": [self.directors],
                "writers": [self.writers],
                "cast": [self.cast],
                "in_theaters_date": [pd.to_datetime(self.in_theaters_date)],
                "on_streaming_date": [pd.to_datetime(self.on_streaming_date)],
                "runtime_in_minutes": [self.runtime_in_minutes],
                "studio_name": [self.studio_name],
                "tomatometer_status": [self.tomatometer_status],
                "tomatometer_rating": [self.tomatometer_rating],
                "tomatometer_count": [self.tomatometer_count],
                "release_year": [self.release_year],
                "movie_age_years": [self.movie_age_years],
                "has_critics_consensus": [self.has_critics_consensus],
                "primary_genre": [self.primary_genre]
            }

            return pd.DataFrame(data)
        except Exception as e:
            raise customException(e, sys)
