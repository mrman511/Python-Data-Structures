def print_items(n):
  for i in range(n):
    print(i)
    # runs O(n) times

  for j in range(n):
    print(j)

  # runs O(2n) times
  # drop Constants
  # O(n)
print_items(4)

