from src import processing


def test_filter_by_state_like_executed(list_of_dict_input: list[dict], list_of_dict_output_executed: list[dict]) -> None:
    assert processing.filter_by_state(list_of_dict_input, state="EXECUTED") == list_of_dict_output_executed


def test_filter_by_state_like_canceled(list_of_dict_input: list[dict], list_of_dict_output_canceled: list[dict]) -> None:
    assert processing.filter_by_state(list_of_dict_input, state="CANCELED") == list_of_dict_output_canceled


def test_sort_by_date(list_of_dict_input: list[dict], list_of_dict_sorted_by_date: list[dict]) -> None:
    assert processing.sort_by_date(list_of_dict_input) == list_of_dict_sorted_by_date
