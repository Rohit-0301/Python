import numpy as np
print("Enter elements of matrix A :-")
A=[]
for i in range(3):
    m=[]
    for j in range(3):
        m.append(eval(input()))
    m=np.array(m)
    A.append(m)
A=np.array(A)

print("Enter elements of matrix B :-")
B=[]
for i in range(3):
    m=[]
    for j in range(3):
        m.append(eval(input()))
    m=np.array(m)
    B.append(m)
B=np.array(B)

print("\nArray A :-\n",A)
print("\nArray B :-\n",B)

Sum=np.add(A,B)
print("\nSum:-\n",Sum)

Difference=np.subtract(B,A)
print("\nDifference:-\n",Difference)

divide=np.divide(A,B)
print("\nDivision:-\n",divide)

print("\nMultiplication using loop:-")
Mul=[]
for i in range(3):
    m=[]
    for j in range(3):
        x=0
        for k in range(3):
            x+=A[i][k]*B[k][j]
        m.append(x)
    m=np.array(m)
    Mul.append(m)
print(np.array(Mul))

Product=np.dot(A,B)
print("\nProduct:-\n",Product)
print("\nProduct:-\n",A@B)

print("\nRank of A = ",np.linalg.matrix_rank(A))
print("Rank of B = ",np.linalg.matrix_rank(B))

A=A.transpose()
print("\nTranspose of A:-\n",A)
B=B.transpose()
print("\nTranspose of B:-\n",B)