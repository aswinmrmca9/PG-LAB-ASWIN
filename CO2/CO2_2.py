n=int(input("Enter the number"))
x=0
y=1
s=0
count=1
print("Fibanocci=",end=" ")
while(count<=n):
    print(s,end=" ")
    count+=1
    x=y
    y=s
    s=x+y
    
