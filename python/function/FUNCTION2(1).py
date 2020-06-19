print("ENTER TWO NO FIRST BIGGER THEN SMLALER")
n1,n2=input().split()
n1=int(n1)
n2=int(n2)
def compute(n3,n4):
    for i in range(1,n4+1):
        if(n3%i==0 and n4%i==0):
            gcd=i
    lcm=(n3*n4)/gcd
    print(gcd)
    print(int(lcm))
compute(n1,n2)
