import random
rand_list = [int(round(random.random() * 100 + 1, 0)) for i in range(10)]

def bubble_sort(my_list):
  sort_length=len(my_list)
  while sort_length > 0:
    for i in range(sort_length-1):
      if my_list[i]>my_list[i+1]:
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    sort_length -= 1
  return my_list

print(rand_list)
print(bubble_sort(rand_list))