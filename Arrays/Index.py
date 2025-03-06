def find_index(arr, element):
    try:
        return arr.index(element)
    except ValueError:
        return -1
numbers = [10, 20, 30, 40, 50]
element = int(input("Enter element to find: "))
index = find_index(numbers, element)
if index != -1:
    print(f"Element found at index: {index}")
else:
    print("Element not found")