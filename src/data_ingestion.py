import os
import sys
import pandas as pd
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_execption import CustomException
from config.paths_config import RAW_DIR, RAW_FILE_PATH, TRAIN_FILE_PATH, TEST_FILE_PATH
from utils.common_funtions import read_yaml

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, config):
        try:
            self.config = config["data_ingestion"]
            self.bucket_name = self.config["bucket_name"]
            self.file_name = self.config["bucket_file_name"]
            self.train_test_ratio = self.config["train_ratio"]

            os.makedirs(RAW_DIR, exist_ok=True)
            logger.info(f"Data Ingestion initialized with bucket: {self.bucket_name}, file: {self.file_name}")

        except Exception as e:
            raise CustomException("Error during DataIngestion initialization", e)

    def download_csv_from_gcp(self):
        """Download CSV file from Google Cloud Storage. If file exists locally, skip download."""
        try:
            # Skip download if already present
            if os.path.exists(RAW_FILE_PATH):
                logger.info(f"Raw file already exists at {RAW_FILE_PATH}; skipping GCP download.")
                return

            client = storage.Client()
            bucket = client.bucket(self.bucket_name)
            blob = bucket.blob(self.file_name)
            blob.download_to_filename(RAW_FILE_PATH)

            logger.info(f"CSV file successfully downloaded to {RAW_FILE_PATH}")

        except Exception as e:
            logger.error("Error while downloading the CSV file from GCP")
            raise CustomException("Failed to download CSV file", e)

    def split_data(self):
        """Split CSV data into training and testing datasets"""
        try:
            logger.info("Starting train-test split")
            data = pd.read_csv(RAW_FILE_PATH)
            train_data, test_data = train_test_split(
                data, test_size=1 - self.train_test_ratio, random_state=42
            )

            train_data.to_csv(TRAIN_FILE_PATH, index=False)
            test_data.to_csv(TEST_FILE_PATH, index=False)

            logger.info(f"Train data saved to {TRAIN_FILE_PATH}")
            logger.info(f"Test data saved to {TEST_FILE_PATH}")

        except Exception as e:
            logger.error("Error while splitting data")
            raise CustomException("Failed to split data into training and test sets", e)

    def run(self):
        """Run the full data ingestion pipeline"""
        try:
            logger.info("Starting data ingestion process")
            self.download_csv_from_gcp()
            self.split_data()
            logger.info("Data ingestion completed successfully")

        except CustomException as ce:
            logger.error(f"CustomException: {str(ce)}")
            # Stop execution if something goes wrong
            sys.exit(1)

        finally:
            logger.info("Data ingestion process finished")

# Entry point
if __name__ == "__main__":
    try:
        config = read_yaml(os.environ.get("CONFIG_PATH", "config/config.yaml"))
        data_ingestion = DataIngestion(config)
        data_ingestion.run()
    except Exception as e:
        logger.error(f"Fatal error in DataIngestion script: {e}")
        sys.exit(1)
