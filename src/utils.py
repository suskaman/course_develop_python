import json
import logging

from logging_config import setup_logging

# create logger
util_logger = logging.getLogger("utils")


def get_transactions(path_to_json: str) -> list:
    """return a list of all transactions"""
    util_logger.info("START getting transactions")
    try:
        with open(path_to_json, "r", encoding="utf-8") as f:
            util_logger.info("opened json file")

            data = json.load(f)

            if not isinstance(data, list):
                raise ValueError("json file must contain a list of transactions")

            util_logger.info("transactions are got")
            return data

    except FileNotFoundError:
        util_logger.error("transactions are not found, please check the path", exc_info=True)
        return [{}]

    except json.decoder.JSONDecodeError:
        util_logger.error("invalid json file", exc_info=True)
        return [{}]

    except ValueError:
        util_logger.error("json file must contain a list of transactions", exc_info=True)
        return [{}]

    finally:
        util_logger.info("END getting transactions")


if __name__ == "__main__":
    setup_logging()
