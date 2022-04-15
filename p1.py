import array

st=array.array('i',[])
n=int(input('enter number of elements:'))
i=0
while i<n:
	st.append(int(input('enter element:')))
	i=i+1
st.insert(1,106)

print(st)
st.pop(0)
print(st)