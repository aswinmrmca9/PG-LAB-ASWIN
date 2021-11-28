w =str(input("Enter the word :"))
print("The original string is : "+w)
print("The vowel are : ",end="")
for i in w:
 	if i in 'aeiouAEIOU':
 		print([i],end=" ")
