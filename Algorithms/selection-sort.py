import random
rand_list = [int(round(random.random() * 100 + 1, 0)) for i in range(100)]

def selection_sort(my_list):
  for i in range(len(my_list) - 1):
    min_val_index = i
    for j in range(i, len(my_list) - 1):
      if my_list[j] < my_list[min_val_index]:
        min_val_index = j
    my_list[i], my_list[min_val_index] = my_list[min_val_index], my_list[i]
  return my_list
print(selection_sort(rand_list))