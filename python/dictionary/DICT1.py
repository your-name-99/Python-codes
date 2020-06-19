n=int(input())
l1=[]
l2=[]
for i in range(n):
    s=input()
    l=len(s)
    l1.append(s)
    l2.append(l)
d=dict(zip(l1,l2))
print(d)
