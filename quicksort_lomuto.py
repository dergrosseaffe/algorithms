def partition(list, left, right):
    pivot = list[right]
    i = left - 1

    for j in range(left, right):
        if list[j] <= pivot:
            i += 1
            list[i], list[j] = list[j], list[i]

    list[i + 1], list[right] = list[right], list[i + 1]
    return i + 1


def quicksort(list, left, right):
    if left >= right:
        return

    m = partition(list, left, right)

    quicksort(list, left, m - 1)
    quicksort(list, m + 1, right)


list_of_nums = [
    [1, 3, 5, 6, 8, 2, 3, 4, 0, 12, 14, 135],
    [3, 6, 8, 10, 1, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [4, 5, 5, 4, 3, 3, 1, 2, 2, 1],
    [1],
    [],
    [23, 45, 12, 9, 34, 95, 30, 11, 50, 31, 42, 55, 15, 8, 65, 105, 7, 90, 4, 60, 89, 3, 22, 44, 88],
    [-10, 7, -3, -2, 9, 5, -1, 3]
]

for nums in list_of_nums:
    quicksort(nums, 0, len(nums) - 1)
    print(nums)