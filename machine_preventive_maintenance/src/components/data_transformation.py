import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import customException
from src.logger import logging
from src.utills import save_object
import os

class DataTransformationconfig:
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationconfig()
    def get_data_transformer_object(self):
        """data transformation based on data type"""
        try:
         numerical_columns=['Temperature', 'Vibration', 'Pressure',
          'Voltage', 'Current', 'FFT_Feature1', 'FFT_Feature2', 'Normalized_Temp',
           'Normalized_Vibration', 'Normalized_Pressure', 'Normalized_Voltage',
       'Normalized_Current', 'Anomaly_Score']
        
         num_pipeline=Pipeline(steps=[
            ("imputer",SimpleImputer(strategy="median")),
            ("scaler",StandardScaler())]
        )
         cat_pipeline = Pipeline(steps=[
           ("imputer", SimpleImputer(strategy="most_frequent")),
           ("one_hot_encoder", OneHotEncoder()),
           ("scaler", StandardScaler())
                                ])
         logging.info("column transformers completed"
                      )
         preprocessor = ColumnTransformer(
           transformers=[
                   ("num_pipeline", num_pipeline, numerical_columns)
                         ]
                            )
         return preprocessor

        
        except Exception as e:
            raise customException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("Read train and test data completed")
            logging.info("obtaining pre process data")
            preprocessing_obj=self.get_data_transformer_object()
            target_column_name='Fault_Status'
            numerical_colums=['Temperature', 'Vibration', 'Pressure',
          'Voltage', 'Current', 'FFT_Feature1', 'FFT_Feature2', 'Normalized_Temp',
           'Normalized_Vibration', 'Normalized_Pressure', 'Normalized_Voltage',
       'Normalized_Current', 'Anomaly_Score']
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]
            
            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(f"Applying preprocessing object on training dataframe and testing dataframe")

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)] 
            test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)] 
            logging.info(f"saved preprocessing object.")
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,


            )
        except Exception as e:
            raise customException(e,sys)