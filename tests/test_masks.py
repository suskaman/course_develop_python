import pytest

from src import masks


@pytest.mark.parametrize(
    "string, expected", [("7000792289606361", "7000 79** **** 6361"), ("7656735609851331", "7656 73** **** 1331")]
)
def test_get_mask_card_number(string: str, expected: str) -> None:
    assert masks.get_mask_card_number(string) == expected


@pytest.mark.parametrize("string, expected", [("73654108430135874305", "**4305"), ("98341501723874563492", "**3492")])
def test_get_mask_account(string: str, expected: str) -> None:
    assert masks.get_mask_account(string) == expected
