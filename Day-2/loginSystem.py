'''

user = "Admin"
password = "Password"

a = str(input("Enter user id: "))
b = input("Enter password: ")

if(a == user and b == password ):
    print("sign in sucessfull")
else:
    print("Unauthorized access")

'''

#Valid Triangle
'''
side_1  = float(input("Enter value:"))
side_2  = float(input("Enter value:"))
side_3  = float(input("Enter value:"))

if( side_1 + side_2 > side_3 and side_2 + side_3 > side_1 and side_1 + side_3 > side_2):
    print("Perfect triangle")
else:
    print("Not a triangle")


'''


'''
a = float(input("length of side a: "))
b = float(input("length of side b: "))
c = float(input("length of side c: "))

if( a**2 + b**2 == c**2 or c**2 + b**2 == a**2 or a**2 + c**2 == b**2  ):
    print("It is  a right angle triangle")
else:
    print("Not")
'''

a = float(input("length of side a: "))
b = float(input("length of side b: "))
c = float(input("length of side c: "))


'''


if( a == b == c):
    print("It is an equilateral triangle")
elif(a!=b!=c):
    print("It is a scalene triangle")    
else:
    print("It is Isoceles triangle")

'''

