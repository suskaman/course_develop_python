import collections as col
import logging
import re

from configurate.logging_config import setup_logging
from custom_errors import EmptyError

# create logger
finder_logger = logging.getLogger("finder")


def process_bank_search(data: list[dict], search_description: str) -> list[dict]:
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
            if re.search(search_description, str(transaction.get("description", "")), re.IGNORECASE)
        ]
        finder_logger.info("return a list of dicts with transactions which filtered by search description")
        return found_transactions

    except TypeError:
        finder_logger.error("Your search string is not string")
        return [{}]
    except EmptyError:
        finder_logger.error("Your data is empty")
        return [{}]
    except Exception as e:
        finder_logger.error("unknown error: {}".format(e))
        return [{}]

    finally:
        finder_logger.info("END Processing Bank Search")


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """The function counts the number of transactions by category"""
    finder_logger.info("START Processing Bank Search")
    try:
        if data == [{}]:
            raise EmptyError()
        if not isinstance(categories, list):
            raise TypeError("your categories is not a list")

        categories_dict: dict[str, int] = {}
        for category in categories:
            if not isinstance(category, str):
                raise TypeError("your categories is not a string")

            bank_search = process_bank_search(data, category)
            list_of_operations = [trans["description"] for trans in bank_search if trans.get("description")]
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


if __name__ == "__main__":
    setup_logging()
