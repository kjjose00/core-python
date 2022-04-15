# string functions

s='jose kj'
print(s.upper())#upper
print(s.lower())#lower
print(s.title())#title
print(s.swapcase())#swaps case

print(s.upper().isupper())
print(s.islower())
print(s.title().istitle())

n='123456'
print(n.isdigit())
print(n.isalnum())
s1='ghghsgh'
print(s1.isalpha())

name=' '
print(name.isspace())

sp='	ghfhdfh	'
print(sp)
print(sp.lstrip())#removes left space
print(sp.rstrip())#removes right space
print(sp.strip())#removes both left and right sapce

