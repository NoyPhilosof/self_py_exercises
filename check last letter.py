# function that prints True if the last letter in a string appears before and False if it doesn\'92t.\

def last_early(my_str):
    lower_string = my_str.lower()
    if(lower_string[-1:]) in (lower_string[0:-1]):
        print("True")
    else:
        print("False")


last_early("happy birthday")
last_early("best of luck")
last_early("Wow")
last_early("X")
