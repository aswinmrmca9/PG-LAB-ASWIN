a=int(input("enter the starting year="))
b=int(input("enter the end year="))
if(a<b):
    print("Leap year")
    for i in range(a,b):
        if(i%4==0 and i%100!=0):
            print(i,end=" ")


