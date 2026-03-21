from src import generators


def test_filter_by_currency(
    result_for_filter_by_currency: list[dict], list_for_filter_by_currency: list[dict]
) -> None:
    assert list(generators.filter_by_currency(list_for_filter_by_currency, "USD")) == result_for_filter_by_currency
    assert generators.filter_by_currency([{}], "USD") == [{}]
    assert list(generators.filter_by_currency(list_for_filter_by_currency, "EUR")) == []


def test_transaction_descriptions(list_for_filter_by_currency: list[dict]) -> None:
    generator = generators.transaction_descriptions(list_for_filter_by_currency)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"
    try:
        assert next(generator)
    except StopIteration:
        pass


def test_transaction_descriptions_empty() -> None:
    generator = generators.transaction_descriptions([{}])
    try:
        assert next(generator)
    except StopIteration:
        pass


def test_card_number_generator() -> None:
    generator = generators.card_number_generator(1, 5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"


def test_card_number_generator_last_numbers() -> None:
    generator = generators.card_number_generator(9999999999999995, 9999999999999999)
    assert next(generator) == "9999 9999 9999 9995"
    assert next(generator) == "9999 9999 9999 9996"
    assert next(generator) == "9999 9999 9999 9997"
    assert next(generator) == "9999 9999 9999 9998"
    assert next(generator) == "9999 9999 9999 9999"
    try:
        assert next(generator) == [{}]
    except StopIteration:
        pass
