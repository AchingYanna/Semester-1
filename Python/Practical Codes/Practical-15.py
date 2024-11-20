#PRACTICAL 11: TO READ A FILE AND DO THE FOLLOWING OPERATIONS



# Open the file in read mode
filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        content = file.read()  # Read the entire file content
        
        # Operation m: Count the number of lines
        file.seek(0)  # Reset the cursor to the beginning of the file
        lines = file.readlines()
        line_count = len(lines)

        # Operation n: Count the number of words
        word_count = len(content.split())  # Split the content into words and count them

        # Operation o: Count the number of characters
        char_count = len(content)  # Count all characters including spaces

        # Print results
        print("Number of lines (m):", line_count)
        print("Number of words (n):", word_count)
        print("Number of characters (o):", char_count)

except FileNotFoundError:
    print("The file was not found. Please check the filename and try again.")
