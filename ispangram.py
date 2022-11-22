s=input("Enter a string : ")
a='abcdefghijklmnopqrstuvwxyz'
f=1
for i in a:
    if(i not in s.lower()):
        f=0
        break
if(f==1):
    print(s," is pangram.")
else:
    print(s," is not pangram.")