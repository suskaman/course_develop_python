from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """changing card number with mask"""

    mask_str = "XXXX XX** **** XXXX"
    mask_list = list(mask_str)
    card_number_str = str(card_number)
    counter = 0

    if len(card_number_str) != 16:
        raise Exception("Invalid card number")

    for i in range(len(mask_list)):
        if mask_list[i] == "X":
            mask_list[i] = card_number_str[counter]
            counter += 1
        elif mask_list[i] == "*":
            counter += 1

    mask_card_number = "".join(mask_list)

    return mask_card_number


def get_mask_account(account_number: Union[int, str]) -> str:
    """changing account number with mask"""

    mask_str = "**XXXX"
    mask_list = list(mask_str)
    len_mask_str = len(mask_str)
    card_number_str = str(account_number)[-len_mask_str:]
    counter = 0

    for i in range(len(mask_list)):
        if mask_list[i] == "X":
            mask_list[i] = card_number_str[counter]
            counter += 1
        elif mask_list[i] == "*":
            counter += 1

    mask_account_number = "".join(mask_list)

    return mask_account_number
