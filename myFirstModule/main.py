from packages import help

from packages import power
from packages import simple_math
""" a = help.help_info()
 """
r = power.power_in(5,2)
f = simple_math.add(4,6)
# print(a)
print(r)
print(f)
print(help(power.power_in))

'''
list_1 = [1,2,3]
list_2 = [1,2,3]
print(list_1 == list_2)
print(list_1 is list_2)

print("/////")

set_1 = [1,2,3]
set_2 = [1,2,3]
print(set_1 == set_2)
print(set_1 is set_2)

print("/////")

tp = (1,2,3)
tp_1 = (1,2,3)
print(tp == tp_1)
print(tp is tp_1)

print("/////")

dic_1 = {"name":"Akash"}
dic_2 = {"name":"Akash"}
print(dic_1 == dic_2)
print(dic_1 is dic_2 )
'''

''' Squaring list using lambda function '''

# list_3 = [1,2,3,4,5]
# s = lambda x : x ** 2
# print(list(map(s,list_3)))

from calPro import calc as cp

print(cp.sub(6,5))
print(cp.mul(3,6))