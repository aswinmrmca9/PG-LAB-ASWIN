a=[]
n= int(input("Enter the number :")) 
for i in range(0,n):
	el=input("Enter element :"+ str(i+1) ) 
	a.append(el)
	max1=len(a[0]) 
	temp=a[0]
for x in a: 
	if(len(x)>max1):
		max1=len(i) 
		temp=i
print("Longest Word:",temp) 
print("Length of longest word :",max1)
