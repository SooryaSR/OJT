# Nested Loop
# Define the size of the pattern
size = 7
# Nested loops to iterate through rows and columns
for row in range(size):
    for col in range(size):
        # Conditions to determine whether to print '*' or ' '
        if (col == 1 or col == 5) and row != 0:
            print("*", end="")
        elif (row == 0 or row == 3) and (1 < col < 5):
            print("*", end="")
        else:
            print(" ", end="")
    
    # Move to the next line after each row is printed
    print()