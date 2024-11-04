#დავალება N1

def positive_check(func):
    def wrapper(number):
        if number < 0:
            raise ValueError("The number must be positive")
        result = func(number)
        print(f"Result: {result}")
        return result
    return wrapper

@positive_check
def return_number(number):
    return number

try:
    return_number(5)
    return_number(-3)
except ValueError as e:
    print(e)
