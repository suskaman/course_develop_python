def get_mask_card_number(card_number: int) -> str:
    """changing card number with mask"""

    mask_str = "XXXX XX** **** XXXX"
    mask_list = list(mask_str)
    card_number_str = str(card_number)
    counter = 0

    for i in range(len(mask_list)):
        if mask_list[i] == "X":
            mask_list[i] = card_number_str[counter]
            counter += 1
        elif mask_list[i] == "*":
            counter += 1

    mask_str = "".join(mask_list)

    return mask_str


def get_mask_account(account_number: int) -> str:
    """changing account number with mask"""

    mask_str = "**XXXX"
    mask_list = list(mask_str)
    card_number_str = str(account_number)[-len(mask_str):]
    counter = 0

    for i in range(len(mask_list)):
        if mask_list[i] == "X":
            mask_list[i] = card_number_str[counter]
            counter += 1
        elif mask_list[i] == "*":
            counter += 1

    mask_str = "".join(mask_list)

    return mask_str
