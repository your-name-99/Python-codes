sum=0
flag=0
for i in range(2,2001):
    k=i/2
    k=int(k)
    for j in range(2,(k+1)):
        if(i%j==0):
            flag=1
            break
    if(flag==0):
        sum=sum+i
    flag=0
print(sum)
