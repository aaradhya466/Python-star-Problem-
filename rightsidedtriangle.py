# write a program to print  a right sided traingle with increasing spaces and decreasing stars
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=' ')
    print()
