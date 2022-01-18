# program to calculate is a given amount of chocolate bars are enough 

def chocolate_maker(small, big, x):
    bigx3 = (big * 5)
    if x <= (small + bigx3):
        is_possible = True
        return is_possible
    else:
        is_possible = False
        return is_possible


print(chocolate_maker(3, 1, 8))
print(chocolate_maker(3, 1, 9))
print(chocolate_maker(3, 2, 10))