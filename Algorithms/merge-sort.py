from cmath import log
import random

rand_list1 = [int(round(random.random() * 100 + 1, 0)) for i in range(6)]
rand_list2 = [int(round(random.random() * 100 + 1, 0)) for i in range(6)]

def insertion_sort(lst):
  for i in range(1, len(lst)):
    while lst[i] < lst[i-1] and i > 0:
      lst[i], lst[i-1] = lst[i-1], lst[i]
      i -= 1
  return lst

sorted_list1 = insertion_sort(rand_list1)
sorted_list2 = insertion_sort(rand_list2)

print(sorted_list1)
print(sorted_list2)

def merge_sort(lst1, lst2):
  long, short = (lst1, lst2) if len(lst1)>=len(lst2) else (lst2, lst1)
  lst=[]
  for i in range(len(long)):
    while len(short)>0 and long[0]>short[0]:
      lst.append(short.pop(0))
    lst.append(long.pop(0))
  lst+=short
  return lst

print(merge_sort(sorted_list1, sorted_list2))