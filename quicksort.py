import random


class PartitionSchemes:
    @staticmethod
    def lomuto(list, left, right):
        pivot = list[right]
        i = left - 1

        for j in range(left, right):
            if list[j] <= pivot:
                i += 1
                list[i], list[j] = list[j], list[i]

        list[i + 1], list[right] = list[right], list[i + 1]
        return i + 1

    @staticmethod
    def randomized_lomuto(list, left, right):
        pivot_index = random.randint(left, right)
        list[right], list[pivot_index] = list[pivot_index], list[right]
        pivot = list[right]
        i = left - 1

        for j in range(left, right):
            if list[j] <= pivot:
                i += 1
                list[i], list[j] = list[j], list[i]

        list[i + 1], list[right] = list[right], list[i + 1]
        return i + 1


def quicksort(list, left, right, partition_scheme):
    if left >= right:
        return

    m = partition_scheme(list, left, right)

    quicksort(list, left, m - 1, partition_scheme)
    quicksort(list, m + 1, right, partition_scheme)


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

# adds random lists of 10_000 elements
for exponent in range(2, 8):
    max_element = 10 ** exponent
    random_list = [random.randint(-max_element, max_element) for _ in range(10000)]
    list_of_nums.append(random_list)

schemes = [PartitionSchemes.lomuto, PartitionSchemes.randomized_lomuto]

for nums in list_of_nums:
    for scheme in schemes:
        quicksort(nums, 0, len(nums) - 1, scheme)
        print(f"{scheme.__name__} > is sorted? {nums == sorted(nums)}: {nums}")
