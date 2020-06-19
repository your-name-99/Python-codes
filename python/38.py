from prim import *
B=[]
c,d=input().split()
c=int(c)
d=int(d)
B=prime(c,d)
l=len(B)
for i in range(l):
    print(B[i],end=' ')
