class Node:
  def __init__(self, value):
    self.value=value
    self.next=None
    self.prev=None

  def __str__(self):
    return str(self.value)

  def __eq__(self, target):
      return self.value == target.value

class DoublyLinkedList:
  def __init__(self, value):
      new_node = Node(value)
      self.head = new_node
      self.tail = new_node
      self.length = 1

  def __str__(self):
    lst = []
    temp = self.head
    while temp:
      lst.append(temp.value)
      temp = temp.next
    return str(lst)

  def append(self, value):
    new_node=Node(value)
    tail=self.tail
    new_node.prev=tail
    tail.next=new_node
    self.tail=new_node
    self.length+=1

  def prepend(self, value):
    new_node=Node(value)
    temp=self.head
    temp.prev=new_node
    new_node.next=temp
    self.head=new_node
    self.length+=1

  def pop(self):
    new_tail=self.tail.prev
    old_tail=self.tail
    old_tail.prev=None
    new_tail.next=None
    self.tail=new_tail
    self.length-=1
    return old_tail

  def pop_first(self):
    new_head=self.head.next
    new_head.prev=None
    old_head=self.head
    self.head=new_head
    old_head.next=None
    self.length-=1
    return old_head

  def insert(self, index, value):
    if index <= 0:
      self.prepend(value)
    elif index >= self.length:
      self.append(value)
    else:
      new_node=Node(value)
      i=1
      temp=self.head.next 
      while i != index:
        temp=temp.next
        i+=1
      new_node.prev=temp.prev
      new_node.next=temp
      temp.prev.next=new_node
      temp.prev=new_node
      self.length+=1 

  def remove(self, index):
    if index <= 0:
      self.pop_first()
    elif index >= self.length:
      self.pop()
    else:
      i=1
      temp=self.head.next 
      while i != index:
        temp=temp.next
        i+=1
      prev=temp.prev
      next=temp.next
      prev.next=next
      next.prev=prev
      temp.prev=None
      temp.next=None
      self.length-=1 
      return temp

  def swap_first_last(self):
    head_next=self.head.next
    tail_prev=self.tail.prev
    new_head=self.tail
    new_tail=self.head
    new_head.next=head_next
    new_tail.prev=tail_prev
    self.tail.prev.next=new_tail
    self.head.next.prev=new_head
    new_head.prev=None
    new_tail.next=None
    self.head=new_head
    self.tail=new_tail

  def reverse(self):
    temp=self.head
    new_head=self.tail
    self.tail=temp
    self.head=new_head
    while temp:
      prev=temp.prev
      next=temp.next
      temp.prev=next
      temp.next=prev
      temp=next

  def is_palindrome(self):
    ignore_middle=True if self.length % 2 != 0 else False
    half_length=(self.length -1)/2 if ignore_middle else self.length/2
    i=1
    temp_start = self.head
    temp_end = self.tail
    while i < half_length:
      if temp_start != temp_end:
        return False
      temp_start = temp_start.next
      temp_end = temp_end.prev
      i+=1
    return True

     

print('\ncreate doubly linked list')
my_doubly=DoublyLinkedList(12)
print(my_doubly)

print('\nAppend doubly linked list')
my_doubly.append(23)
my_doubly.append(51)
my_doubly.append(6)
print(f'my_doubly.head.prev: {my_doubly.head.prev}, my_doubly.head.next: {my_doubly.head.next}')
print(f'my_doubly.tail.prev: {my_doubly.tail.prev}, my_doubly.tail.next: {my_doubly.tail.next}')
print(my_doubly)
print(f'length: {my_doubly.length}')

print('\nPrepend doubly linked list')
my_doubly.prepend(78)
my_doubly.prepend(118)
print(f'my_doubly.head.prev: {my_doubly.head.prev}, my_doubly.head.next: {my_doubly.head.next}')
print(f'my_doubly.tail.prev: {my_doubly.tail.prev}, my_doubly.tail.next: {my_doubly.tail.next}')
print(my_doubly)
print(f'length: {my_doubly.length}')

print('\nPop doubly linked list')
removed = my_doubly.pop()
print(f'my_doubly.head.prev: {my_doubly.head.prev}, my_doubly.head.next: {my_doubly.head.next}')
print(f'my_doubly.tail.prev: {my_doubly.tail.prev}, my_doubly.tail.next: {my_doubly.tail.next}')
print(f'removed: {removed}')
print(my_doubly)
print(f'length: {my_doubly.length}')

print('\n Pop First doubly linked list')
removed = my_doubly.pop_first()
print(f'my_doubly.head.prev: {my_doubly.head.prev}, my_doubly.head.next: {my_doubly.head.next}')
print(f'my_doubly.tail.prev: {my_doubly.tail.prev}, my_doubly.tail.next: {my_doubly.tail.next}')
print(f'removed: {removed}')
print(my_doubly)
print(f'length: {my_doubly.length}')

print('\ninsert into doubly linked list')
removed = my_doubly.insert(2, 17)
print(f'my_doubly.head.prev: {my_doubly.head.prev}, my_doubly.head.next: {my_doubly.head.next}')
print(f'my_doubly.tail.prev: {my_doubly.tail.prev}, my_doubly.tail.next: {my_doubly.tail.next}')
print(my_doubly)
print(f'length: {my_doubly.length}')

print('\nremove index doubly linked list')
removed = my_doubly.remove(3)
print(f'my_doubly.head.prev: {my_doubly.head.prev}, my_doubly.head.next: {my_doubly.head.next}')
print(f'my_doubly.tail.prev: {my_doubly.tail.prev}, my_doubly.tail.next: {my_doubly.tail.next}')
print(my_doubly)
print(f'length: {my_doubly.length}')

print('\nswap first and last')
removed = my_doubly.swap_first_last()
print(f'my_doubly.head.prev: {my_doubly.head.prev}, my_doubly.head.next: {my_doubly.head.next}')
print(f'my_doubly.tail.prev: {my_doubly.tail.prev}, my_doubly.tail.next: {my_doubly.tail.next}')
print(my_doubly)
print(f'length: {my_doubly.length}')

print('\n reverse')
removed = my_doubly.reverse()
print(f'my_doubly.head.prev: {my_doubly.head.prev}, my_doubly.head.next: {my_doubly.head.next}')
print(f'my_doubly.tail.prev: {my_doubly.tail.prev}, my_doubly.tail.next: {my_doubly.tail.next}')
print(my_doubly)
print(f'length: {my_doubly.length}')

print('\nIs Palindrome')
palindrome = DoublyLinkedList(1)
palindrome.append(1)
palindrome.append(1)
palindrome.append(1)
palindrome.append(1)

print(f'my_doubly: {my_doubly}')
print(f'my_doubly.is_palindrome: {my_doubly.is_palindrome()}')
print(f'palindrome: {palindrome}')
print(f'palindrome.is_palindrome: {palindrome.is_palindrome()}')
