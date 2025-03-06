def second_largest(arr):
    if len(arr) < 2:
        return "Array should have at least two elements"
    first, second = float('-inf'), float('-inf')
    for num in arr:
        if num > first:
            second, first = first, num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else "No second largest number"
arr = [10, 20, 5, 8, 15]
print(second_largest(arr))