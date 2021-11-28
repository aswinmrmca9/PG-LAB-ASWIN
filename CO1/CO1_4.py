str1 = input("Enter a string : ")
word = str1.split()
count= []
for w in word:
	count.append(word.count(w))
	print("count of the occurrence:" + str(list(zip(word, count))))
