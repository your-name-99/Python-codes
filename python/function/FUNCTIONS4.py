A=[]
B=[]
A=list(map(int,input().split()))
def cu_pro(B):
    C=[]
    flag=0
    count=0
    l=len(B)
    for i in range(l):
        for j in range(l):
            if(B[i]==B[j]):
                flag=flag+1
        if(flag==1):
            C.append(B[i])
            count=count+1
        flag=0
    for i in range(count):
        print(C[i],end=' ')
    
cu_pro(A)
