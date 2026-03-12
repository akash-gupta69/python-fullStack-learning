def fs(n):
    if(n == 0):
        return 0
    elif(n==1):
        return 1
    else:
        return fs(n-1) + fs(n-2)

n = int(input("enter a number: "))

for i in range(n):
    print(fs(i),end=" ")