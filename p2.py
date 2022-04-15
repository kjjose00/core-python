from numpy import *

st=array([101,102,103,104,105],dtype=float)
print(st)
st[0]=110
print(st.dtype)
l=len(st)
i=0
while i<l:
	print(st[i])
	i=i+1
	