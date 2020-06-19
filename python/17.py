sum=0
x=0
y=1
for i in range(3,101):
    z=x+y
    if(z%2==0):
        sum=sum+z
    x=y
    y=z
print(sum)
