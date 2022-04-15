#function 
def add(a,b):
	print('this is a function')
	print(a+b)

add(10,20)

#return statement
def ddd(a,b):
	s=a+b
	m=b-a
	return s,m

sum,result=ddd(20,30)
print('sum=',sum)
print('result=',result)

# nested function
def disp():
	def inner():
		print('inner function')
	print('outer function')
	inner()

disp()
	
# passing a function as parameter to another function
def one(t):
	print('one function'+t())

def two():
	return ' function two '

one(two)

# a function return another function
def dsp():
	def inn():
		return 'inner function'
	print('outer')
	return inn
c=dsp()
print(c())

# actual and formal arguments
def ad(x,y):# x and y are formal arguments
	print(x+y)

ad(56,78)# 56 and 78 are actual arguments


# types of actual arguments
# 1. positional arguments
def pwd(x,y):
	z=x**y
	print(z)
pwd(5,2)

# 2. keyword arguments
def sh(name,age):
	print(f'{name} {age}')

sh(name='jose',age=37)# keyword arguments

# 3.default arguments
def show1(name,age=37):#age=37 is default argument
	print(name,age)
show1('josekj')

# variable length arguments
def varlen(*x):
	s=0
	for i in range(len(x)):
		s=s+x[i]

	
	print(s)
varlen(56,45,78,34,55,67)


#keyword variable length arguments
def keyargs(**num):
	z=num['a']+num['b']+num['c']
	print(z)
keyargs(a=5,b=2,c=7)

# lambda function
# no name
sum=lambda x,y:x+y
print(sum(20,30))

# nested lambda function
add=lambda x=10:(lambda y:x+y)
a=add()
print(a(20))

# passing lambda function to another function
def show2(a):
	print(a(8))
show2(lambda x:x)

# returning lambda function
def add3():
	y=20
	return (lambda x:x+y)
a=add3()
print(a(10))

(lambda x:print(x+1))(5)#immediate 


# local variable	=	variable inside a function
def localv():
	x=10	#local variable
	print(x)
localv()

# global variable
# scope of global variable is entire program
a=20
def show4():
	x=10
	print(x)
	print(a)
show4()

# if local variable name and global variable name is same the function
# by default ignores global variable
# for accessing global variable inside function use global keyword
a=50
def show5():
	global a
	print(a)
show5()
print(a)

# globals function 
a=20
def show8():
	a=10
	print('local variable:',a)
	g=globals()['a']
	print('global variable:',g)
	g=50
	print(g)
show8()
print('a:',a)

# Recursion --- default 1000 times
i=0
def myfun():
	global i
	i=i+1
	print('josekj',i)
	myfun()
myfun()





