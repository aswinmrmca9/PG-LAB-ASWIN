x=int(input("enter the number"))
y=int(input("enter the number"))
z=int(input("enter the number"))
if(x>y):
    if(x>z):
        print("x is large",x)
    else:
        print("z is large",z)
else:
    if(y>z):
        print("y is large",y)
    else:
        print("z is large",z)
