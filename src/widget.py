from src import masks


def mask_account_card(card_info: str) -> str:
    """changing card info with mask"""
    card_info_list = card_info.split(" ")

    for value in card_info_list:
        if value == "Счет" or value == "счет":
            card_info_list[1] = masks.get_mask_account(card_info_list[1])
        elif value == "Maestro" or value == "MasterCard":
            card_info_list[1] = masks.get_mask_card_number(card_info_list[1])
        elif value == "Visa":
            card_info_list[2] = masks.get_mask_card_number(card_info_list[2])

    return " ".join(card_info_list)


def get_date(date_time: str) -> str:
    """changing date info with mask"""
    date = date_time.split("T")[0].split("-")
    return date[2] + "." + date[1] + "." + date[0]
