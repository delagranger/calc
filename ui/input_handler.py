def get_operation_and_operands(last_result):
    print("""
          Возможные операции
          ------------------
          1) Базовые: +, -, *, /
          2) Продвинутые: ^, sqrt, %, //
          3) Операции над одним числом: abs, !, +-

Введите Enter в качестве первого числа, чтобы продолжить работу над предыдущим числом
          """)

    a = input("Введите первое число: ")
    if a == "":
        a = last_result
    else:
        a = float(a)

    op = input("Введите операцию: ")
    if op in ["abs", "!", "+-"]:
        return a, op, 0
    
    b = float(input("Введите второе число: "))
    
    return a, op, b

def get_command():
    answer = input("Впишите команду (или help для просмотра команд): ")
    return answer
