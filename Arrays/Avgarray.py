def average_of_array():
    array = []
    N = int(input("Enter the number of elements: "))
    for i in range(N):
        value = int(input("Enter a value: "))
        array.append(value)
    if len(array) == 0:
        return 0
    average = sum(array) / len(array)
    return average
result = average_of_array()
print("The average of the array is: ", result)