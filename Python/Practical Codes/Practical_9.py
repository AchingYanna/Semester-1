#PRACTICAL 9: FINDING INDICES OF SUBSTRINGS IN STRINGS

string = input("Enter the Main string: ")
sub_string = input("Enter the sub-string to search: ")

indices = []
start = 0

while True:
    index = string.find(sub_string, start)
    if index == -1:
        break

    indices.append(index)
    start = index + 1


if indices:
    print("Indices of occurences: ", indices)

else:
    print("No sub-string as such found:", '/n', "Indice =  -1")
    
