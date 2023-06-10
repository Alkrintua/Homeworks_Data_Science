#Перевірка кількості ядер
import os

if __name__ == "__main__":
    cpu = os.cpu_count()
    print(f"Ваш процесор має {cpu} ядер")

#Обчислення квадратного кореня по циклу
import multiprocessing
import time
import math

def calculate_square_root(num):
    return math.sqrt(num)

def main():
    # Кількість потоків
    num_threads = 3
    pool = multiprocessing.Pool(processes=num_threads)

    sequence = range(1, 101)

    start_time = time.time()
    results = pool.map(calculate_square_root, sequence)
    end_time = time.time()

    print("Results:", results)
    print("Time taken:", end_time - start_time, "seconds")

if __name__ == '__main__':
    main()

num_attempts = 10
total_time = 0

for _ in range(num_attempts):
    start_time = time.time()
    if __name__ == '__main__':
        main()
    end_time = time.time()

    total_time += end_time - start_time

average_time = total_time / num_attempts
print("Average Time taken:", average_time, "seconds")
print("Total time taken", total_time)