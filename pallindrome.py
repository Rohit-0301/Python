str=input("Enter a string : ")
i=0
j=len(str)-1
f=0 
while(i<len(str)/2):
    if(str[i]!=str[j]):
        f=1
        break
    i+=1
    j-=1
if(f==0):
    print(str," is pallindrome.")
else:
    print(str," is not pallindrome.")

s1=str[::-1]
s2=str.lower()
s3=str.upper()
s4=str.capitalize()
s5=str.split('a')
s6=str.count('a')
s7=str.title()
print("Reverse of ",str," is ",s1)
print("LowerCase of ",str," is ",s2)
print("UpperCase of ",str," is ",s3)
print("Capitalise of ",str," is ",s4)
print("Split of ",str," by 'a' is ",s5)
print("Number of 'a' in ",str," is ",s6)
print("Title case of ",str," is ",s7)