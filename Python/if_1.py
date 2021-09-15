a = int(input("Enter first Number : \n"))
b = int(input("Enter second Number : \n"))
c = int(input("Enter third Number : \n"))
d = int(input("Enter fourth Number : \n"))
if (a>b):
	f1=a
else:
	f1=b
if(c>d):
	f2=c
else:
	f2=d
if(f1>f2):
	print(str(f1)+" is the greatest number")
else:
	print(str(f2)+" is the greatest number")