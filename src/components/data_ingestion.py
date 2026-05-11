#all code related to reading the data and prepare the train test split
import os
import sys
from src.execption import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
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



"""
======================== FILE EXPLANATION ========================

PURPOSE OF THIS FILE:
This file is responsible for the Data Ingestion phase of your ML pipeline.

Data Ingestion means:

1. Reading raw dataset
2. Creating required folders
3. Saving raw dataset
4. Splitting dataset into train/test sets
5. Saving train/test datasets
6. Returning file paths for future pipeline stages

This is usually the FIRST major step in an ML project pipeline.


----------------------------------------------------------------
1) import os
----------------------------------------------------------------

import os

Built-in Python module.

Used for interacting with operating system.

Used here for:

- creating folders
- managing file paths
- directory operations


Functions used:

os.makedirs()
os.path.join()
os.path.dirname()


----------------------------------------------------------------
2) import sys
----------------------------------------------------------------

import sys

Built-in Python module.

Used for interacting with Python runtime.

In this file it's mainly used for:

sys.exc_info()

through your CustomException class.


Used when:

raise CustomException(e,sys)


----------------------------------------------------------------
3) CustomException import
----------------------------------------------------------------

from src.execption import CustomException

This imports your custom exception class.

Purpose:

Instead of showing ugly default Python errors,
it shows formatted error messages containing:

- file name
- line number
- error message


Example:

raise CustomException(e,sys)


NOTE:
You currently wrote:

src.execption

Looks like a spelling mistake.

It should probably be:

src.exception


----------------------------------------------------------------
4) logging import
----------------------------------------------------------------

from src.logger import logging

Imports your custom logging configuration.

Allows writing logs into log files.

Example:

logging.info("Data loaded successfully")


----------------------------------------------------------------
5) pandas import
----------------------------------------------------------------

import pandas as pd

Pandas is a popular Python library for data manipulation.


Used here for:

pd.read_csv()
df.to_csv()


Common structure:
Data is stored in DataFrames.


----------------------------------------------------------------
6) train_test_split import
----------------------------------------------------------------

from sklearn.model_selection import train_test_split

Imported from :contentReference[oaicite:0]{index=0}.

Purpose:
Splits dataset into training and testing datasets.


Example:

train_set, test_set = train_test_split(...)


----------------------------------------------------------------
7) dataclass import
----------------------------------------------------------------

from dataclasses import dataclass

Built-in Python decorator.

Automatically generates:

- constructor
- object representation
- boilerplate code

Used for configuration storage.


----------------------------------------------------------------
8) @dataclass
----------------------------------------------------------------

@dataclass

Decorator applied to class below it.

Automatically creates:

__init__()
__repr__()
__eq__()

for the class.


Without this decorator:

You would manually write constructor code.


----------------------------------------------------------------
9) DataIngestionConfig class
----------------------------------------------------------------

class DataIngestionConfig:

Purpose:
Stores all file paths related to ingestion.


Acts like configuration container.


----------------------------------------------------------------
10) train_data_path
----------------------------------------------------------------

train_data_path : str = os.path.join("artifacts","train.csv")

Stores path where training dataset will be saved.


Example:

artifacts/train.csv


----------------------------------------------------------------
11) test_data_path
----------------------------------------------------------------

test_data_path : str = os.path.join("artifacts","test.csv")

Stores path for test dataset.


Example:

artifacts/test.csv


----------------------------------------------------------------
12) raw_data_path
----------------------------------------------------------------

raw_data_path : str = os.path.join("artifacts","raw.csv")

Stores raw dataset path before splitting.


Example:

artifacts/raw.csv


----------------------------------------------------------------
13) DataIngestion class
----------------------------------------------------------------

class DataIngestion:

Main class responsible for executing ingestion pipeline.


----------------------------------------------------------------
14) __init__()
----------------------------------------------------------------

def __init__(self):

Constructor method.

Runs automatically when object is created.


Example:

di = DataIngestion()


----------------------------------------------------------------
15) self.ingestion_config
----------------------------------------------------------------

self.ingestion_config = DataIngestionConfig()

Creates object of configuration class.

Now class can access:

train path
test path
raw path


Example:

self.ingestion_config.train_data_path


----------------------------------------------------------------
16) initiate_data_ingestion()
----------------------------------------------------------------

def initiate_data_ingestion(self):

Main method that performs full ingestion process.


This is where actual pipeline starts.


----------------------------------------------------------------
17) logging.info()
----------------------------------------------------------------

logging.info("Entered the Data ingestion method or component")

Creates log entry.

Helps track execution flow.


----------------------------------------------------------------
18) try block
----------------------------------------------------------------

try:

Runs risky code.

If error occurs:
control moves to except block.


----------------------------------------------------------------
19) pd.read_csv()
----------------------------------------------------------------

df = pd.read_csv("notebook/stud.csv")

Reads CSV file into pandas DataFrame.


Input file:

notebook/stud.csv


Output:

df → DataFrame


----------------------------------------------------------------
20) df variable
----------------------------------------------------------------

Stores dataset after reading CSV.


Example structure:

gender | math_score | reading_score


----------------------------------------------------------------
21) os.makedirs()
----------------------------------------------------------------

os.makedirs(
    os.path.dirname(self.ingestion_config.train_data_path),
    exist_ok=True
)

Purpose:
Creates artifacts folder.


os.path.dirname()

Extracts folder name from:

artifacts/train.csv

Output:

artifacts


exist_ok=True:
prevents error if folder already exists.


----------------------------------------------------------------
22) df.to_csv()
----------------------------------------------------------------

df.to_csv(
    self.ingestion_config.raw_data_path,
    index=False,
    header=True
)

Saves original raw dataset.


index=False
-> prevents row numbers from being saved

header=True
-> saves column names


Output:

artifacts/raw.csv


----------------------------------------------------------------
23) train_test_split()
----------------------------------------------------------------

train_set, test_set = train_test_split(
    df,
    test_size=0.3,
    random_state=24
)

Splits dataset into:

70% training data
30% testing data


random_state=24

Ensures same split every time.


----------------------------------------------------------------
24) train_set
----------------------------------------------------------------

Stores training dataset.


Used to train ML model.


----------------------------------------------------------------
25) test_set
----------------------------------------------------------------

Stores testing dataset.


Used to evaluate model performance.


----------------------------------------------------------------
26) train_set.to_csv()
----------------------------------------------------------------

Saves training dataset.


Output:

artifacts/train.csv


----------------------------------------------------------------
27) test_set.to_csv()
----------------------------------------------------------------

Saves testing dataset.


Output:

artifacts/test.csv


----------------------------------------------------------------
28) return statement
----------------------------------------------------------------

return (
    self.ingestion_config.train_data_path,
    self.ingestion_config.test_data_path
)

Returns paths of saved train/test files.

These paths are used in future pipeline stages.


----------------------------------------------------------------
29) except block
----------------------------------------------------------------

except Exception as e:

Catches any error during ingestion.


Example:

missing dataset file
wrong path
CSV corruption


----------------------------------------------------------------
30) raise CustomException()
----------------------------------------------------------------

raise CustomException(e,sys)

Raises your custom formatted exception.


Shows:

- file name
- line number
- actual error


----------------------------------------------------------------
31) if __name__ == "__main__"
----------------------------------------------------------------

if __name__ == "__main__":

Runs only when this file is executed directly.


Does NOT run when imported elsewhere.


----------------------------------------------------------------
32) di variable
----------------------------------------------------------------

di = DataIngestion()

Creates object of DataIngestion class.


----------------------------------------------------------------
33) di.initiate_data_ingestion()
----------------------------------------------------------------

Starts full ingestion pipeline.


----------------------------------------------------------------
FULL EXECUTION FLOW
----------------------------------------------------------------

Program starts
    ↓
Imports modules
    ↓
Creates config paths
    ↓
Creates DataIngestion object
    ↓
Reads dataset
    ↓
Creates artifacts folder
    ↓
Saves raw dataset
    ↓
Splits train/test data
    ↓
Saves train.csv
    ↓
Saves test.csv
    ↓
Returns file paths


----------------------------------------------------------------
FINAL OUTPUT FILE STRUCTURE
----------------------------------------------------------------

artifacts/
    raw.csv
    train.csv
    test.csv


===============================================================
"""