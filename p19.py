from numpy import *
r=int(input('enter number of rows:'))
c=int(input('enter number of columns:'))
a=zeros((r,c),dtype=int)
for i in range(r):
	for j in range(c):
		a[i][j]=int(input('enter element:'))
for i in range(r):
	for j in range(c):
		print(a[i][j])

