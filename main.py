from ui.input_handler import GetOpAndNums, GetAnswer
from ui.starter import starter

from operations.math_core import Addition, Subtraction, Multiplication, Division

from history.history import ShowHistory

starter()
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
    elif answer == "История":
        ShowHistory()
    elif answer == "Выход":
        break
            



