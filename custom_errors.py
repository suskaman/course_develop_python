class StatusError(Exception):
    """exception class for status errors"""

    def __init__(self, *args: object):
        if args:
            self.status_code = args[0]
        else:
            self.status_code = None

    def __str__(self) -> str:
        return "Status Error {0}".format(self.status_code)


class EmptyError(Exception):
    """exception class for empty errors"""

    def __init__(self, *args: object):
        if args:
            self.empty = args[0]
        else:
            self.empty = None

    def __str__(self) -> str:
        if self.empty:
            return f"{self.empty}"
        else:
            return "empty error"
