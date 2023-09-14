# How it works simplified

head = {
  "value": 11,
  "next": {

    "value": 33,
    "next": {

      "value": 24,
      "next": {

        "value": 8,
        "next": None
      }
    }
  }
}

print(head["next"]["next"]['value'])

# comparative linked list syntax
# print(my_linked_list.next.next.value)