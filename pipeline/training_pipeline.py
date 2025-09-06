from src.data_ingestion import DataIngestion
from utils.common_funtions import read_yaml
from config.paths_config import *
import sys
import os


if __name__=="__main__":
    # 1. Data Ingestion (download or use existing raw.csv and split into train/test)
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()