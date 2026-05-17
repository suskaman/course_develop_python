import logging
from typing import Union

from configurate.logging_config import setup_logging
from src import masks

widget_logger = logging.getLogger("widget")


def mask_account_card(card_info: Union[str, None]) -> str:
    """changing card info with mask"""
    if card_info is None or isinstance(card_info, float):
        widget_logger.warning("card_info cannot be None or float")
        return ""
    one = ["Maestro", "MasterCard", "МИР", "Mastercard"]
    card_info_list = card_info.split(" ")
    for value in card_info_list:
        if value == "Счет" or value == "счет" or value == "Discover":
            card_info_list[1] = masks.get_mask_account(card_info_list[1])
        elif value in one or value == "Visa" and len(card_info_list) == 2:
            card_info_list[1] = masks.get_mask_card_number(card_info_list[1])
        elif value == "Visa" and len(card_info_list) == 3 or value == "American":
            card_info_list[2] = masks.get_mask_card_number(card_info_list[2])

    return " ".join(card_info_list)


def get_date(date_time: Union[str, None]) -> str:
    """changing date info with mask"""
    if date_time is None:
        return ""
    date = date_time.split("T")[0].split("-")
    return date[2] + "." + date[1] + "." + date[0]


if __name__ == "__main__":
    setup_logging()
    print(get_date("2020-10-06T23:30:05Z"))
