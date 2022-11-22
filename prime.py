p=[]
for i in range (2,50):
    f=0
    j=2
    while(j<=(i**(1/2))):
        if(i%j==0):
            f=1
            break
        j+=1
    if(f==0):
        p.append(i)
print("Prime numbers less than 50 ==> ",p)

a=int(input("Enter the integer to be inserted : "))
i=int(input("Enter index : "))
p.insert(i,a)
print(a," inserted at pos ",5," ==> ",p)

p.remove(a)
print(a," is removed from list ==> ",p)

p.sort(reverse=True)
print("Sort in descending order ==> ",p)


p.pop()
print("List after pop operation ==> ",p)

p.reverse()
print("Reversal of list ==> ",p)

print("Largest number ==> ",p[len(p)-1])

print("Second Largest number ==> ",p[len(p)-2])

s='National Institute of Technology, Raipur'
c=0
for i in s.lower():
    if(i in ['a','e','i','o','u']):
        c+=1
print("Number of vowels in ",s," = ",c)