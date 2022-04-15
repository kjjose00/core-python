#replace
s='josekj'
old='kj'
new=' k john'
str1=s.replace(old,new)
print(str1)

#split
n='hello how are you'
str2=n.split(' ')
print(n)
print(str2)

#join
name=('hello','how','are','you')
str3=' '.join(name)
print(str3)

#startswith
print(s.startswith('j'))

#endswith
print(s.endswith('j'))