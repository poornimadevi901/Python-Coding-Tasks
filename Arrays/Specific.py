def contains_value(arr, value):
    return value in arr
numbers = [10, 20, 30, 40, 50]
element = int(input("Enter element to check: "))
if contains_value(numbers, element):
    print("Element exists in the array.")
else:
    print("Element not found.")