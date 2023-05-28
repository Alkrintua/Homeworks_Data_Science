# function got number of months and returns names
import sys
def month_name(num):
    try:
        if not str(num).isdigit():
            raise ValueError("Змінна має містити число")
        elif num not in range(1, 13) and num not in str(list(range(1, 13))):
            raise ValueError("Змінна має бути числом від 1 до 12")
        month_names = {1: "Січень", 2: "Лютий", 3: "Березень", 4: "Квітень", \
         5: "Травень", 6: "Червень", 7: "Липень", 8: "Серпень", 9: "Вересень", \
        10: "Жовтень", 11: "Листопад", 12: "Грудень"}
        return (month_names[int(num)])
    except ValueError as er:
        print(f"Помилка: {str(er)}", file=sys.stderr)
        return 0

# Приклади виклику функції
# print(month_name("99"))
# print(month_name("12"))
# print(month_name(9))
# print(month_name("рядок"))

# перевірка списку чисел на унікальність
def unique_numbers(lst):
    try:
        if not lst:
            raise ValueError("Список чисел порожній")
        for el in lst:
            if not str(el).isdigit():
                raise ValueError("Список має містити лише числа")
        else:
            if len(lst) != len(set(lst)):
                raise ValueError("У списку є повторювані числа")
    except ValueError as er:
        print(f"Помилка: {str(er)}", file=sys.stderr)
        return 0
    else:
        return "Список чисел унікальний"

# Приклади виклику функції
# print(unique_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(unique_numbers([0, 2, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(unique_numbers([0, "1", 2, 3, 4, 5, 6, 7, 8, 9]))
# print(unique_numbers([0, "Один", 2, 3, 4, 5, 6, 7, 8, 9]))

# Напишіть користувацький клас виключення
class UserException(Exception):
    def __init__(self, parameter):
        self.parameter = parameter

    def __str__(self):
        return f"UserException: {self.parameter}"

def div_numb(a, b):
    try:
        if b == 0:
            raise UserException("Ділення на нуль неможливе")
        return a / b
    except UserException as e:
        print(e)
        return 0

# Приклади виклику функції
# print(div_numb(15, 0))
# print(div_numb(15, 3))
