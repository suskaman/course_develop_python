import pandas as pd
import logging

# create logger
data_logger = logging.getLogger("app.data_logger")
file_handler = logging.FileHandler("../logs/data_logger.log", mode='w', encoding='utf-8')
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
data_logger.addHandler(file_handler)
data_logger.setLevel(logging.DEBUG)

def get_data_from_csv(path_to_csv: str):
    """this function gets the data from the csv file"""
    data_logger.info("START getting data from csv")

    try:
        df = pd.read_csv(path_to_csv)

        return df.to_dict(orient='records')

    except FileNotFoundError:
        data_logger.error('invalid file path')
        return None

    finally:
        data_logger.info("END getting data from csv")

def get_data_from_excel(path_to_xlsx: str):
    """this function gets the data from the excel file"""
    data_logger.info('START getting data from excel')

    try:
        df = pd.read_excel(path_to_xlsx)

        return df.to_dict(orient='records')

    except FileNotFoundError:
        data_logger.error('invalid file path')
        return None

    finally:
        data_logger.info("END getting data from excel")

if __name__ == '__main__':
    print(get_data_from_csv('../data/transactions.csv'))
    print(get_data_from_excel('../data/transactions_excel.xlsx'))