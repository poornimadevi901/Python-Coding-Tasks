def find_min_max(arr):
    if not arr:
        return None, None
    return min(arr), max(arr)
numbers = [90, 210, 55, 40, 340]
minimum, maximum = find_min_max(numbers)
print("Minimum value:", minimum)
print("Maximum value:", maximum)