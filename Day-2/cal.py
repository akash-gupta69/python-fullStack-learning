'''
a = int(input("Enter the number: "))

if(a>0):
    print("the number is positive")
elif (a==0):
    print("the number is neither positive nor negative, it is 0")
else:
    print("the number is negative")
'''
'''
num = int(input("enter number:"))
if(num%2==0):
    print("it is even")
else:
    print("it is odd")
'''
'''
b = int(input("enter a number:"))
if( b%3 == 0 & b%5 == 0):
    print("It is divisibile by both")
else:
    print("not  divisible")
'''
'''
a = int(input("enter a number: "))
b = int(input("enter a number: "))
c = int(input("enter a number: "))

if (a>b and a>c):
    print("the greatest value is: ",a)
elif (b>c and b>c):
    print("the greatest value is: ",b)
else:
    print("the greatest value is: ",c)
'''


'''
m = input("Enter an alphabet: ")
vowels = ['a','e','i','o','u']

if not m.isalpha() :
    print("m is not an alphabet")
elif(m.lower() in vowels):
    print("The given alphabet is vowel: ",m)
else:
    print("The given alphabet is a consonant: ",m)
    '''


'''
u = int(input("Enter a number: "))
if u>=75:
    print("Eligible")
else:
    print("Not eligible")
'''

'''
a = int(input("Enter a value: "))
if len(a) == 2:
    print("valid")
else:
    print("not valid")
'''

'''

exp = input("data for eval: ")

result = eval(exp)

print(f"The result is {result}")  # __import__ ("os").system("ls") # It just prints the directory listing to the terminal # it is generally called PAYLOADs
'''

'''

year =int(input("Enter a year: "))

if( year % 4 ==0 and year % 100!=0) or (year % 400 == 0):
    print(f" {year} is a leap year")
else:
    print(f" {year} NOt a leap year")

'''

'''
temp = float(input("Enter temperature: "))

if(temp<15):
    print("cold")
elif(temp>=15 and temp<=30):
    print("Moderate")
else:
    print("Hot")

'''

