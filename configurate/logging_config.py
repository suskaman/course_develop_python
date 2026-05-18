import logging.config

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": '["%(asctime)s"] | "%(levelname)s" | "%(funcName)s" | %(name)s | "%(message)s"',
        },
        "file": {
            "format": (
                "[%(asctime)s] | %(levelname)s | %(name)s | "
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
            "level": "DEBUG",
            "formatter": "file",
            "filename": "C:/Users/maks/PycharmProjects/course_develop_python/logs/data_loader.log",
            "encoding": "utf-8",
            "mode": "w",
        },
        "file_masks": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "file",
            "filename": "C:/Users/maks/PycharmProjects/course_develop_python/logs/masks.log",
            "encoding": "utf-8",
            "mode": "w",
        },
        "file_utils": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "file",
            "filename": "C:/Users/maks/PycharmProjects/course_develop_python/logs/utils.log",
            "encoding": "utf-8",
            "mode": "w",
        },
        "file_finder": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "file",
            "filename": "C:/Users/maks/PycharmProjects/course_develop_python/logs/finder.log",
            "encoding": "utf-8",
            "mode": "w",
        },
        "file_external_api": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "file",
            "filename": "C:/Users/maks/PycharmProjects/course_develop_python/logs/external_api.log",
            "encoding": "utf-8",
            "mode": "w",
        },
        "file_generators": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "file",
            "filename": "C:/Users/maks/PycharmProjects/course_develop_python/logs/generators.log",
            "encoding": "utf-8",
            "mode": "w",
        },
        "file_processing": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "file",
            "filename": "C:/Users/maks/PycharmProjects/course_develop_python/logs/processing.log",
            "encoding": "utf-8",
            "mode": "w",
        },
        "file_widget": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "file",
            "filename": "C:/Users/maks/PycharmProjects/course_develop_python/logs/widget.log",
            "encoding": "utf-8",
            "mode": "w",
        },
        "file_main": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "file",
            "filename": "C:/Users/maks/PycharmProjects/course_develop_python/logs/main.log",
            "encoding": "utf-8",
            "mode": "w",
        },
        "file_root": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "file",
            "filename": "C:/Users/maks/PycharmProjects/course_develop_python/logs/app.log",
            "maxBytes": 1024,
            "backupCount": 5,
            "encoding": "utf-8",
            "mode": "w",
        },
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
        "finder": {
            "level": "DEBUG",
            "handlers": ["file_finder"],
            "propagate": False,
        },
        "external_api": {
            "level": "DEBUG",
            "handlers": ["file_external_api"],
            "propagate": False,
        },
        "generators": {
            "level": "DEBUG",
            "handlers": ["file_generators"],
            "propagate": False,
        },
        "processing": {
            "level": "DEBUG",
            "handlers": ["file_processing"],
            "propagate": False,
        },
        "widget": {
            "level": "DEBUG",
            "handlers": ["file_widget"],
            "propagate": False,
        },
        "main": {
            "level": "DEBUG",
            "handlers": ["file_main"],
            "propagate": False,
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["file_root"],
    },
}


def setup_logging() -> None:
    logging.config.dictConfig(LOGGING_CONFIG)
