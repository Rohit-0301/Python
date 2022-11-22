s=input()
a={}
for i in s:
    if(i not in a):
        a[i]=0
    a[i]+=1
for i in a:
    print("No. of ",i," = ",a[i])