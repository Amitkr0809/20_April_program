# Access List Items

list = ["apple", "banana", "cherry"]
print(list[-1])

list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list1[2:5])

list2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list2[:4])

list3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list3[2:])

list4 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list4[-4:-1])

list5 = ["apple", "banana", "cherry"]
if "apple" in list5:
  print("Yes, 'apple' is in the fruits list")
