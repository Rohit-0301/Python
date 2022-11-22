import numpy as np
print("Enter elements of matrix A :-")
A=np.zeros((3,3),dtype=np.int64)
for i in range(3):
    for j in range(3):
        A[i][j]=eval(input("Enter A["+f'{i}'+"]["+f'{j}'+"] :"))

print("\nEnter elements of matrix B :-")
B=[]
for i in range(3):
    m=[]
    for j in range(3):
        m.append(eval(input("Enter B["+f'{i}'+"]["+f'{j}'+"] :")))
    B.append(m)
B=np.array(B)

print("\nArray A :-\n",A)
print("\nArray B :-\n",B)