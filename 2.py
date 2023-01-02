mkad=109
v=input('скорость байкера: ')
t=input('время в пути: ')
s=int(t)*int(v)
v=s%mkad
print(v)