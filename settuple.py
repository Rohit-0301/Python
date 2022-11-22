l=[2,9,8,7,2,6,8,2,6]
s=set(l)
t=tuple(l)

print("Set ==> ",s)
print("Tuple ==> ",t)

l1=list(s)
max=l1[0]
min=l1[0]
for i in range(1,len(l1)):
    if(l1[i]>max):
        max=l1[i]
    if(l1[i]<min):
        min=l1[i]

print("Max element in set = ",max)
print("Min element in set = ",min)

print("Deletion :-")
for i in range(0,len(s)):
    s.pop()
    print(s)