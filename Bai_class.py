'''
----------------------------------------------------
Examples:
def test_var_args(a, *argv):
	print("first normal arg:", a)
	for arg in argv:
		print("another arg through *argv:", arg)

test_var_args("google","facebook","python",1,"Lotus")

---------------------------------------------------
Usage of *arg : give you pass an unspecified number of 
argument to a funtion
---------------------------------------------------
def take_number(a,*args):
	sum = 0
	if a>3:
		print(f"first number: {a} is higher than 3")
	else:
		print(f"your number: {a} is lower than 3")
	for arg in args:
		sum += arg
	sum = sum +a
	print(f"Sum of all element is {sum}")

a = int(input('Nhập số bất kì nhưng lớn hơn 3:'))
for i in range(3):
	argu = int(input('Nhập một dãy số gồm 3 số:'))
else:
	pass


take_number(a,argu)
-----------------------------------------------------
'''
'''
----------------------------------------------------
Usage of *kwags : Allows you pass keyworded variable 
length of arguments to a function
----------------------------------------------------
def greet_me(**kwargs):
	for key,value in kwargs.items():
		print("{0} : {1}".format(key, value))

greet_me(name1="ducvu",name2="hongduc")
----------------------------------------------------
# *args
---
'''
"""
# import pdb
# def test_args(arg1,arg2,arg3):
# 	print("arg1",arg1)
# 	print("arg2",arg2)
# 	print("arg3",arg3)
# args = {"one",1,"4'"}# set,list,tuple can be used by *arg
# test_args(*args)

# mydict = {"arg3":3,'arg2':"two","arg1":5}
# test_args(**mydict)
#----------------------------------------
#GENERATORS ARE ITERATORS,ONLY ITERATE OVER THEM ONCE.BECAUSE
THEY NOT STORE ALL THE VALUES IN MEMORY ,THEY GENERATE THE 
VALUES ON THE FLY .HOWEVER, THEY NOT RETURN A VALUE,THEY YIELD 
IT.
------------------------------------------
EXAMPLES

def generator_function(x):
	for i in range(x):
		yield i
# for item in generator_function():
# 	print(item)
x = int(input("nhap vao so nguyen"))
print(generator_function(x))

def fibon(n):
	a=b=1
	for i in range(n):
		yield a
		a,b = b,a+b
for x in fibon(2):
	print(x)
"""

#MAP,FILTER AND REDUCE
'''
map(function_to_apply,list_of_inputs)


def mutiply(x):
	return (x*x)
def add(x):
	return(x+x)

funcs = [mutiply,add] #list of functions instead of a list_of_inputs

for i in range(5):
	value = list(map(lambda x: x(i),funcs))
	print(value)

#FILTER 
number_list = range(-5,5)
minlist = list(filter(lambda x:x<0,number_list))
logiclist = list(map(lambda c:c<0,number_list))
print(minlist,logiclist)

#REDUCE
a =1
R_list = [1,1,2,3,5,8]
b = 1
for i in R_list:
	a = a* i
print(a)
from functools import reduce
b = reduce((lambda x,y:x*y),R_list)

print(f"gia tri {b}")
'''
def greet(name = "Vu"):
	
	def hi():
		return "inside function hi()"
	def welcome():	
		return "inside function welcome()"
	list = [hi,welcome]
	if name == "Vu":
		return welcome
	else :
		return hi

x = greet("Vu")
print(x())






