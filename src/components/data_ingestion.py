#all code related to reading the data and prepare the train test split
import os
import sys
from src.execption import CustomException
from src.logger import logging

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer
import pandas as pd 

from sklearn.model_selection import train_test_split
from dataclasses import dataclass



@dataclass
class DataIngestionConfig:
    train_data_path : str = os.path.join("artifacts","train.csv") # will save the train data in this folder
    test_data_path : str = os.path.join("artifacts","test.csv") # will save the test data in this folder
    raw_data_path : str = os.path.join("artifacts","raw.csv") # will save the raw data in this folder

class DataIngestion :
    def __init__(self) :
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the Data ingestion method or component")
        try :
            df = pd.read_csv("notebook/stud.csv")
            logging.info("REad the Dataset as a Dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok= True )

            df.to_csv(self.ingestion_config.raw_data_path,index = False,header =True)
            logging.info("Train Test Split initiated")
            train_set ,test_set = train_test_split(df,test_size= 0.3, random_state=24)
            train_set.to_csv(
                self.ingestion_config.train_data_path,
                index = False,
                header = True)
            test_set.to_csv(self.ingestion_config.test_data_path,
                            index = False,
                            header = True)

            logging.info("Data Ingestoin Completed")
            return  (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )



        except Exception as e :
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    di = DataIngestion()
    train_data , test_data = di.initiate_data_ingestion()

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)

    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data,test_data)

    model_trainer =ModelTrainer()
    print(model_trainer.initiate_model_trainer(training_arr=train_arr,test_arr=test_arr))


