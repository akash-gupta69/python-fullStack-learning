a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number:  "))

# largest = max(a,b,c)

if(a>b):
    if(a>c):
        largest = a
    else:
        largest = c
else:
    if(b>c):
        largest = b
    else:
        largest = c

print(f"the largest number among three is: {largest}")

