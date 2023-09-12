import random


class Node:
  def __init__(self, value):
    self.value=value
    self.left=None
    self.right=None

  def checkInstance(self, other):
    if not isinstance(other, Node):
      return False
    else:
      return True

  def __str__(self):
    return str(self.value)

  def __eq__(self, other):
    is_instance=self.checkInstance(other)
    return (self.value == other.value) if is_instance else False

  def __gt__(self, other):
    is_instance=self.checkInstance(other)
    return self.value > other.value if is_instance else other

  def __ge__(self, other):
    is_instance=self.checkInstance(other)
    return self.value >= other.value if is_instance else other

  def __lt__(self, other):
    is_instance=self.checkInstance(other)
    return self.value < other.value if is_instance else other

  def __le__(self, other):
    is_instance=self.checkInstance(other)
    return self.value <= other.value if is_instance else other




class RBST:
  def __init__(self, value):
    new_node=Node(value)
    self.start=new_node

  def __str__(self):
    rows=[]
    row=[self.start]
    string=''
    while row:
      next_row = []
      is_row=False 
      for node in row:
        if node:
          if node.left:
            is_row=True
            next_row.append(node.left)
          else:
            next_row.append(None)
          if node.right:
            is_row=True
            next_row.append(node.right)
          else:
            next_row.append(None)
        else:
            next_row.append(None)
            next_row.append(None)

      rows.append(row)
      row = next_row if is_row else is_row
    for row in rows:
      string+='\n'
      for node in row:
        string+=f'[{node}]'if node is not None else '[]'
    return string

  def insert(self, value, current_node='start'):
    if current_node == 'start':
      current_node = self.start
    if value > current_node.value:
      if current_node.right:
        return self.insert(value, current_node.right)
      current_node.right = Node(value)
      return True
    if current_node.left:
      return self.insert(value, current_node.left)
    current_node.left = Node(value)
    return True

  def contains(self, value, current_node='start'):
    if current_node == 'start':
      current_node = self.start
    if current_node:
      if current_node.value==value:
        return True
      if value > current_node.value:
        return self.contains(value, current_node.right)
      return self.contains(value, current_node.left)
    return False

  # def delete(self, value, current_node='start'):
  #   if current_node == 'start':
  #     current_node = self.start

    

print('Create Binary Search Tree')
my_rbst=RBST(5)
print(my_rbst)

print('\nInsert into Binary Search Tree')
# instanciate number garaunteed to be in tree
search_num_true=0
for i in range(18):
  num=int(round(random.random() * 80 + 1, 0))
  search_num_true = num
  print(f'Inserting Number: [{num}]')
  my_rbst.insert(num)
print(my_rbst)

print('\nDoes Binary Search Tree contain number')
search_num_false = -1
print('should return node')
print(f"my_binary_search_tree.contains({search_num_true}):{my_rbst.contains(search_num_true)}")
print('should return False')
print(f"my_binary_search_tree.contains({search_num_false}): {my_rbst.contains(search_num_false)}")