from numpy import *

a=array([100,200,300,400,500])
b=array([1,2,3,400,500])
r=a==b
print(r)
print(any(r))
print(all(r))
re=where(a<b,a,b)
print(re)
d=array([100,2,13,400,90,0])
nz=nonzero(d)
print(nz)