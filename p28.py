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

