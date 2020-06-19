print("ENTER TWO NO FIRST BIGGER THEN SMLALER")
n1,n2=input().split()
n1=int(n1)
n2=int(n2)
for i in range(1,n2+1):
    if(n1%i==0 and n2%i==0):
        gcd=i
lcm=(n1*n2)/gcd
print(int(lcm))
