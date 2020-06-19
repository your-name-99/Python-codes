n=int(input())
l1=[]
l2=[]
for i in range(n):
    name=input()
    run=int(input())
    l1.append(name)
    l2.append(run)

d=dict(zip(l1,l2))
print(d)
m=input("ENETR THE KEY TO BE SEARCHED")
print(d.get(m,-1))
