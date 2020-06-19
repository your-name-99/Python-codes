#f = open('hello.txt','a')
#s=input("enter \n")
#f.write(s)
#f.close()
f=open('hello.txt','r')
for data in reversed(list(f)):
    print(data)


f.close()
