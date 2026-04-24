from math import pow, factorial

def exponentiation(a, b):
    return pow(a, b)


def square_root(a, b):
    return pow(a, 1/b)


def remainder_of_division(a, b):
    return a % b


def integer_division(a, b):
    return a // b


def modulus(a):
    return abs(a)


def fctr(a):
    return factorial(int(a))


def change_of_sign(a):
    a -= a * 2
    return a

