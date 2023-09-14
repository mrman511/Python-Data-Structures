def print_items(a, b):
  for i in range(a):
    print(i)
    # runs O(n) times

  for j in range(b):
    print(j)

  # non O(n) because we are using more than one parameter
  # O(a+b) is the correct answer


  for i in range(a):
    for j in range(b):
      print(f'{i}, {j}')

    # runs O(ab) times
