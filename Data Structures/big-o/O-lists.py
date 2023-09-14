# O(1)
array = [11, 564, 21, 1, 5].append(17)
array.pop()

# O(n)
array.pop(0)
array.insert(0, 11)

# O(n)
array.insert(1, 45)

# O(n)
array.index(21)

# O(1)
array[3]