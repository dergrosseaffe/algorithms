class MaxHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _sift_up(self):
        index = self.size - 1
        while index > 0:
            parent = self._parent(index)
            if self.data[index] > self.data[parent]:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def _sift_down(self):
        index = 0
        while index < self.size:
            left = self._left_child(index)
            right = self._right_child(index)
            max_index = index

            if left < self.size and self.data[max_index] < self.data[left]:
                max_index = left
            if right < self.size and self.data[max_index] < self.data[right]:
                max_index = right

            if max_index != index:
                self.data[max_index], self.data[index] = self.data[index], self.data[max_index]
                index = max_index
            else:
                break

    def push(self, value):
        if self.size == self.capacity:
            raise Exception('Queue is full')
        self.data[self.size] = value
        self.size += 1
        self._sift_up()

    def peek(self):
        if self.size == 0:
            raise Exception('Queue is empty')
        return self.data[0]

    def pop(self):
        if self.size == 0:
            raise Exception('Queue is empty')
        value = self.data[0]
        self.data[0] = self.data[self.size - 1]
        self.size -= 1
        self._sift_down()
        return value

    def __str__(self):
        return str(self.data[:self.size])


# tests
def test_priority_queue():
    pq = MaxHeap(10)
    pq.push(1)
    pq.push(2)
    pq.push(3)
    pq.push(4)
    pq.push(5)
    pq.push(6)
    pq.push(7)
    pq.push(8)
    pq.push(9)
    pq.push(10)
    assert pq.peek() == 10
    assert pq.pop() == 10
    assert pq.peek() == 9
    assert pq.pop() == 9
    assert pq.peek() == 8
    assert pq.pop() == 8
    assert pq.peek() == 7
    assert pq.pop() == 7
    assert pq.peek() == 6
    assert pq.pop() == 6
    assert pq.peek() == 5
    assert pq.pop() == 5
    assert pq.peek() == 4
    assert pq.pop() == 4
    assert pq.peek() == 3
    assert pq.pop() == 3
    assert pq.peek() == 2
    assert pq.pop() == 2
    assert pq.peek() == 1
    assert pq.pop() == 1
    assert pq.size == 0


test_priority_queue()
print('PriorityQueue tests pass')