def prime(a,b):
    A=[]
    for i in range(a,b+1):
        flag=0
        j=(i/2)
        j=int(j)
        for k in range(2,j+1):
            if(i%k==0):
                flag=1
                k=j+3
                break
        if(flag==0):
            A.append(i)
    return(A)
