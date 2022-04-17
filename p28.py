# lists
# lists are mutable
# list printing using for loop
a=[1,2,3,4,5,6]
for i in a:
	print(i)

# list printing using index and for loop
l=len(a)
for i in range(l):
	print(a[i])

# append method

a.append(7)
print(a)

# getting list input from user

a=[]
n=int(input('enter number of elements:'))

for i in range(n):
	k=input('enter element:')
	a.append(k)

print(a)

# insert method
# listname.insert(position number,element)

a=[1,2,3,4,5,6,'jose']
print(a)
a.insert(2,'my name is god')
print(a)

# pop method

a.pop()
print(a)

# pop(n) method

a.pop(3)
print(a)

# remove method
# list_name.remove(element)-->syntax

a=[1,2,3,'jose',4.5]
print(a)
a.remove(4.5)
print(a)

# index method
# syntax-->list_name.index(element)

a=[1,2,3,4,'jose',6.7]
print(a.index('jose'))

# reverse method
print(a)
a.reverse()
print(a)

# extend method

a=[1,2,3,4,5]
b=[6,7,8,9,10]
print('before extend:',a)
a.extend(b)
print('after extend',a)

# count method-shows count of a element in list

a=[10,20,30,10,90]
print(a.count(20))

# sort method
a.sort()
print(a)

# clear method

a=[1,2,3,4,5]
print('before clear:',a)
a.clear()
print('after clear:',a)

# slicing in list

a=[1,2,3,4,5,6,7,8,9,10]
print(a)
print(a[1:5])

# list concatenation

a=[10,20,30]
b=[1,2,3]
r=a+b
print('result:',r)

# repetition of list

a=[1,2,3]
result=a*3
print(a)
print(result)

# aliasing list 
b=a#b is alias name for a in this example
print(b)
a[1]=10
print(b)
b[1]=20
print(b)

# copying in list

a=[10,20,30,40,50]
b=a.copy()

a[1]=22
print(a)
print(b)

# nested list

a=[10,20,30,[40,50,60]]
print(a)

# list function

a=list('josekj')
print(a)

# slicing nested list

x=[[10,20,30],
[40,50,60],
[70,80,90],
[34,56,78],
[99,77,44]]

print(x)
print(x[:][0][0])

# filter function 

a=[0,20,34,55,67,78]
def high_marks(n):
	if n>=60:
		return True
h=filter(high_marks,a)
for i in h:
	print(i)

# map function

a=[10,20,30,40,50,60]

def inc(n):
	return n+2

result=list(map(inc,a))
print(result)

result=list(map(lambda n:n+4,a))
print(result)

# reduce function

from functools import *

a=[10,20,30,40,50]

result=reduce(lambda n,m:n+m,a)
print(result)

# generator function yield statement and next function

def disp99(a,b):
	yield a
	yield b 
result=disp99(10,20)
print(type(result))
print(next(result))
print(next(result))
print(list(result))

