n=eval(input("Enter no of Students : "))
roll=[]
name=[]
marks=[]
for i in range(n):
    roll.append(eval(input("Enter Roll no : ")))
    name.append(input("Enter name : "))
    marks.append(eval(input("Enter marks : ")))
Stu=[roll,name,marks]

for i in range(n-1):
    f=0
    for j in range(n-1):
        if(Stu[0][j]>Stu[0][j+1]):
            f=1
            Stu[0][j],Stu[0][j+1]=Stu[0][j+1],Stu[0][j]
            Stu[1][j],Stu[1][j+1]=Stu[1][j+1],Stu[1][j]
            Stu[2][j],Stu[2][j+1]=Stu[2][j+1],Stu[2][j]
    if(f==0):
        break

print(Stu)

c=eval(input("Enter roll whose details you want : "))
f=0
for i in range(n):
    if(Stu[0][i]==c):
        print("\nStudent Details:-")
        print("Roll = ",roll[i],"\nName = ",name[i],"\nMarks = ",marks[i])
        f=1
if(f==0):
    print("Record not found...")
