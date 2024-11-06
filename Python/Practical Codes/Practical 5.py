#PRACTICAL 5: GENERATING A PYRAMID AND INVERSE PYRAMID

# Number of rows in the pyramid
rows = 5

# Generate pyramid
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

#Generating an inverse pyramid
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
