from unittest.mock import patch

import pandas as pd

from src import data_loader


def test_get_data_from_csv() -> None:
    with patch("src.data_loader.pd.read_csv") as mock_read_csv:
        mock_read_csv.return_value = pd.DataFrame({"one": [1, 2], "two": [4, 5]})
        assert data_loader.get_data_from_csv("test.csv") == [{"one": 1, "two": 4}, {"one": 2, "two": 5}]
        mock_read_csv.assert_called_once_with("test.csv")


def test_get_data_from_excel() -> None:
    with patch("src.data_loader.pd.read_excel") as mock_read_excel:
        mock_read_excel.return_value = pd.DataFrame({"one": [1, 2], "two": [4, 5]})
        assert data_loader.get_data_from_excel("test.xlsx") == [{"one": 1, "two": 4}, {"one": 2, "two": 5}]
        mock_read_excel.assert_called_once_with("test.xlsx")
