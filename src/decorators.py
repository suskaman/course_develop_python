import sys
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

# TypeVar для возвращаемого значения
R = TypeVar("R")
# ParamSpec для типов аргументов
P = ParamSpec("P")


def log(filename: str = ""):
    """This decorator logs the start and end of the function execution, as well as its results or errors that occurred"""
    def my_decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            target = open(filename, "w") if filename else sys.stdout

            try:
                res = func(*args, **kwargs)
                print(f"{func.__name__} ok\n" f"result: {res}", file=target)

            except Exception as e:
                print(f"{func.__name__} error: {type(e).__name__}. Inputs:({args, kwargs})", file=target)

            finally:
                if filename:
                    target.close()

            return func(*args, **kwargs)

        return wrapper

    return my_decorator


# Callable[[ArgTypes], ReturnType]:Тип, описывающий функцию, где [ArgTypes]— список типов аргументов,
#   а ReturnType — тип возвращаемого значения.
# TypeVar: Используется для обобщения (generics), чтобы декоратор возвращал функцию того же типа, что и принял.
# ParamSpec: Используется для точной передачи аргументов *args и **kwargs от исходной функции к обертке.
