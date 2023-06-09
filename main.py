from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os
import sys
from Insurance.utils import get_collection_as_dataframe
from Insurance.entity.config_entity import DataIngestionConfig
from Insurance.entity import config_entity
from Insurance.components.data_ingestion import DataIngestion

# def test_logger_and_exception():
# try:
# logging.info('Starting the test-logger_and_exception')
# result = 3 / 0
# print(result)
# logging.info('Ending point of the test-logger_and_exception')
# except Exception as e:
#  logging.debug(str(e))
# raise InsuranceException(e, sys)


if __name__ == '__main__':
    try:
        #   start_training_pipeline()
     #  test_logger_and_exception()
        # get_collection_as_dataframe(
        #     database_name='INSURANCE', collection_name='INSURANCE_PROJECT')
        training_pipeline_config = config_entity.TrainingPipelineConfig()

        # data ingestion
        data_ingestion_config = config_entity.DataIngestionConfig(
            training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
        data_ingestion = DataIngestion(
            data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

    except Exception as e:
        print(e)
