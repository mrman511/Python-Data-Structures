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
    self.root=new_node

  def __str__(self):
    rows=[]
    row=[self.root]
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

  def insert(self, value):
    new_node=Node(value)
    current=self.root
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
    
  def breadth_first_search(self):
    current_node=self.root
    que=[]
    results=[]
    que.append(self.root)
    while len(que)>0:
      if current_node.left:
        que.append(current_node.left)
      if current_node.right:
        que.append(current_node.right)
      results.append(que.pop(0).value)
      if len(que)>0:
        current_node=que[0]
    return results






print('Create Binary Search Tree')
my_binary_search_tree=BinarySearchTree(50)
print(my_binary_search_tree)

print('\nInsert into Binary Search Tree')
# instanciate number garaunteed to be in tree
search_num_true=0
for i in range(6):
  num=int(round(random.random() * 100 + 1, 0))
  search_num_true = num
  my_binary_search_tree.insert(num)
print(my_binary_search_tree)

print('\nBreadth First Search')
print(my_binary_search_tree.breadth_first_search())
