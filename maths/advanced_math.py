from math import pow, factorial

def exponentiation(a, b):
    try:
        return pow(a, b)
    except ValueError:
        print("..............................")
        print("!!! ОШИБКА: РАССЧЕТ НЕВОЗМОЖЕН")
        print("..............................")
        return 0
    except (OverflowError, MemoryError):
        print(".................................")
        print("!!! ОШИБКА: СЛИШКОМ БОЛЬШОЕ ЧИСЛО")
        print(".................................")
        return 0


def square_root(a, b):
    try:
        return pow(a, 1/b)
    except ValueError:
        print("..............................")
        print("!!! ОШИБКА: РАССЧЕТ НЕВОЗМОЖЕН")
        print("..............................")
        return 0
    except ZeroDivisionError:
        print("...........................")
        print("!!! ОШИБКА: ДЕЛЕНИЕ НА НОЛЬ")
        print("...........................")
        return 0
    except (OverflowError, MemoryError):
        print(".................................")
        print("!!! ОШИБКА: СЛИШКОМ БОЛЬШОЕ ЧИСЛО")
        print(".................................")
        return 0


def remainder_of_division(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        print("............................")
        print("!!! ОШИБКА: ДЕЛЕНИЕ НА НОЛЬ")
        print("............................")
        return 0


def integer_division(a, b):
    try:
        return a // b
    except ZeroDivisionError:
        print("............................")
        print("!!! ОШИБКА: ДЕЛЕНИЕ НА НОЛЬ")
        print("............................")
        return 0


def modulus(a):
    return abs(a)


def fctr(a):
    try:
        return factorial(int(a))
    except (OverflowError, MemoryError):
        print(".................................")
        print("!!! ОШИБКА: СЛИШКОМ БОЛЬШОЕ ЧИСЛО")
        print(".................................")
        return 0
    except ValueError:
        print("..............................")
        print("!!! ОШИБКА: РАССЧЕТ НЕВОЗМОЖЕН")
        print("..............................")
        return 0

def change_of_sign(a):
    return -a
