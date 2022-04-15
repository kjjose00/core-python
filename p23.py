# f-string/formatted string literal
a=20
print(f'my age is {a}')#integer
print(f'{20} {30}')#multiple values
# print(f'{}')#error blank not allowed
#---------string---------
f_name='jose'
l_name='john'
print(f'{f_name} {l_name}')
num=19
print(f'{num:05d}')
print(f'{12.345:.20f}')
price=1234567890
print(f'{price:,}')
print(f'{10*8}')

data={'jose':3000,'john':4000}
print(f'{data["jose"]} {data["john"]}')

name='jose'
print(f'{{name.upper()}}')

from datetime import datetime
# today=datetime(2022,10,4)
td=datetime.today()
print(f'{td:%d  %b %y}')