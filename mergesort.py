from typing import List

def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:] + right[j:]

    return result

def mergeSort(A: List[int]) -> List[int]:
    if len(A) <= 1: return A

    mid = len(A) // 2
    left = mergeSort(A[:mid])
    right = mergeSort(A[mid:])

    return merge(left, right)

A = [1, 35, 6, 734, 98, 1, 2, 1254, 66, 125, 78, 12, 32, 6, 9, 8, 4, 9, 9, 1571, 0]
print(mergeSort(A))