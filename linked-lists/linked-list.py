from cmath import log


class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self):
    return f'node value: { self.value }, next value: {self.next.value}'


class LinkedList:
  def __init__(self, value):
    new_node= Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

  def __str__(self) -> str:
    lst = []
    temp = self.head
    while temp is not None:
      lst.append(temp.value)
      temp = temp.next
    return str(lst)

  def append(self, value):
    node = Node(value)
    temp = self.head
    while temp.next is not None:
      temp = temp.next
    temp.next = node
    self.tail = node
    self.length += 1

  def prepend(self, value):
    node = Node(value)
    node.next = self.head
    self.head = node
    self.length += 1

  def insert(self, index, value):
    if index <= 0:
      self.prepend(value)
    elif index >= self.length:
      self.append(value)
    else:
      node = Node(value)
      i = 1
      temp = self.head
      while i != index:
        i+=1
        temp = temp.next
      node.next=temp.next
      temp.next=node
      self.length += 1

  def pop(self):
    temp = self.head
    while temp.next.next is not None:
      temp = temp.next
    temp.next = None
    self.tail = temp
    self.length -= 1

  def pop_first(self):
    self.head = self.head.next
    self.length -= 1

  def remove(self, index):
    if index <= 0:
      self.pop_first()
    elif index >= self.length:
      self.pop()
    else:
      i = 1
      temp = self.head
      while i != index:
        i+=1
        temp = temp.next
      temp.next=temp.next.next
      self.length -= 1

  def reverse(self):
    lst = []
    temp = self.head
    while temp is not None:
      lst.append(temp)
      temp = temp.next
    
    # print(f"here { }")
    self.head = lst.pop(-1)
    self.tail = lst.pop(0)
    self.tail.next = None
    temp = self.head
    while len(lst) > 0:
      temp.next = lst.pop(-1)
      temp = temp.next
    temp.next=self.tail




print('create list with one value')
my_linked_list = LinkedList(4)
print(my_linked_list)

print('\nappend list')
my_linked_list.append(32)
my_linked_list.append(31)
my_linked_list.append(2)
my_linked_list.append(17)
print(my_linked_list)

print('\nprepend list')
my_linked_list.prepend(73)
print(my_linked_list)

print('\ninsert into list')
my_linked_list.insert(2, 5)
print(my_linked_list)

print('\nremove last item from list')
my_linked_list.pop()
print(my_linked_list)

print('\nremove first item from list')
my_linked_list.pop_first()
print(my_linked_list)

print('\nremove item from list at index')
my_linked_list.remove(2)
print(my_linked_list)

print('\nreverse list')
my_linked_list.reverse()
print(my_linked_list)