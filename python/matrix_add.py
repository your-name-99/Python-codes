m=int(input("enter rows"))
n=int(input("enter colomn"))
l1=[]
l2=[]
l3=[]
for i in range(m):
    l1.append([0]*n)
for i in range(m):
    l2.append([0]*n)
for i in range(m):
    l3.append([0]*n)
print("enter value for matrix 1")
for i in range(m):
    for j in range(n):
        l1[i][j]=int(input("enter the value"))
print("enter value for second matrix")
for i in range(m):
    for j in range(n):
        l2[i][j]=int(input("enter the value"))
                     
for i in range(m):
    for j in range(n):
        l3[i][j]=l2[i][j]+l1[i][j]
for i in range(m):
    print(l3[i])
