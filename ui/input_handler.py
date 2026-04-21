def GetOpAndNums():
    print("Возможноные операции: +, -, *, /")

    a = float(input("Введите первое число: "))
    op = input("Введите операцию: ")
    b = float(input("Введите второе число: "))
    
    return a, op, b

def GetAnswer():
    answer = input("Впишите действие (Посчитать, История, Выход): ")
    return answer
