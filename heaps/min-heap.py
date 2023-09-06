from cmath import log
import random

class Heap:
  def __init__(self, value):
    self.heap=[value]

  def __str__(self):
    return str(self.heap)

  def _left_child(self, index):
    return (2 * index) + 1
  
  def _right_child(self, index):
    return (2 * index) + 2

  def _parent(self, index):
    return (index - 1) // 2

  def _swap_index(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

  def _sink_down(self, index):
    while True:
      min_value = index
      left=self._left_child(index)
      right=self._right_child(index)
      if left < len(self.heap) and self.heap[index] > self.heap[left]:
        min_value=left
      if right < len(self.heap) and self.heap[index] > self.heap[right]:
        min_value=right
      if min_value == index:
        return
      self._swap_index(min_value, index)
      index=min_value

  def insert(self, value):
    self.heap.append(value)
    current = len(self.heap)-1
    while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
      self._swap_index(current, self._parent(current))
      current = self._parent(current)


  def remove(self):
    if len(self.heap) == 0:
      return

    if len(self.heap) == 1:
      return self.heap.pop()

    min_value=self.heap[0]
    self.heap[0]=self.heap.pop()
    self._sink_down(0)
    return min_value

    

print('Create min heap')
my_heap = Heap(20)
print(f'my_heap: { my_heap }')

print('\nInsert Into Heap')
for i in range(3):
  num=int(round(random.random() * 100 + 8, 0))
  search_num_true = num
  my_heap.insert(num)
my_heap.insert(5)
print(f'my_heap: { my_heap }')

print('\nRemove item from heap')
print(f'item removed: {my_heap.remove()}')
print(my_heap)
