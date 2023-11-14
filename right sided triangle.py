# write a program to print  
n=5
for i in range(n): # for rows
    for j in range(i,n): # for columns (Spaces)
        print(" ",end=" ")
    for j in range(i+1): # for columns (Stars)
        print("*",end=" ")


    print()