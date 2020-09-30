# Poetry Slam

# Import random module
import random
#Import os module to help clear during loop
import os 

# Welcome the user
print("Hi there, welcome to my poetry slam!")
print("The Poem of the Day is 'The Road Not Taken' by Robert Frost.")
print("Please make a selection below: \n")

# Creation of function to print out the menu of options to choose from
def get_user_input():
    print("1. Read the poem as it was originally written. \n")
    print("2. Read the poem written backwards. \n")
    print("3. Read the poem in random written order. \n")
    print("4. Read the poem lines from shortest to longest. \n")
    print("5. Read the poem lines from longest to shortest. \n")
    return input("Choose a number from the list or type 'done' to exit program. \n")

# Creation of get_file_lines() function
def get_file_lines(filename):
    return open(filename, 'r').read().strip().split('\n')

# Creation of lines_printed_normally() function
def lines_printed_normally(lines_list):
    for i in range(len(lines_list)):
        print(f'{lines_list[i]}')

# Creation of lines_printed_backwards() function
def lines_printed_backwards(lines_list):
    for i in range(len(lines_list)- 1, -1, -1):
        print(f'{lines_list[i]}')

# Creation of lines_printed_random() function
def lines_printed_random(lines_list):
    while len(lines_list) > 0: 
        print(f'{lines_list.pop(random.randint(0, len(lines_list)-1))}')

# Creation of lines_printed_custom() function
def lines_printed_custom(length, lines_list):
    lines_list.sort(key = len)
    if length.lower() == 'short':
        for i in range(len(lines_list)):
            print(lines_list[i])
    if length.lower() == 'long':
        lines_printed_backwards(lines_list)

# Creation of add line number to line function
def add_line_number(lines_list):
    for i in range(len(lines_list)):
        lines_list[i] = f'{i + 1} {lines_list[i]}'
    return lines_list        

# Creation of while loop to continuously go through choices until user types 'done'
while True:
    choice = get_user_input()
    if choice == '1':
        lines_printed_normally(add_line_number(get_file_lines('poem.txt')))
        print('\n')
        input("Press Enter to select again.")
        os.system('clear')
    elif choice == '2':
        lines_printed_backwards(add_line_number(get_file_lines('poem.txt')))
        print('\n')
        input("Press Enter to select again.")
        os.system('clear')
    elif choice == '3':
        lines_printed_random(add_line_number(get_file_lines('poem.txt')))
        print('\n')
        input("Press Enter to select again.")
        os.system('clear')
    elif choice == '4':
        lines_printed_custom('short', get_file_lines('poem.txt'))
        print('\n')
        input("Press Enter to select again.")
        os.system('clear')
    elif choice == '5':
        lines_printed_custom('long', get_file_lines('poem.txt'))
        print('\n')
        input("Press Enter to select again.")
        os.system('clear')
    elif choice.lower() == 'done':
        break
    else:
        print("Please make a selection choosing a number from 1-5 or 'done' to exit.")
        input("Press Enter to return to the menu.")
        os.system('clear')
