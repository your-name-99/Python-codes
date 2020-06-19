import random
x=random.random()
try:
    if(x<0.1):
        raise MemoryError
    else:
        print(x)
        print("No Error")
except MemoryError:
    print("Value Is Below 0.1")
