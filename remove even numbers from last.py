In [92]:
list = [11, 22, 33, 44, 55]
print("Original list:",list)
for i  in list:
    if(i%2 == 0):
      list.remove(i)
print("list after removing EVEN numbers:",list)