#დავალება N3

import time

def time_calculator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Execution time: {duration:.6f} seconds")
        return result
    return wrapper

@time_calculator
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

example_function(1000000)
