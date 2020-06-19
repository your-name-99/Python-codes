r=int(input("ENTER NUMBER OF ROWS"))
c=int(input("ENTER NUMBER OF COLOUMNS"))
matrix1=[]
matrix2=[]
matrix3=[]

for i in range(r):
    matrix1.append([0]*c)
for i in range(r):
    matrix2.append([0]*c)
for i in range(r):
    matrix3.append([0]*c)
    
print("ENTER VALUES OF FIRST MATRIX ROW WISE")
for i in range(r):
    for j in range(c):
        matrix1[i][j]=int(input())

print("ENTER VALUES OF SECOND MATRIX ROW WISE")
for i in range(r):
    for j in range(c):
        matrix2[i][j]=int(input())
for i in range(r):
    for j in range(c):
            matrix3[i][j]=matrix1[i][j]+matrix2[i][j]
print("ADDITION OF TWO MATRIX IS AS FOLOOWS")
for i in range(r):
    for j in range(c):
        print(matrix3[i][j],end=" ")
    print(end="\n")

