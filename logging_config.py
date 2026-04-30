import logging.config


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "console": {
            "format": '"%(asctime)s" | "%(levelname)-8s" | "%(funcName)s" | %(name)s | "%(message)s"',
        },
        "file": {
            "format": (
                "%(asctime)s | %(levelname)-8s | %(name)s | "
                '%(filename)s:%(lineno)d | %(funcName)s() | "%(message)s"'
            ),
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "console",
            "stream": "ext://sys.stdout",
        },

        "file_data_loader": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "file",
            "filename": "../logs/data_loader.log",
            "encoding": "utf-8",
            "mode": "w",
        },

        "file_masks": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "file",
            "filename": "../logs/masks.log",
            "encoding": "utf-8",
            "mode": "w",
        },

        "file_utils": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "file",
            "filename": "../logs/utils.log",
            "encoding": "utf-8",
            "mode": "w",
        },

        "file_root": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "file",
            "filename": "../logs/app.log",
            "maxBytes": 1024,
            "backupCount": 5,
            "encoding": "utf-8",
            "mode": "w",
        }
    },

    "loggers": {
        "data_loader": {
            "level": "DEBUG",
            "handlers": ["file_data_loader"],
            "propagate": False,
        },
        "masks": {
            "level": "DEBUG",
            "handlers": ["file_masks"],
            "propagate": False,
        },
        "utils": {
            "level": "DEBUG",
            "handlers": ["file_utils"],
            "propagate": False,
        },
    },

    "root": {
        "level": "DEBUG",
        "handlers": ["file_root"],
    },
}


def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
