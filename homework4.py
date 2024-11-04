#დავალება N4

class LoggingMeta(type):
    def __new__(cls, name, bases, dct):
        methods = [key for key, value in dct.items() if callable(value)]
        
        print(f"Creating class: {name}")
        print(f"Methods: {methods}")
        
        return super().__new__(cls, name, bases, dct)

class ExampleClass(metaclass=LoggingMeta):
    def method1(self):
        pass
    
    def method2(self):
        pass

    def method3(self):
        pass

example = ExampleClass()
