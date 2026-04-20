from unittest.mock import mock_open, patch

from src.utils import get_transactions


def test_get_transactions() -> None:
    with patch("builtins.open", mock_open(read_data='[{"id": 441945886}]')):
        assert get_transactions("test.json") == [{"id": 441945886}]
