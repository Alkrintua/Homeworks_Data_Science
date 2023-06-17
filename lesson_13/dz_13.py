from random_word import RandomWords
import time
import random

w = RandomWords()

int_list = [random.randint(0, 1000) for _ in range(5000)]
float_list = [random.uniform(0.1, 100.0) for _ in range(5000)]
str_list = [w.get_random_word() for _ in range(5000)]


#bubble sort

def bubble_sort(lst):
    length = len(lst)
    for i in range(length):
        swapped = False
        for j in range(0, length - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
                swapped = True
        if not swapped:
            break
    return(lst)

cor_time = time.time()
print(bubble_sort(str_list))
print(f"Duration time: {time.time() - cor_time} sorting.")