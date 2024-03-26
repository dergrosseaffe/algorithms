
def right(i):
    return 2 * i + 2


def left(i):
    return 2 * i + 1


def parent(i):
    return (i - 1) // 2


def sift_down(heap, i, size=None):
    max_index, l, r = i, left(i), right(i)
    size = len(heap) if size is None else size

    if l < size and heap[l] > heap[max_index]:
        max_index = l

    if r < size and heap[r] > heap[max_index]:
        max_index = r

    if i != max_index:
        heap[i], heap[max_index] = heap[max_index], heap[i]
        sift_down(heap, max_index, size)


def pop(heap):
    heap[0], heap[-1] = heap[-1], heap[0]
    max_value = heap.pop()
    sift_down(heap, 0)
    return max_value


def heapify(nums, start_index=0):
    for i in range(len(nums)//2, start_index - 1, -1):
        sift_down(nums, i)


def heapsort(heap):
    heapify(heap, 0)
    for i in range(len(heap) - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift_down(heap, 0, i)


nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
heapify(nums)
print("Heapified:", nums)
print("Pop:", pop(nums))
print("Pop:", pop(nums))
print("Pop:", pop(nums))
print("Pop:", pop(nums))
print("After 4 pops:", nums)

nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
heapsort(nums)
print("Sorted:", nums)