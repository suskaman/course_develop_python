import os
from typing import Any

import requests
from dotenv import load_dotenv

from custom_errors import EmptyError, StatusError

load_dotenv()
api_key = os.getenv("API_KEY")

payload: dict = {}
headers = {"apikey": f"{api_key}"}


def get_amount_from_transaction(transaction: dict) -> float | None | Any:
    """this function gets the amount from the transaction
    if currency is an EUR or USD then it converts it to RUB and return"""

    try:
        if not transaction:
            raise EmptyError("your transaction is empty")

        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["code"]

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        response = requests.request("GET", url, headers=headers, data=payload)

        status_code = response.status_code
        result = response.json()

        if int(status_code) >= 400:
            raise StatusError(status_code)

        return round(result["result", 2])

    except StatusError as se:
        print(se.__str__())
    except EmptyError as e:
        print(e.__str__())
    except KeyError:
        print("KeyError: can not find key")

    return None
