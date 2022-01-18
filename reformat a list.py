def format_list(my_list):
    seperator = ', '
    new_list = (seperator.join(my_list[::2]))
    david = '%s and %s' % (new_list, my_list[-1])
    return david


my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
print(format_list(my_list))
