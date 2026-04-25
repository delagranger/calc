def get_operation_and_operands(last_result):
    print("""
          Возможные операции
          ------------------
          1) Базовые: +, -, *, /
          2) Продвинутые: ^, sqrt, %, //
          3) Операции над одним числом: abs, !, +-

Введите ENTER в качестве первого числа, чтобы продолжить работу над предыдущим числом.
    Впишите ВЫХОД, чтобы выйти из режима рассчета.
          """)

    a = input("Введите первое число: ").lower()
    if a == "":
        a = last_result
    elif a == "выход":
        return "выход", None, None
    else:
        try:
            a = float(a)
        except ValueError:
            print("!!! ОШИБКА: НЕКОРРЕКТНЫЕ ДАННЫЕ")
            print("    Повторите ввод.")
            return None, None, None

    op = input("Введите операцию: ")
    if op in ["abs", "!", "+-"]:
        return a, op, None
    elif op not in ["+", "-", "*", "/", '^', 'sqrt', '%', '//', 'abs', '!', '+-']:
        print("!!! ОШИБКА: НЕКОРРЕКТНАЯ ОПЕРАЦИЯ")
        print("    Повторите ввод.")
        return None, None, None
    
    try:
        b = float(input("Введите второе число: "))
    except ValueError:
        print("!!! ОШИБКА: НЕКОРРЕКТНЫЕ ДАННЫЕ")
        print("    Повторите ввод.")
        return None, None, None
    
    return a, op, b

def get_command():
    answer = input("Впишите команду (или HELP для просмотра команд): ").lower()
    if not answer in ["help", "посчитать", "история", "выход"]:
        print("!!! ОШИБКА: НЕИЗВЕСТНАЯ КОМАНДА")
        print("    Повторите ввод.")
    else:
        return answer
