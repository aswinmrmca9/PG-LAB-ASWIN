c=int(input("1.area of circle \n2.area of rectangle \n3.area of square \n"))
if(c==1):
    r=int(input("Enter the radius"))
    print("area of circle=",3.14*r*r)
elif(c==2):
       l,b=(int(x) for x in input("Enter the length and breath").split())
       print("area of rectangle=",l*b)
else:
    a=int(input("Enter the side"))
    print("area of square=",4*a)
    
      
