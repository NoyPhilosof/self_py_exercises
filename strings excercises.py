# This application sample the first character in a string amd replaces all re-occurrences with the letter "e"

user_string = input("Please enter a valid string: ")
print()

modified_string = user_string[1:].replace(user_string[0], "e")
print(user_string[0] + modified_string)
print()
print()
print()


# prints a string with the second half in capital letters
user_string = input("Please enter a string: ")
capitalize_from = int(len(user_string) / 2)
print()
print(user_string[:capitalize_from] + user_string[capitalize_from:].upper())
print()
print()
print()

# receving a user input and printing it as - - - 
full_word = input("Please enter a word: ")  # original input 
length_of_string = len(full_word)  # length of the original input
secret_string = (" - " * length_of_string)  # creating string with same number of - - - as the original input
print(secret_string)

