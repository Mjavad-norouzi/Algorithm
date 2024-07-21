def search_matrix(matrix, target):
    if not matrix:
        return False
    one_dimensional_array = []
    for row in matrix:
        one_dimensional_array.extend(row)
    return binary_search(one_dimensional_array, target)


def binary_search(arr, tp):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid]
        if mid_value == tp:
            return True
        elif mid_value < tp:
            left = mid + 1
        else:
            right = mid - 1
    return False


matrix = [
    [1, 3, 5],
    [7, 8, 10],
    [12, 15, 18]
]
target = 8

result = search_matrix(matrix, target)
print(result)
