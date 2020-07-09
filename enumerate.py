In [76]:
l1=[1,3,5,7,9,10,12]
l1=[x for (i,x) in enumerate(l1)if i not in (0,4,5)] 
print(l1)