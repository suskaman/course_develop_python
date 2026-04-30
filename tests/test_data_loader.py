# from unittest.mock import patch
# from src import data_loader
# import pandas as pd
#
#
# def test_get_data_from_csv():
#     with patch('src.data_loader.pd.read_csv') as mock_read_csv:
#         mock_read_csv.return_value = pd.DataFrame({'one': [1, 2], 'two': [4, 5]})
#         assert data_loader.get_data_from_excel('test.csv') == [{'one': 1, 'two': 4}, {'one': 2, 'two': 5}]
#         mock_read_csv.assert_called_once_with('test.csv')


# def test_get_data_from_excel():
