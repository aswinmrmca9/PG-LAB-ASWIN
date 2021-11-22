a=int(input("Enter the 1st number"))
b=int(input("Enter the 2nd number"))
c=str(input("Choose the option \n Add(+) Sub(-) mul(*) div(/)"))
if(c=="+"):
    print("Sum=",a+b)
elif(c=="-"):
    print("sub=",a-b)
elif(c=="*"):
    print("mul=",a*b)
else:
    print("div=",a/b)
