x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))
if(x>y)&&(x>z):
	largest=x
elif((y>x)&&(y>z)):
	largest=y
else:
	largest=z
	print("The largest number is",largest)
