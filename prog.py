from utils.get_data import GetData
from utils.operations import Addition, Subtraction, Multiplication, Division

a, op, b = GetData()

match op:
    case '+':
        res = Addition(a, b)
    case '-':
        res = Subtraction(a, b)
    case '*':
        res = Multiplication(a, b)
    case '/':
        res = Division(a, b)

print(res)



