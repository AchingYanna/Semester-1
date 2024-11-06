#PRACTICAL 10: WAP to create a list of the cubes of only the even integrs in a list


#Taking user input for the list
user_input = input("Enter the entries seperated by ',': ")

input_list = []


#Checking the type of entries
for item in user_input.split(','):
    item = item.strip()

    if item.isdigit(): #Checking if the entry is a integer value
        input_list.append(int(item))

    else:
        try: #Checking if the entry is a float
            input_list.append(float(item))

        except ValueError: #If neither the case then adding it to the list as a string
            input_list.append(item)

def cube_input(input_list):
    loop_list = []

    for item in input_list:
        if isinstance(item,int) and item%2 == 0:
            loop_list.append(item**3)


    list_comprehension = [item**3 for item in input_list if isinstance (item, int) and item%2 == 0]
    return loop_list, list_comprehension

loop_list, list_comprehension = cube_input(input_list)

print("Using 'for' loop: ", loop_list)
print("Using List comprehension: ", list_comprehension)



