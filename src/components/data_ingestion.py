#all code related to reading the data and prepare the train test split
import os
import sys
from src.execption import CustomException
from src.logger import logging
import pandas as pd
import numpy as np

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
    di.initiate_data_ingestion()

