from collections.abc import Iterable
from typing import Any, Generator


def filter_by_currency(transactions: list[dict], currency: str) -> list[dict] | Iterable[dict[Any, Any]]:
    """this function filter transactions by currency"""
    if transactions == [{}]:
        return transactions
    return filter(lambda item: item["operationAmount"]["currency"]["name"] == currency, transactions)


def transaction_descriptions(transactions: list[dict]) -> Generator[str, str, Any]:
    """this generator return descriptions of transactions"""
    for trans in transactions:
        if "description" in trans:
            yield trans["description"]


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
