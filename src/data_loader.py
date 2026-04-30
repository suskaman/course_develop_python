import pandas as pd
from logging_config import setup_logging
import logging
# create logger
data_logger = logging.getLogger("data_loader")

def get_data_from_csv(path_to_csv: str):
    """this function gets the data from the csv file"""
    data_logger.info("START getting data from csv")

    try:
        df = pd.read_csv(path_to_csv)
        data_logger.info("CSV file loaded")
        return df.to_dict(orient='records')

    except FileNotFoundError:
        data_logger.error('invalid file path')
        return [{}]

    except pd.errors.EmptyDataError:
        data_logger.error("CSV file is empty")
        return [{}]

    finally:
        data_logger.info("FINISH")

def get_data_from_excel(path_to_xlsx: str):
    """this function gets the data from the excel file"""
    data_logger.info('START getting data from excel')

    try:
        df = pd.read_excel(path_to_xlsx)
        data_logger.info("Excel file loaded")
        return df.to_dict(orient='records')

    except FileNotFoundError:
        data_logger.error('invalid file path')
        return [{}]

    except pd.errors.EmptyDataError:
        data_logger.error("EXCEL file is empty")
        return [{}]

    finally:
        data_logger.info("FINISH")

if __name__ == '__main__':
    setup_logging()

    get_data_from_csv('../data/transactions.csv')
