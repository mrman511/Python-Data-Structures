import random

class Heap:
  def __init__(self, value):
    self.heap=[value]

  def __str__(self):
    return str(self.heap)

  def _left_child(self, index):
    return 2 * index + 1

  def _right_child(self, index):
    return 2 * index + 2

  def _parent(self, index):
    return (index - 1) // 2

  def _swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

  def _sink_down(self, index):
    max_index = index
    while True:
      left_index = self._left_child(index)
      right_index = self._right_child(index)

      if (left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]):
        max_index = left_index
      if ( right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]):
        max_index = right_index
      if max_index != index:
        self._swap(index, max_index)
        index=max_index
      else:
        return
        index=max_index

    # if self.heap[index] < self.heap[self._left_child(index)] or self.heap[index] < self.heap[self._right_child(index)]:
    #   if self.heap[self._left_child(index)] > self.heap[self._right_child(index)]:
    #     self._swap(index, self._left_child(index))
    #     return self._left_child(index)
    #   else:
    #     self._swap(self._right_child(index), index)
    #     return self._right_child(index)


  def remove(self):
    if len(self.heap) == 0:
      return None
    
    if len(self.heap) == 1:
      return self.heap.pop()
    
    max_value=self.heap[0]
    self.heap[0] = self.heap.pop()
    i=0
    self._sink_down(i)
    return max_value


  def insert(self, value):
    self.heap.append(value)
    current = len(self.heap)-1
    parent=self._parent(current)
    while current > 0 and self.heap[parent] < self.heap[current]:
      self._swap(current, parent)
      current=parent
      parent=self._parent(current)


    
      
print('Create max heap')
my_heap = Heap(20)
print(f'my_heap: { my_heap }')

print('\nInsert Into Heap')
for i in range(10):
  num=int(round(random.random() * 100 + 1, 0))
  search_num_true = num
  print(f'Inserting Number: [{num}]')
  my_heap.insert(num)
print(f'my_heap: { my_heap }')

print('\nRemove item from heap')
print(f'item removed: {my_heap.remove()}')
print(my_heap)
