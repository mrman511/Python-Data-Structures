num1 = 11

num2 = num1

print("Before num2 is Updated")
print(f"num1: { num1 }")
print(f"num2: {num2}")
# nums point to same address
print(f"num1 points to: {id(num1)}")
print(f"num2 points to: {id(num2)}")

# if you change either num it will point to a seperate id
print("\nBefore num2 num in Updated")
num2 = 6
print(f"num1: { num1 }")
print(f"num2: {num2}")

print(f"num1 points to: {id(num1)}")
print(f"num2 points to: {id(num2)}")

dict1 = { 'value': 11 }
dict2 = dict1
print('\n check dicts')
print(f"dict1: { dict1['value'] }")
print(f"dict2: { dict2['value'] }")
print(f"dict1 points to: {id(dict1)}")
print(f"dict2 points to: {id(dict2)}")

print('\n change dict2 value')
dict2['value']= 22
print(f"dict1: { dict1['value'] }")
print(f"dict2: { dict2['value'] }")
print(f"dict1 points to: {id(dict1)}")
print(f"dict2 points to: {id(dict2)}")