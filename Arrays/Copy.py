def copy_array(arr):
    return arr[:]
original_array = [100, 200, 300, 400, 500]
copied_array = copy_array(original_array)
print("Original array:", original_array)
print("Copied array:", copied_array)