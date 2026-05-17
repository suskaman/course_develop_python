from src import finder


def test_process_bank_search(list_of_transactions: list[dict]) -> None:
    assert finder.process_bank_search(list_of_transactions, "Перевод с карты на карту") == [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }
    ]


def test_process_bank_operations(list_of_transactions: list[dict]) -> None:
    assert (
        finder.process_bank_operations(list_of_transactions, ["Перевод с карты на карту", "Перевод организации"])
    ) == {
        "Перевод организации": 2,
        "Перевод с карты на карту": 1,
    }
