from typing import TYPE_CHECKING

import pytest

import src.decorators as dec

# Необходим, чтобы не импортировать внутренние модули pytest при реальном запуске тестов,
# так как это может вызвать ошибку
if TYPE_CHECKING:
    from _pytest.capture import CaptureFixture


@dec.log()
def func_for_test_log(a: int, b: int) -> float:
    """function for testing decorator"""
    return a / b


def test_decorator(capsys: "CaptureFixture[str]") -> None:
    func_for_test_log(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "func_for_test_log ok\nresult: 0.5\n"


def test_decorator_with_exception(capsys: "CaptureFixture[str]") -> None:
    with pytest.raises(Exception, match="division by zero"):
        func_for_test_log(1, 0)

    captured = capsys.readouterr()
    assert captured.out == "func_for_test_log error: ZeroDivisionError. Inputs:(((1, 0), {}))\n"
