import pandas as pd
from .logger import Logger

class DataProcessor:
    def __init__(self):
        self.data = None
        self.logger = Logger()

    def set_data(self, data):
        self.data = data
        self.logger.log("Data set for processing", "INFO")

    def clean_data(self):
        self.data.drop_duplicates(inplace=True)
        self.data.fillna({
            'Price': self.data['Price'].mean(),
            'Quantity': self.data['Quantity'].mean()
        }, inplace=True)
        self.logger.log("Data cleaned", "INFO")

    def transform_data(self):
        self.data['Price'] = self.data['Price'] * 1.1
        self.logger.log("Data transformed", "INFO")