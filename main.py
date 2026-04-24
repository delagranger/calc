from history.history import show_history, update_history

from operations.math_core import addition, subtraction, multiplication, division

from ui.input_handler import get_operation_and_operands, get_command
from ui.output_handler import print_last_result, print_result, show_commands, greeting, farewell

from utils.validation import *

greeting()
show_commands()

result = 0
last_result = 0

while True:
    print_last_result()
    command = get_command()

    if command == "Посчитать":
        a, op, b = get_operation_and_operands()

        match op:
            case '+':
                result = addition(a, b)
            case '-':
                result = subtraction(a, b)
            case '*':
                result = multiplication(a, b)
            case '/':
                result = division(a, b)
                
        print_result(result)

        last_result, result = result, 0
        
        update_history(last_result)
    elif command == "История":
        show_history()
    elif command == "Выход":
        farewell()
        break
    elif command == "help":
        show_commands()
