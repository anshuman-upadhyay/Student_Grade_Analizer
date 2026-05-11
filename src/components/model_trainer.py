#Will be used to train the model and tune the hyperparameter
import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import AdaBoostRegressor,GradientBoostingRegressor,RandomForestRegressor

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.execption import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    

    def  initiate_model_trainer(self,training_arr,test_arr,):
        try:
            logging.info("Splitting the training and test input data")
            x_train,y_train,x_test,y_test = (
                training_arr[:,:-1],
                training_arr[:,-1],
                
                test_arr[:,:-1],
                test_arr[:,-1],

            )
            models = {
                "LinearRegression": LinearRegression(),
                "KNeighborsRegressor": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
                "Gradient Boosting" : GradientBoostingRegressor()
            }

            model_report :dict = evaluate_models(
                X_train=x_train,
                y_train=y_train,
                X_test = x_test,
                y_test=y_test,
                models= models
                )
            #to get the best model score form dict 
            best_model_score = max(sorted(model_report.values()))

            #toget the best model name from dict
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]
            if best_model_score<0.6 :
                raise CustomException("No best model found",None)
            logging.info(f"Best Found model on both training and testing dataset : {best_model}")

            save_object(
                file_path= self.model_trainer_config.trained_model_file_path,
                obj= best_model
            )
            predicted = best_model.predict(x_test)
            r2 = r2_score(y_test,predicted)
            return r2
        except Exception as e:
            raise CustomException(e,sys)