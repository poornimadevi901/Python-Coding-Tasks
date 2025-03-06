def sum_of_array():
    array = []
    N = int(input("Enter the number of elements: "))
    for arr in range(N):
        value = int(input("Enter a value: "))
        array.append(value)
    total = sum(array)
    return total
result = sum_of_array()
print("The sum of the array is: ", result)
