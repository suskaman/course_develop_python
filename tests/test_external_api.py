import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import get_amount_from_transaction


def test_get_amount_from_transaction(list_of_transactions: list[dict]) -> None:
    with patch("requests.get") as get_amount:
        get_amount.return_value.json.return_value = {"result": 999}
        assert get_amount_from_transaction(list_of_transactions[0]) == 999

        load_dotenv()
        api_key = os.getenv("API_KEY")

        headers = {"apikey": f"{api_key}"}

        url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=9824.07"
        get_amount.assert_called_with(url, headers=headers)
