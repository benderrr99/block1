a=input('первое число: ')
b=input('второе число: ')
c=input('третье число: ')
if int(a)==int(b)==int(c):
	print(3)
elif int(a)!=int(b) and int(a)!=int(c) and int(b)!=int(c):
	print(0)
else:
	print(2)