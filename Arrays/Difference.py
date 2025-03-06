def difference_max_min(arr):
    if not arr:
        return None
    return max(arr) - min(arr)
numbers = [10, 20, 5, 40, 50]
difference = difference_max_min(numbers)
print("Difference between largest and smallest value:", difference)