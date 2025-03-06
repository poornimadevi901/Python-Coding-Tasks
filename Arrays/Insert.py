def insert_element(arr, value, position):
    arr.insert(position, value)
    return arr
numbers = [111, 210, 301, 450, 590]
element = int(input("Enter element to insert: "))
position = int(input("Enter position (index) to insert at: "))

updated_array = insert_element(numbers, element, position)
print("Updated array:", updated_array)