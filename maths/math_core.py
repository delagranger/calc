def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
            print(".................................")
            print(f"!!! ОШИБКА: ДЕЛЕНИЕ НА НОЛЬ ({e})")
            print("    Повторите ввод.")
            print(".................................")
    else:
         return result
