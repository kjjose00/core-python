from numpy import *

a=array([1,2,3,4,5,6,7,8,9,10,11,12])
b=reshape(a,(2,3,2))
print(b)
c=b.flatten() #convert to 1 d array
print(c)