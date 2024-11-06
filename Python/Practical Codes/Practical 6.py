#PRACTICAL 6: ANALYSING AN INPUT


#Takes the character input from user
enter = input("Enter a character: ")


#Checks if the entered character is alphabetical
if enter.isalpha():
    print("The charcater is a letter")
    if enter.isupper():
            print("The charcter is uppercase")
    else:
            print("The character is lower case")

#Checks if the entered character is a numerical value
elif enter.isdigit():
    print("The character is a numerical value")

    digit_names = {
        '0': "ZERO", '1': "ONE", '2': "TWO", '3': "THREE", '4': "FOUR",
        '5': "FIVE", '6': "SIX", '7': "SEVEN", '8': "EIGHT", '9': "NINE"
    }

    print(digit_names[enter])
    

#Checks if the enetred value is a special character
else:
    print("The character is s special value")
