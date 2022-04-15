from numpy import *

a=ones((3,2),dtype=int)
# print(a)
# for i in a:
# 	for j in i:
# 		print(j)
# 	print()

i=0
while i<len(a):
	j=0
	while j<len(a[i]):
		print(i,j,a[i][j])
		j=j+1
	i=i+1