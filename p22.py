#format() string
str='my age is {}'
print(str.format(37))
print('{1} {0}'.format(10,20))
print('{n2} {n1}'.format(n1='josek',n2='john'))
print('{:d}'.format(37))
print('{num:*<5d}'.format(num=15))
print('{num:*>5d}'.format(num=15))
print('{num:*^5d}'.format(num=15))
#float-------------------------
print('{}'.format(12.34))
print('{:f}'.format(12.34))
print('{num:8.3f}'.format(num=12.34))
print('{num:+8.3f}'.format(num=12.34))
#string--------------------------
print('{:*<8}'.format('jose'))
print('{:*>8}'.format('jose'))
print('{:*^8}'.format('jose'))
print('{:.2s}'.format('jose'))

print('{:,}'.format(1234567890))
print('{:_}'.format(1234567890))

data={'jose':3000,'kjohn':4000}
print('{0[jose]:d} {0[kjohn]:d}'.format(data))
print('{jose} {kjohn}'.format(**data))