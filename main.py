from ui.input_handler import GetOpAndNums, GetAnswer
from ui.greeting import greeting
from ui.farewell import farewell

from operations.math_core import Addition, Subtraction, Multiplication, Division

from history.history import ShowHistory

greeting()
result = 0
last_result = 0

while True:
    answer = GetAnswer()
    if answer == "Посчитать":
        a, op, b = GetOpAndNums()

        match op:
            case '+':
                result = Addition(a, b)
            case '-':
                result = Subtraction(a, b)
            case '*':
                result = Multiplication(a, b)
            case '/':
                result = Division(a, b)
                
        print(result)
        last_result, result = result, 0
    elif answer == "История":
        ShowHistory()
    elif answer == "Выход":
        farewell()
        break
