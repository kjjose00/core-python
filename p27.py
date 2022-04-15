# pass/call by object reference
def val(lst):
	print(lst,id(lst))
	lst.append(4)
	print(lst,id(lst))
lst=[1,2,3]
val(lst)

# lists are mutable

# immutable objects-->integer,float,string and tuple

# mutable objects-->list and dictionary

### function decorator
# eg:1
def dec(num):
	def inner():
		print('before decoration.')
		num()
		print('after decoration.')
	return inner
@dec
def num():
	print('this is the basic function')

num()

#eg:2
def decor(no):
	def inner():
		a=no()
		add=a+10
		return add
	return inner

@decor
def no():
	return 10

print(no())

#eg:3
def decora1(no1):
	def inner():
		b=no1()
		multi=b*5
		return multi
	return inner

def decora(no1):
	def inner():
		c=no1()
		add=c+5
		return add
	return inner
@decora
@decora1
def no1():
	return 10

print(no1())

#-------------------------------- 
# passing array to function
#--------------------------------
from array import *

def show(ar):
	print(ar)
	print(type(ar))
	for i in ar:
		print(i)

a=array('i',[101,102,103,104,105])
show(a)

#-----------------------------------
#returning array from function
#------------------------------------
from array import *

def show(ar):
	print(ar)
	print(type(ar))
	for i in ar:
		print(i)
	return ar

a=array('i',[101,102,103,104,105])
ra=show(a)
print('returning array:',ra)

#--------------------------------------
# numpy built in math functions
#--------------------------------------
#1.sum
#2.prod
#3.sqrt

#sum

from numpy import *

a=array([24,34,45,56,78])
print('a:',sum(a))

#prod

print('a:',prod(a))
b=array([[1,2,3,4],[1,2,3,4]])
print('b:',prod(b))

#sqrt

print('a:',sqrt(a))
print('b:',sqrt(b))

# math module 

from math import *

print(floor(4.5))# 4
print(ceil(4.5))# 5
print(sqrt(49))
print(factorial(5))
print(pow(5,2))

















