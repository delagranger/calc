BASE_OPERATIONS = ["+", "-", "*", "/", '^', 'sqrt', '%', '//', 'abs', '!', '+-']
UNAR_OPERATIONS = ["abs", "!", "+-"]
COMMANDS = ["help", "посчитать", "история", "выход"]

def get_operation_and_operands(last_result):
    print("""
          Возможные операции
          ------------------
          1) Базовые: +, -, *, /
          2) Продвинутые: ^, sqrt, %, //
          3) Унарные: abs, !, +-
          ------------------
Введите ENTER в качестве первого числа, чтобы продолжить работу над предыдущим числом.
    Впишите ВЫХОД, чтобы выйти из режима рассчета.
          """)

    a = input("Введите первое число: ").lower()
    if not a:
        a = last_result
    elif a == "выход":
        return "выход", None, None
    else:
        try:
            a = float(a)
        except ValueError:
            print(".................................")
            print("!!! ОШИБКА: НЕКОРРЕКТНЫЕ ДАННЫЕ")
            print("    Повторите ввод.")
            print(".................................")
            return None, None, None

    op = input("Введите операцию: ")
    if op in UNAR_OPERATIONS:
        return a, op, None
    elif op not in BASE_OPERATIONS:
        print(".................................")
        print("!!! ОШИБКА: НЕКОРРЕКТНАЯ ОПЕРАЦИЯ")
        print("    Повторите ввод.")
        print(".................................")
        return None, None, None
    
    try:
        b = float(input("Введите второе число: "))
    except ValueError:
        print(".................................")
        print("!!! ОШИБКА: НЕКОРРЕКТНЫЕ ДАННЫЕ")
        print("    Повторите ввод.")
        print(".................................")
        return None, None, None
    
    return a, op, b


def get_command():
    answer = input("Впишите команду (или HELP для просмотра команд): ").lower()
    if answer not in COMMANDS:
        print(".................................")
        print("!!! ОШИБКА: НЕИЗВЕСТНАЯ КОМАНДА")
        print("    Повторите ввод.")
        print(".................................")
    else:
        return answer

