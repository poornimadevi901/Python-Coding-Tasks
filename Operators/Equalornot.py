def numbers_equal():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num1 == num2:
        return "The numbers are equal."
    else:
        return "The numbers are not equal."
result = numbers_equal()
print(result)