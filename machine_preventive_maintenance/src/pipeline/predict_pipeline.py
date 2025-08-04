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
    def __init__(self, Temperature: float,
                 Vibration: float,
                 Pressure: float,
                 Voltage: float,
                 Current: float,
                 FFT_Feature1: float,
                 FFT_Feature2: float,
                 Normalized_Temp: float,
                 Normalized_Vibration: float,
                 Normalized_Pressure: float,
                 Normalized_Voltage: float,
                 Normalized_Current: float,
                 Anomaly_Score: float):

        self.Temperature = Temperature
        self.Vibration = Vibration
        self.Pressure = Pressure
        self.Voltage = Voltage
        self.Current = Current
        self.FFT_Feature1 = FFT_Feature1
        self.FFT_Feature2 = FFT_Feature2
        self.Normalized_Temp = Normalized_Temp
        self.Normalized_Vibration = Normalized_Vibration
        self.Normalized_Pressure = Normalized_Pressure
        self.Normalized_Voltage = Normalized_Voltage
        self.Normalized_Current = Normalized_Current
        self.Anomaly_Score = Anomaly_Score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                'Temperature': [self.Temperature],
                'Vibration': [self.Vibration],
                'Pressure': [self.Pressure],
                'Voltage': [self.Voltage],
                'Current': [self.Current],
                'FFT_Feature1': [self.FFT_Feature1],
                'FFT_Feature2': [self.FFT_Feature2],
                'Normalized_Temp': [self.Normalized_Temp],
                'Normalized_Vibration': [self.Normalized_Vibration],
                'Normalized_Pressure': [self.Normalized_Pressure],
                'Normalized_Voltage': [self.Normalized_Voltage],
                'Normalized_Current': [self.Normalized_Current],
                'Anomaly_Score': [self.Anomaly_Score],
            }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise customException(e, sys)
