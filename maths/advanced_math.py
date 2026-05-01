from math import pow, factorial

def exponentiation(a, b):
    try:
        result = pow(a, b)
    except ValueError as e:
        print("..............................")
        print(f"!!! ОШИБКА: РАССЧЕТ НЕВОЗМОЖЕН ({e})")
        print("..............................")
    except (OverflowError, MemoryError) as e:
        print(".................................")
        print(f"!!! ОШИБКА: СЛИШКОМ БОЛЬШОЕ ЧИСЛО ({e})")
        print(".................................")
    else:
        return result


def square_root(a, b):
    try:
        result = pow(a, 1/b)
    except ValueError as e:
        print("..............................")
        print(f"!!! ОШИБКА: РАССЧЕТ НЕВОЗМОЖЕН ({e})")
        print("..............................")
    except ZeroDivisionError as e:
        print("...........................")
        print(f"!!! ОШИБКА: ДЕЛЕНИЕ НА НОЛЬ ({e})")
        print("...........................")
    except (OverflowError, MemoryError) as e:
        print(".................................")
        print(f"!!! ОШИБКА: СЛИШКОМ БОЛЬШОЕ ЧИСЛО ({e})")
        print(".................................")
    else:
        return result


def remainder_of_division(a, b):
    try:
        result = a % b
    except ZeroDivisionError as e:
        print("............................")
        print(f"!!! ОШИБКА: ДЕЛЕНИЕ НА НОЛЬ ({e})")
        print("............................")
    else:
        return result


def integer_division(a, b):
    try:
        result = a // b
    except ZeroDivisionError as e:
        print("............................")
        print(f"!!! ОШИБКА: ДЕЛЕНИЕ НА НОЛЬ ({e})")
        print("............................")
    else:
        return result


def modulus(a):
    return abs(a)


def fctr(a):
    try:
        result = factorial(int(a))
    except (OverflowError, MemoryError) as e:
        print(".................................")
        print(f"!!! ОШИБКА: СЛИШКОМ БОЛЬШОЕ ЧИСЛО ({e})")
        print(".................................")
    except ValueError as e:
        print("..............................")
        print(f"!!! ОШИБКА: РАССЧЕТ НЕВОЗМОЖЕН ({e})")
        print("..............................")
    else:
        return result

def change_of_sign(a):
    return -a
