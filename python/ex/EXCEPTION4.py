try:
    count=1
    while(1):
        if(count>10):
            raise StopIteration
        else:
            print(count)
            count=count+1  
except StopIteration:
    print("YOU HAVE TO EXIT NOW")
