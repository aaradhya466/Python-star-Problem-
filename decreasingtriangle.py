# write a program to print 
# * * *  * *
# * * * *
# * * * 
# * * 
# * 
n=int(input("Enter the number\n")) # user input
for i in range(n): # For rows
    for j in range(n-i): # For Columns
        print("*",end="  ")
    print()