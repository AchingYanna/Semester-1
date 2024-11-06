# Input string and character for operations
text = input("Enter a string: ")
char = input("Enter the character to analyze or modify: ")

# 1. Find the frequency of the character in the string
frequency = text.count(char)
print(f"The frequency of '{char}' in the string is: {frequency}")

# 2. Replace a character by another character in the string
replace_with = input("Enter the character to replace it with: ")
replaced_text = text.replace(char, replace_with)
print(f"The string after replacing '{char}' with '{replace_with}': {replaced_text}")

# 3. Remove the first occurrence of the character from the string
first_occurrence_removed = text.replace(char, "", 1)
print(f"The string after removing the first occurrence of '{char}': {first_occurrence_removed}")

# 4. Remove all occurrences of the character from the string
all_occurrences_removed = text.replace(char, "")
print(f"The string after removing all occurrences of '{char}': {all_occurrences_removed}")
