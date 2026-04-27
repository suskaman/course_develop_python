import json
import logging

# create logger
util_logger = logging.getLogger("app.utilss")
file_handler = logging.FileHandler('../logs/utils.log', mode='w')
console_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
file_handler.setFormatter(console_formatter)
util_logger.addHandler(file_handler)
util_logger.setLevel(logging.DEBUG)


def get_transactions(path_to_json: str) -> list:
    """return a list of all transactions"""
    util_logger.info('start getting transactions')
    try:
        with open(path_to_json, "r", encoding="utf-8") as f:
            util_logger.info('opened json file')

            data = json.load(f)

            if not isinstance(data, list):
                raise ValueError("json file must contain a list of transactions")

            util_logger.info('transactions are got')
            return data

    except FileNotFoundError:
        util_logger.error("transactions are not found, please check the path", exc_info=True)
        return [{}]

    except json.decoder.JSONDecodeError:
        util_logger.error("invalid json file", exc_info=True)
        return [{}]

    except ValueError :
        util_logger.error(f"json file must contain a list of transactions", exc_info=True)
        return [{}]

    finally:
        util_logger.info('end getting transactions')



if __name__ == "__main__":
    print(get_transactions("../data/operations.json"))
