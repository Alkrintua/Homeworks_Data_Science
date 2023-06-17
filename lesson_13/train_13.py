# list of random words
from random_word import RandomWords
import time

word_list = []
w = RandomWords()

for i in range(0, 250):
    word_list.append(w.get_random_word())

print("Згенерований список з випадкових слів: ", word_list)


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

print(bubble_sort(word_list))
print(f"Duration time: {time.time() - cor_time}")

# quick sort
def partitions(nums, low, hight):
    pivot = nums[(low + hight) // 2]
    i = low - 1
    j = hight + 1

    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partitions(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)
    print("Sorted data:", nums)

cor_time= time.time()
quick_sort(word_list)
print(f"Duration time: {time.time() - cor_time}")