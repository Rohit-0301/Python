sp=set()
for i in range(2,20):
    f=0
    j=2
    while(j<=(i**(1/2))):
        if(i%j==0):
            f=1
            break
        j+=1
    if(f==0):
        sp.add(i)
print("Prime numbers upto 20 ==> ",sp)

sn=set()
for i in range(1,21):
    sn.add(i)
print("Natural numbers upto 20 ==> ",sn)
print("sn-sp ==> ",sn-sp)
print("sp-sn ==> ",sp-sn)
print("Union ==> ",sn|sp)
print("Intersection ==> ",sn&sp)