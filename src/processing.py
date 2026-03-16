def filter_by_state(list_of_dict: list[dict], state: str = "EXECUTED") -> list:
    """this function filter the list of dict by state"""
    filtered_list = []

    for list_item in list_of_dict:
        if list_item["state"] == state:
            filtered_list.append(list_item)

    return filtered_list


def sort_by_date(list_of_dict: list[dict], sort_order: bool = True) -> list:
    """this function sort the list of dict by date"""

    return sorted(list_of_dict, key=lambda x: x["date"], reverse=sort_order)
