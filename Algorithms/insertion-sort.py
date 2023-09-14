import random
rand_list = [int(round(random.random() * 100 + 1, 0)) for i in range(10)]

def insertion_sort(lst):
  for i in range(1, len(lst)):
    while lst[i] < lst[i-1] and i > 0:
      lst[i], lst[i-1] = lst[i-1], lst[i]
      i -= 1
  return lst

print(rand_list)
print(insertion_sort(rand_list))