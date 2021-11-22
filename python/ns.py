n=int(input("enter the row"))
for i in range(1,n+2):
    for j in range(1,i):
        print(j,end=" ")
    print()

print("...........")

for i in range(0,3):
    for j in range(1,i+2):
        print(j,end=" ")
    print()
