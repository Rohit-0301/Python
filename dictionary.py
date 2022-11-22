D={}
Sum={}
Name=['A','B','C','D','E']
Marks=[[20,25,30],[18,29,30],[20,27,38],[5,28,30],[21,2,30]]
marks=[]
for i in range(0,len(Name)):
    sum=0
    for j in range(0,3):
        sum+=Marks[i][j]
    marks.append(sum)
    Sum.update({Name[i]:sum})
    D.update({Name[i]:Marks[i]})
print(D)
print(Sum)

# for i in range(len(Name)-1):
#     f=0
#     for j in range(len(Name)-1):
#         if(marks[j]<marks[j+1]):
#             f=1
#             t1=Name[j]
#             t2=marks[j]
#             Name[j]=Name[j+1]
#             marks[j]=marks[j+1]
#             Name[j+1]=t1
#             marks[j+1]=t2
#     if(f==0):
#         break
# Sorted={}
# for i in range(len(Name)):
#     Sorted.update({Name[i]:marks[i]})
# print(Sorted)

s=sorted(Sum.items(),key=lambda kv: kv[1],reverse=True)
S=dict(s)
print(S)
