s='josekj'
for i in range(len(s)):
	print(s[i])

print('d'*10)#repetition operator
#c-style string formatting
print('my name is %s and age is %d'%('josekj',37))
print('my nam is %(nm)s age is %(ag)d'%{'nm':'josekj','ag':37})
print('%f'%12.34566746)
print('%s'%'my name is GOD')
print('%s%s'%('my name is','god'))
print('%d'%5435442)