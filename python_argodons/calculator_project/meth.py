class Meth():
    def sum(a, b):
        return a + b
    
    def subtraction(a, b):
        return a - b
    
    def division(a, b):
        return a / b
    
    def multiply(a, b):
        return a * b

    meth_functions={
        "sum": lambda a, b: a + b,
        "subtraction": lambda a, b: a - b,
        "division": lambda a, b: a / b,
        "multiply": lambda a, b: a * b
    }
    