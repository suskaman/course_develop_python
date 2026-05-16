import logging
import re
import collections as col
from custom_errors import EmptyError
from configurate.logging_config import setup_logging
from data_loader import get_data_from_csv

# create logger
finder_logger = logging.getLogger('finder')

def process_bank_search(data:list[dict], search_description:str) -> list[dict]:
    """The function found the transactions by description search"""
    finder_logger.info("START Processing Bank Search")
    try:
        if not isinstance(search_description, str):
            raise TypeError()
        if data == [{}]:
            raise EmptyError()

        found_transactions = [
            transaction
            for transaction in data
            if transaction['description']
            and re.search(search_description, str(transaction))
        ]
        finder_logger.info("return a list of dicts with transactions which filtered by search description")
        return found_transactions

    except TypeError:
        finder_logger.error("Your search string is not string")
        return [{}]
    except EmptyError:
        finder_logger.error("Your data is empty")
        return [{}]

    finally:
        finder_logger.info("END Processing Bank Search")

def process_bank_operations(data:list[dict], categories:list) -> dict:
    """The function counts the number of transactions by category"""
    finder_logger.info("START Processing Bank Search")
    try:
        if data == [{}]:
            raise EmptyError()
        if not isinstance(categories, list):
            raise TypeError('your categories is not a list')

        categories_dict = {}
        for category in categories:
            if not isinstance(category, str):
                raise TypeError('your categories is not a string')

            bank_search = process_bank_search(data, category)
            list_of_operations = [
                trans['description']
                for trans in bank_search
                if trans['description']
            ]
            count = col.Counter(list_of_operations)
            categories_dict.update(count)

        finder_logger.info("return a dict with category-count")

        return categories_dict

    except EmptyError:
        finder_logger.error("Your data is empty")
        return {}
    except TypeError as e:
        finder_logger.error(e)
        return {}

    finally:
        finder_logger.info("END Processing Bank Search")

и
if __name__ == '__main__':
    setup_logging()
    # operations = process_bank_operations([{}], ['Открытие вклада', 'Перевод организации'])
    search = process_bank_search(get_data_from_csv('../data/transactions.csv'), 'Открытие вклада')
    print(search)
