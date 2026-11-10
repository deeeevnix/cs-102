"""Простой консольный калькулятор: сложение, вычитание, умножение, деление, остаток и степень."""

import math
from typing import Callable, Dict


def add(first: float, second: float) -> float:
    """Сложение."""
    return first + second


def subtract(first: float, second: float) -> float:
    """Вычитание."""
    return first - second


def multiply(first: float, second: float) -> float:
    """Умножение."""
    return first * second


def divide(first: float, second: float) -> float:
    """Деление. При делении на ноль выбрасывает ZeroDivisionError."""
    if second == 0:
        raise ZeroDivisionError("деление на ноль невозможно")
    return first / second


def modulo(first: float, second: float) -> float:
    """Остаток от деления. При делении на ноль выбрасывает ZeroDivisionError."""
    if second == 0:
        raise ZeroDivisionError("деление на ноль невозможно")
    return first % second


def power(first: float, second: float) -> float:
    """Возведение в степень. Для недопустимых значений (например, (-8) ** 0.5) выбрасывает ValueError."""
    return math.pow(first, second)


OPERATIONS: Dict[str, Callable[[float, float], float]] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulo,
    "**": power,
}


def calculate(first: float, operator: str, second: float) -> float:
    """Выполняет операцию operator над числами first и second."""
    if operator not in OPERATIONS:
        raise ValueError(f"неизвестная операция: {operator}")
    return OPERATIONS[operator](first, second)


def read_number(prompt: str) -> float:
    """Запрашивает число у пользователя, пока он не введёт корректное значение."""
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Это не число, попробуйте ещё раз.")


def main() -> None:
    """Запускает калькулятор в консоли."""
    print("Калькулятор. Операции: + - * / % ** (степень).")
    while True:
        operator = input("Введите операцию или q для выхода: ").strip()
        if operator == "q":
            break
        if operator not in OPERATIONS:
            print("Неизвестная операция, попробуйте ещё раз.")
            continue
        first = read_number("Первое число: ")
        second = read_number("Второе число: ")
        try:
            print(f"Результат: {calculate(first, operator, second)}")
        except (ZeroDivisionError, ValueError, OverflowError) as error:
            print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
