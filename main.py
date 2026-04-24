from history.history import show_history, update_history

from maths.math_core import addition, subtraction, multiplication, division
from maths.advanced_math import exponentiation, square_root, remainder_of_division, integer_division, modulus, fctr, change_of_sign

from ui.input_handler import get_operation_and_operands, get_command
from ui.output_handler import print_last_result, print_result, show_commands, greeting, farewell

from utils.validation import *

greeting()
show_commands()

result = 0
last_result = 0

while True:
    print_last_result(last_result)
    command = get_command()

    if command == "Посчитать":
        a, op, b = get_operation_and_operands(last_result)

        match op:
            case '+':
                result = addition(a, b)
            case '-':
                result = subtraction(a, b)
            case '*':
                result = multiplication(a, b)
            case '/':
                result = division(a, b)
            case '^':
                result = exponentiation(a, b)
            case 'sqrt':
                result = square_root(a, b)
            case '%':
                result = remainder_of_division(a, b)
            case '//':
                result = integer_division(a, b)
            case 'abs':
                result = modulus(a)
            case '!':
                result = fctr(a)
            case '+-':
                result = change_of_sign(a)
                
        print_result(result)

        expression = f"{a} {op} {b}"
        last_result, result = result, 0

        update_history(expression, last_result)
    elif command == "История":
        show_history()
    elif command == "Выход":
        farewell()
        break
    elif command == "help":
        show_commands()
