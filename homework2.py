#დავალება N2

class PositiveCheck:
    def __init__(self, func):
        self.func = func

    def __call__(self, number):
        if number < 0:
            raise ValueError("The number must be positive")
        result = self.func(number)
        print(f"Result: {result}")
        return result

@PositiveCheck
def return_number(number):
    return number

# Test examples
try:
    return_number(5)
    return_number(-3)
except ValueError as e:
    print(e)
