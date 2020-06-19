m=int(input("enter rows"))
n=int(input("enter colomn"))
mat1=[]
mat2=[]
mat3=[]
for i in range(m):
    mat1.append([0]*n)
for i in range(m):
    mat2.append([0]*n)
for i in range(m):
    mat3.append([0]*n)
print("enter value for matrix 1")
for i in range(m):
    for j in range(n):
        mat1[i][j]=int(input("enter the value"))
print("enter value for second matrix")
for i in range(m):
    for j in range(n):
        mat2[i][j]=int(input("enter the value"))
print("multiplied matrix is =========")

for i in range(m):
   for j in range(n):
       for k in range(n):
           mat3[i][j] += mat1[i][k] * mat2[k][j]
"""for r in mat3:
   print(r)"""
r=mat3
print(r)







"""        
for i in range(m):
    for i in range(n):
        for k in range(n):
            mat3[i][j]=mat3[i][j]+(mat2[i][j]*mat1[i][j])
print("multiplied matrix is")
for i in range(m):
    for j in range(n):
        print(mat3[i][j],end=" ")
    print(end="\n")
"""
