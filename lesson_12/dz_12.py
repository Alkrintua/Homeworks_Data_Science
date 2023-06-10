# 1 завдання факторіал
import concurrent.futures
import math
import time

def calc_factorial(num):
    return math.factorial(num)

def main():
    numbers = [5, 10, 15, 20, 25]

    # Використання ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor() as exec:
        start_time = time.time()
        results_thread = exec.map(calc_factorial, numbers)
        end_time = time.time()

    # Використання ProcessPoolExecutor
    with concurrent.futures.ProcessPoolExecutor() as ex:
        start_time_process = time.time()
        results_process = ex.map(calc_factorial, numbers)
        end_time_process = time.time()

    # Виведення результатів та порівняння швидкості обчислень
    print("Results using ThreadPoolExecutor:")
    for num, result in zip(numbers, results_thread):
        print(f"Factorial of {num}: {result}")

    print("Time taken using ThreadPoolExecutor:", end_time - start_time, "seconds")

    print("Results using ProcessPoolExecutor:")
    for num, result in zip(numbers, results_process):
        print(f"Factorial of {num}: {result}")

    print("Time taken using ProcessPoolExecutor:", end_time_process - start_time_process, "seconds")

    if end_time - start_time < end_time_process - start_time_process:
        print("ThreadPoolExecutor is faster.")
    else:
        print("ProcessPoolExecutor is faster.")

if __name__ == '__main__':
    main()

