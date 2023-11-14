n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1): # note to get a peak of hill you need to change one of the column from i + 1 to i
        print("*",end=' ')
    for j in range(i):
        print("*",end=' ')
    print()