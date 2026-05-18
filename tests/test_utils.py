from unittest.mock import mock_open, patch

from src.utils import get_data_from_json


def test_get_transactions() -> None:
    with patch("builtins.open", mock_open(read_data='[{"id": 111}]')):
        assert get_data_from_json("test.json") == [{"id": 111}]
