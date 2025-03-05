def smaller_larger():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    if a < b:
        print("Smaller number: ", a)
    elif a > b:
        print("Smaller number: ", b)
    else:
        print("Both numbers are equal.")
    if a > b:
        print("Larger number: ", a)
    elif a < b:
        print("Larger number: ", b)
smaller_larger()