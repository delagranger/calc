def Addition(a, b):
    return a + b


def Subtraction(a, b):
    return a - b


def Multiplication(a, b):
    return a * b


def Division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Ошибка: на ноль делить нельзя")