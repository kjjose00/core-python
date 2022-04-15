from numpy import *

a=array([100,200,300,400,500])
b=a.view()
a[1]=2
b[2]=3
print(id(a))
print(a)
print(id(b))
print(b)