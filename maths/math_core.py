def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
            print(".................................")
            print("!!! ОШИБКА: ДЕЛЕНИЕ НА НОЛЬ")
            print("    Повторите ввод.")
            print(".................................")
            return 0
