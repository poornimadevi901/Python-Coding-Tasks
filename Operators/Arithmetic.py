def arithmetic_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Division by zero is undefined"
    print("Addition: ", addition)
    print("Subtraction: ", subtraction)
    print("Multiplication: ", multiplication)
    print("Division: ", division)
arithmetic_operations(25, 14)
