import numpy as np

L=[1,8,8,9,7,6,6,0,7,4,3,2,7]
A=np.array(L)
print("Array ==> ",A)

l1=L[::-1]
print("Reversal using slicing ==> ",l1)

l2=np.flipud(L)
print("Reversal using flipud ==> ",l2)

print("Length of array = ",len(A))

A.sort()
print("Sorted array in ascending order ==> ",A)

s=set(A)
l3=list(s)
print()
for i in l3:
    print("No of ",i," in array = ",L.count(i))