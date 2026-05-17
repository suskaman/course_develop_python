import logging

from configurate.logging_config import setup_logging
from src.data_loader import get_data_from_csv, get_data_from_excel
from src.finder import process_bank_search
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import get_data_from_json
from src.widget import get_date, mask_account_card

main_logger = logging.getLogger("main")


def main() -> None:
    """The program's main function.
    Responsible for initializing the application,
    parsing command-line arguments,
    and starting the program's main loop."""

    json_file = "C:/Users/maks/PycharmProjects/course_develop_python/data/operations.json"
    csv_file = "C:/Users/maks/PycharmProjects/course_develop_python/data/transactions.csv"
    xlsx_file = "C:/Users/maks/PycharmProjects/course_develop_python/data/transactions_excel.xlsx"

    greeting = """
Привет! Добро пожаловать в программу работы с банковскими транзакциями. выберите необходимый пенкт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
    """
    status = """
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
    """

    main_logger.info("greeting")

    print(greeting)
    main_logger.info("choice_get_data")

    choice_get_data = int(input())
    if choice_get_data == 1:
        print("Для обработки выбран JSON-файл")
        data = get_data_from_json(json_file)
        main_logger.debug("get json-file")
    elif choice_get_data == 2:
        print("Для обработки выбран CSV-файл")
        data = get_data_from_csv(csv_file)
        main_logger.debug("get csv-file")
    else:
        print("Для обработки выбран XLSX-файл")
        data = get_data_from_excel(xlsx_file)
        main_logger.debug("get xlsx-file")

    main_logger.info("filter by state START")
    while True:
        print(status)
        state = input().upper()
        if state == "EXECUTED":
            print(f'Операции отфильтрованы по статусу "{state}"')
            state_data = filter_by_state(data, state)
            main_logger.debug(f"filter by {state}")
            break
        elif state == "CANCELED":
            print(f'Операции отфильтрованы по статусу "{state}"')
            state_data = filter_by_state(data, state)
            main_logger.debug(f"filter by {state}")
            break
        elif state == "PENDING":
            print(f'Операции отфильтрованы по статусу "{state}"')
            state_data = filter_by_state(data, state)
            main_logger.debug(f"filter by {state}")
            break
        else:
            main_logger.warning(f"filter by {state} unavailable")
            print(f'Статус операции "{state}" недоступен')
    main_logger.info("filter by state END")

    main_logger.info("sort by date START")
    while True:
        print("Осортирвать операции по дате? Да/Нет")
        if input().lower() == "да":
            print("Отсортировать по возрастанию или по убыванию?")
            cin = input().lower()
            if cin == "по возрастанию":
                main_logger.debug("sort by ascending")
                date_data = sort_by_date(state_data, False)
                break
            elif cin == "по убыванию":
                main_logger.debug("sort by descending")
                date_data = sort_by_date(state_data, True)
                break
            else:
                main_logger.warning("invalid value for sort by date")
                print("некорректное значение")
        else:
            date_data = state_data
            break
    main_logger.info("sort by date END")

    main_logger.info("output transactions by currency")
    print("Выводить только рублевые транзакции? Да/Нет")
    if input().lower() == "да":
        main_logger.debug("output only RUB transactions")
        currency_data = list(filter_by_currency(date_data, "RUB"))
    else:
        main_logger.debug("output all transactions")
        currency_data = list(date_data)

    main_logger.info("filter list of transactions by description")
    print("Отфильтровать список транзакций по определённому слову в описании? Да/Нет")
    if input().lower() == "да":
        print("Введите поисковые слова")
        result_data = process_bank_search(currency_data, input())
        main_logger.debug("get operations by description")
    else:
        result_data = currency_data

    print("Распечатываю итоговый список транзакций...")
    main_logger.info("return result")
    if not result_data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

    else:
        print(f"Всего банковских операций в выборке {len(result_data)}")
        for trans in result_data:
            tr_from = mask_account_card(trans.get("from"))
            tr_to = mask_account_card(trans.get("to"))
            date = get_date(trans.get("date"))

            if choice_get_data == 1:
                amount = trans.get("operationAmount", {}).get("amount")
                currency = trans.get("operationAmount", {}).get("currency", {}).get("code")
            else:
                amount = trans.get("amount")
                currency = trans.get("currency_code")

            if tr_from:
                print(f"{date} {trans.get('description')}\n" f"{tr_from} -> {tr_to}\n" f"Сумма: {amount} {currency}\n")
            else:
                print(
                    f"{trans.get('date')} - {trans.get('description')}\n" f"{tr_to}\n" f"Сумма: {amount} {currency}\n"
                )

    return None


if __name__ == "__main__":
    setup_logging()
    main()
