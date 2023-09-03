class Node:
  def __init__(self, value):
    self.value=value
    self.next=None

  def __str__(self):
    return str(self.value)

class Queue:
  def __init__(self, value):
    new_node=Node(value)
    self.first=new_node
    self.last=new_node
    self.length=1

  def __str__(self):
    temp = self.first
    str = f'[{temp.value}]'
    while temp.next:
      str += f'\n[{temp.next.value}]'
      temp=temp.next
    return str

  def enqueue(self, value):
    new_node=Node(value)
    self.last.next=new_node
    self.last=new_node
    self.length+=1

  def dequeue(self):
    first=self.first
    self.first=first.next
    first.next=None
    self.length+=1
    return first

print('\nQueue')
my_queue=Queue(12)
print(my_queue)

print('\nEnqueue')
my_queue.enqueue(655)
my_queue.enqueue(5)
my_queue.enqueue(38)
print(my_queue)

print('\nDequeue')
removed=my_queue.dequeue()
print(my_queue)
print(f'removed: {removed}')