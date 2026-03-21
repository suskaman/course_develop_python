import pytest

from src import widget


@pytest.mark.parametrize(
    "string, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_mask_account_card(string: str, expected: str) -> None:
    assert widget.mask_account_card(string) == expected


def test_get_date(date_time_input: str, date_time_output: str) -> None:
    assert widget.get_date(date_time_input) == date_time_output
