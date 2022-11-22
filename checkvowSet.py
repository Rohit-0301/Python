Str="National Institute of Technology, Raipur"
c=0
for i in Str:
    if(i in {'a','e','i','o','u','A','E','I','O','U'}):
        c+=1
print("Number of vowels = ",c)
