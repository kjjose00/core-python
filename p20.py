#slicing in two dimensional array using numpy
from numpy import *

a=array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
n=a[0,:2]#row selection slicing
print(n)
n1=a[:,2]#column selection slicing
print(n1)
n2=a[0:3,0:3]
print(n2)
