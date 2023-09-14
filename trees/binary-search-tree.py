from cmath import log
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
    return self.value == other.value if is_instance else other

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




class BinarySearchTree:
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

  def min_value(self, current_node):
    while current_node.left is not None:
      current_node=current_node.left
    return current_node.value

  def insert(self, value):
    new_node=Node(value)
    current=self.start
    while current:
      if new_node < current:
        if current.left is None:
          current.left=new_node
          current=None
        else:
          current=current.left
      else: 
        if current.right is None:
          current.right=new_node
          current=None
        else:
          current=current.right

  def contains(self, value):
    current=self.start
    while current is not None:
      if current.value == value:
        return True
      if current.value>value:
        current=current.left
      else:
        current=current.right
    return False

  def __delete_node(self, current_node, value):
    if current_node == None:
      return None
    if value < current_node.value:
      current_node.left = self.__delete_node(current_node.left, value)
    if value > current_node.value:
      current_node.right = self.__delete_node(current_node.right, value)
    else:
      if current_node.right == None and current_node.left == None:
        return None
      elif current_node.left == None:
        current_node = current_node.right
      elif current_node.right == None:
        current_node = current_node.left
      else:
        sub_tree_min = self.min_value(current_node.right)
        current_node.value = sub_tree_min
        current_node.right = self.__delete_node(current_node.right, sub_tree_min)
    return current_node

  def delete_node(self, value):
    self.__delete_node(self.start, value)
    



print('Create Binary Search Tree')
my_binary_search_tree=BinarySearchTree(5)
print(my_binary_search_tree)

print('\nInsert into Binary Search Tree')
# instanciate number garaunteed to be in tree
search_num_true=0
for i in range(6):
  num=int(round(random.random() * 9 + 1, 0))
  search_num_true = num
  my_binary_search_tree.insert(num)
print(my_binary_search_tree)

print('\nDoes Binary Search Tree contain number')
search_num_false = -1
print('should return node')
print(f"my_binary_search_tree.contains({search_num_true}):{my_binary_search_tree.contains(search_num_true)}")
print('should return False')
print(f"my_binary_search_tree.contains({search_num_false}): {my_binary_search_tree.contains(search_num_false)}")

print('\nMin Value')
print('min from start')
print(my_binary_search_tree.min_value(my_binary_search_tree.start))
print('min from right')
print(my_binary_search_tree.min_value(my_binary_search_tree.start.right))

print('\nDelete Node')
print(my_binary_search_tree)
print("my_binary_search_tree.delete_node(8)")
print(my_binary_search_tree.delete_node(8))
print(my_binary_search_tree)