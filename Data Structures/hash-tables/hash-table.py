class HashTable:
  def __init__(self, size=7):
    self.data_map = [None] * size
  
  def __hash(self, key):
    my_hash=0
    for letter in key:
      # ord(letter) returns the number of the ASCII letter
      # 23 is a prime number
      my_hash=((my_hash + ord(letter) * 23) % len(self.data_map))
    return my_hash

  def __str__(self):
    str = ''
    for i, val in enumerate(self.data_map):
      str+=f'\n{i}: {val}'
    return str

  def set_item(self, key, value):
    index=self.__hash(key)
    if self.data_map[index] == None:
      self.data_map[index]=[]
    self.data_map[index].append([key, value])

  def get_item(self, key):
    index=self.__hash(key)
    if self.data_map[index]:
      for pair in self.data_map[index]:
        if pair and key == pair[0]:
          return pair
    raise ValueError(f"[{key}] is not present within this hash table")

  def keys(self):
    lst=[]
    for index_arr in self.data_map:
      if index_arr:
        lst+=[pair[0] for pair in index_arr]
    return lst


my_hash_table=HashTable()
print('\nCreate hash table')
print(my_hash_table)

print('\nSet Item')
my_hash_table.set_item('Cookie', 5154)
my_hash_table.set_item('Chocolate', 51)
my_hash_table.set_item('Banana', 15)
my_hash_table.set_item('Chip', 84)
my_hash_table.set_item('Nail', 84)
my_hash_table.set_item('Cow', 84)
my_hash_table.set_item('Turbin', 84)
my_hash_table.set_item('Morrowind', 84)
print(my_hash_table)


print('\nGet Item')
print(my_hash_table.get_item('Cow'))
# print(my_hash_table.get_item('Apple'))

print('\nGet keys')
print(my_hash_table.keys())