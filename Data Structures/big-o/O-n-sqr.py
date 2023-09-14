def print_items(n):
  for i in range(n):
    for j in range(n):
      print(f'{i}: {j}')

  # n * n times
  # O(n)^2

  for k in range(n):
    print(k)



# simplify
# drop Non dominants
# O(n^2) + O(n)
# O([n^2 ]+ n) -> n is insignifigant
# O(n^2)


print_items(4)