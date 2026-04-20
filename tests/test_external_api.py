import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import get_amount_from_transaction


def test_get_amount_from_transaction(list_for_filter_by_currency: list[dict]) -> None:
    with patch("requests.request") as get_amount:
        get_amount.return_value.json.return_value = {"result": 747995.98}
        assert get_amount_from_transaction(list_for_filter_by_currency[0]) == 747995.98

        load_dotenv()
        api_key = os.getenv("API_KEY")

        payload: dict = {}
        headers = {"apikey": f"{api_key}"}

        url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=9824.07"
        get_amount.assert_called_with("GET", url, headers=headers, data=payload)
