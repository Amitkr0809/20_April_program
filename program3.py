# Add List Items

list1 = ["apple", "banana", "cherry"]
list1.append("orange")
print(list1)

list2 = ["apple", "banana", "cherry"]
list2.insert(1, "orange")
print(list2)

list3 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
list3.extend(tropical)
print(list3)

list4 = ['1','2','3']
tuple = ("kiwi", "orange")
list4.extend(tuple)
print(list4)
