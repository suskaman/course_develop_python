import logging
from typing import Union

from configurate.logging_config import setup_logging

# create logger
mask_logger = logging.getLogger("masks")


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """changing card number with mask"""
    mask_logger.info("START to create a mask for card number")

    mask_str = "XXXX XX** **** XXXX"
    mask_list = list(mask_str)
    card_number_str = str(card_number)
    counter = 0
    try:

        if len(card_number_str) != 16:
            raise IndexError("Invalid card number")

        for i in range(len(mask_list)):
            if mask_list[i] == "X":
                mask_list[i] = card_number_str[counter]
                counter += 1
            elif mask_list[i] == "*":
                counter += 1
        mask_card_number = "".join(mask_list)

        mask_logger.info("a mask for card number is created")
        return mask_card_number

    except IndexError as ex:
        mask_logger.error(f"error happened: {ex}", exc_info=True)
        return ""

    finally:
        mask_logger.info("END getting mask card number")


def get_mask_account(account_number: Union[int, str]) -> str:
    """changing account number with mask"""
    mask_logger.info("START to create a mask for account number ")

    mask_str = "**XXXX"
    mask_list = list(mask_str)
    len_mask_str = len(mask_str)
    card_number_str = str(account_number)[-len_mask_str:]
    counter = 0

    try:
        if not account_number:
            raise IndexError("Invalid account number")

        for i in range(len(mask_list)):
            if mask_list[i] == "X":
                mask_list[i] = card_number_str[counter]
                counter += 1
            elif mask_list[i] == "*":
                counter += 1

        mask_account_number = "".join(mask_list)

        mask_logger.info("a mask for account number is created")
        return mask_account_number

    except IndexError as ex:
        mask_logger.error(f"error happened: {ex}", exc_info=True)
        return ""

    finally:
        mask_logger.info("END getting mask account number")


if __name__ == "__main__":
    setup_logging()
