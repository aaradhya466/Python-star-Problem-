n=int(input("Enter the number\n")) # user input
for i in range(n): # For rows
    for j in range(i+1): # For Columns
        print("*",end="  ")
    print()