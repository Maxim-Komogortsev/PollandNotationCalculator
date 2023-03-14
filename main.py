
continueCalc = True
rules = "Используйте только знаки ('+', '-', '/', '*'). Все операторы и операнды должны быть разделены пробелом."

OPERATIONS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2}


def check_priority(value: str) -> int:
    if value in PRIORITY.keys():
        return PRIORITY[value]
    return -1


def to_polska(expr: list):
    result = []
    stack = []
    for element in expr:
        if element not in '+-*/':
            result.append(element)
        else:
            last = None if not stack else stack[-1]
            while check_priority(last) >= check_priority(element):
                result.append(stack.pop())
                last = None if not stack else stack[-1]
            stack.append(element)
    for e in reversed(stack):
        result.append(e)
    return result


def count_polska(expr: list):
    result = []
    for element in expr:
        if element not in '+-*/':
            result.append(element)
        else:
            first = int(result.pop(-2))
            second = int(result.pop(-1))
            result.append(OPERATIONS[element](first, second))
    return result[0]


print(" " * 15 + "LINE CALC" + " " * 15)
print("-" * 38)
print(rules)
while continueCalc:
    print("Для выхода нажмите q")
    string = str(input("Ввод: "))

    if string == "q":
        continueCalc = False
    else:
        expression = string.split()
        print("Ответ: ", count_polska(to_polska(expression)))