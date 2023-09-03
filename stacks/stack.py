class Node:
  def __init__(self, value):
    self.value=value
    self.next=None

  def __str__(self):
    return str(self.value)
  
class Stack:
  def __init__(self,value):
      new_node=Node(value)
      self.top=new_node
      self.length=1
    
  def __str__(self):
    temp = self.top
    str = f'[{temp.value}]'
    while temp.next:
      str += f'\n[{temp.next.value}]'
      temp=temp.next
    return str

  def push(self, value):
    new_node=Node(value)
    new_node.next=self.top
    self.top=new_node
    self.length+=1

  def pop(self):
    prev=self.top
    self.top=prev.next
    prev.next=None
    self.length-=1
    return prev


print('\ncreate doubly linked list')
my_stack=Stack(12)
print(my_stack)

print('\nPush')
my_stack.push(655)
my_stack.push(5)
my_stack.push(38)
print(my_stack)

print('\nPop')
removed=my_stack.pop()
print(my_stack)
print(f'removed: {removed}')