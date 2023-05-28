# Zero division error exception
import sys
def division_num(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("На нуль ділити не можна!", file=sys.stderr)
        return 0

# print(division_num(10, 0))

# Function of returning list element
def list_scrolling(list, num):
    try:
        return list[int(num)]
    except IndexError as e:
        print(f"{e}, в списку немає заданого індексу, оновіть запит і повторіть його", file=sys.stderr)
        return -1

# print(list_scrolling([0, 1, 2, 3, 4, 5], 6))

# угадай число з виключеннями
# from random import randint
# gen_int = randint(1, 100)
# # створюємо змінну-рахівницю спроб
# tries = 0
# # обмежуємо кількість спроб до 6 циклом while
# while tries < 6:
# # зберігаємо число в змінну, перевіряємо чи відповідає введене число заданому, зараховуємо використану спробу
#     tr = int(input("Спробуйте вгадати число від 1 до 100, ввівши його сюди:"))
#     if tr not in range(1, 100):
#         raise("Ви ввели число поза межами вибірки гри, спробуйте ще раз")
#     else:
#         tries += 1
#         if tr != gen_int:
#         # якщо користувач не вгадав, повідомляємо користувачеві, що число не вірне та менше чи більше воно від заданого
#             if tr > gen_int:
#                 print("На жаль, ви не вгадали. Ввелено більше число")
#             else:
#                 print("На жаль, ви не вгадали. Ввелено менше число")
# # якщо користувач вгадав, повідомляємо про перемогу та кількість використаних спроб
#         else:
#             print(f"Вітаємо, ви перемогли, використавши {tries} спроб!")
#             break
# # повідомляємо якщо користувач вичерпав свої спроби
# else:
#     print("На жаль, ви програли, використавши всі доступні спроби")

# площа трикутника
import math
def triangle_square(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise("Сторона трикутника не може бути <= 0")
    else:
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

print(triangle_square(0, 3, 3))
