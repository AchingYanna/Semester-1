#PRACTICAL 8: WAP to swap first n characters between two strings


# Input strings and the number of characters to swap
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
n = int(input("Enter the number of characters to swap: "))

# Swap the first n characters if n is valid
if n <= min(len(string1), len(string2)):
    string1, string2 = string2[:n] + string1[n:], string1[:n] + string2[n:]
    print("After swapping:")
    print("First string:", string1)
    print("Second string:", string2)
else:
    print("The value of n is too large for one of the strings.")
