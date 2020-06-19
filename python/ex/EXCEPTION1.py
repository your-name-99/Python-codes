f=open('ds.txt','w')
a=int(input())
b=int(input())
try:
    f.write("%d" % (a/b))
except Exception as e:
    print("you can't devide a number by zero")
f.close()
f=open('ds.txt','r')
p=f.read()
print(p)
f.close()
