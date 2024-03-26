
def right(i):
    return 2 * i + 2


def left(i):
    return 2 * i + 1


def parent(i):
    return (i - 1) // 2


def sift_down(heap, i, size=None):
    min_index, l, r = i, left(i), right(i)
    size = len(heap) if size is None else size

    if l < size and heap[l] < heap[min_index]:
        min_index = l

    if r < size and heap[r] < heap[min_index]:
        min_index = r

    if i != min_index:
        heap[i], heap[min_index] = heap[min_index], heap[i]
        sift_down(heap, min_index, size)


def sift_up(heap, i):
    while i > 0 and heap[parent(i)] > heap[i]:
        heap[parent(i)], heap[i] = heap[i], heap[parent(i)]
        i = parent(i)


def pop(heap):
    heap[0], heap[-1] = heap[-1], heap[0]
    max_value = heap.pop()
    sift_down(heap, 0)
    return max_value


def heapify(nums, start_index=0):
    for i in range(len(nums)//2, start_index - 1, -1):
        sift_down(nums, i)


def heapsort(heap):
    heapify(heap)
    for i in range(len(heap) - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift_down(heap, 0, i)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
heapsort(nums)
print("Sorted:", nums)