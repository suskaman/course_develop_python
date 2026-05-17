import logging
from collections.abc import Iterable
from typing import Any, Generator

from configurate.logging_config import setup_logging
from src.data_loader import get_data_from_csv
from src.utils import get_data_from_json

generator_logger = logging.getLogger("generators")


def filter_by_currency(transactions: list[dict], currency: str) -> list[dict] | Iterable[dict[Any, Any]]:
    """this function filter transactions by currency"""
    generator_logger.info("START filter by currency")
    try:
        if transactions == [{}]:
            return transactions

        if transactions[0].get("operationAmount"):
            return filter(
                lambda item: item.get("operationAmount", {}).get("currency", {}).get("code") == currency, transactions
            )
        else:
            return filter(lambda item: item.get("currency_code") == currency, transactions)
    finally:
        generator_logger.info("END filter by currency")


def transaction_descriptions(transactions: list[dict]) -> Generator[str, str, Any]:
    """this generator return descriptions of transactions"""
    generator_logger.info("START get description of transactions")

    try:
        for trans in transactions:
            if "description" in trans:
                yield trans["description"]
    finally:
        generator_logger.info("END get description of transactions")


def card_number_generator(start: int, stop: int) -> Generator[str, str, None]:
    """this generator generate a card numbers from 'start' to 'stop'"""
    while start <= stop:
        reversed_start = str(start)[::-1]
        reversed_card_number = reversed_start + "0" * (16 - len(reversed_start))
        reversed_card_number_as_list = list(reversed_card_number)

        for i in range(len(reversed_card_number_as_list)):
            if i == 4 or i == 9 or i == 14:
                reversed_card_number_as_list.insert(i, " ")

        card_number = "".join(reversed_card_number_as_list[::-1])
        yield card_number
        start += 1


if __name__ == "__main__":
    setup_logging()
    data = get_data_from_csv("C:/Users/maks/PycharmProjects/course_develop_python/data/transactions.csv")
    data1 = get_data_from_json("C:/Users/maks/PycharmProjects/course_develop_python/data/operations.json")
    res = list(filter_by_currency(data, currency="PEN"))

    print(res)
