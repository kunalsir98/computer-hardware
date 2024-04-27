import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        



class CustomData:
    def __init__(self,
                 MYCT: int,
                 MMIN: int,
                 MMAX: int,
                 CACH: int,
                 CHMIN: int,
                 CHMAX: int,
                 PRP: int,
                 ERP: int):
        
        self.MYCT = MYCT
        self.MMIN = MMIN
        self.MMAX = MMAX
        self.CACH = CACH
        self.CHMIN = CHMIN
        self.CHMAX = CHMAX
        self.PRP = PRP
        self.ERP = ERP

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'MYCT': [self.MYCT],
                'MMIN': [self.MMIN],
                'MMAX': [self.MMAX],
                'CACH': [self.CACH],
                'CHMIN': [self.CHMIN],
                'CHMAX': [self.CHMAX],
                'PRP': [self.PRP],
                'ERP': [self.ERP]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.error('Exception occurred in data transformation process')
            raise CustomException(e, sys)
