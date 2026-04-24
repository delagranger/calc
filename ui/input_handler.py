def get_operation_and_operands(last_result):
    print("""
          Возможные операции: +, -, *, /
Введите Enter в качестве первого числа, чтобы продолжить работу над предыдущим числом
          """)

    a = input("Введите первое число: ")
    if a == "":
        a = last_result
    else:
        a = float(a)
    op = input("Введите операцию: ")
    b = float(input("Введите второе число: "))
    
    return a, op, b

def get_command():
    answer = input("Впишите команду (или help для просмотра команд): ")
    return answer
