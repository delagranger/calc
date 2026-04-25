from math import pow, factorial

def exponentiation(a, b):
    try:
        return pow(a, b)
    except ValueError:
        print("!!! ОШИБКА: РАССЧЕТ НЕВОЗМОЖЕН")
    except (OverflowError, MemoryError):
        print("!!! ОШИБКА: СЛИШКОМ БОЛЬШОЕ ЧИСЛО")


def square_root(a, b):
    try:
        return pow(a, 1/b)
    except ValueError:
        print("!!! ОШИБКА: РАССЧЕТ НЕВОЗМОЖЕН")
    except ZeroDivisionError:
        print("!!! ОШИБКА: ДЕЛЕНИЕ НА НОЛЬ")
    except (OverflowError, MemoryError):
        print("!!! ОШИБКА: СЛИШКОМ БОЛЬШОЕ ЧИСЛО")


def remainder_of_division(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        print("!!! ОШИБКА: ДЕЛЕНИЕ НА НОЛЬ")


def integer_division(a, b):
    try:
        return a // b
    except ZeroDivisionError:
        print("!!! ОШИБКА: ДЕЛЕНИЕ НА НОЛЬ")


def modulus(a):
    return abs(a)


def fctr(a):
    try:
        return factorial(int(a))
    except (OverflowError, MemoryError):
        print("!!! ОШИБКА: СЛИШКОМ БОЛЬШОЕ ЧИСЛО")
    except ValueError:
        print("!!! ОШИБКА: РАССЧЕТ НЕВОЗМОЖЕН")


def change_of_sign(a):
    a -= a * 2
    return a

