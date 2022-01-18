# program to filter ages 13-15 and 16-19

def fix_age(age):
    if (13 <= age < 15) or (16 < age <= 19):
        age = 0
        return age
    else:
        return age


def filter_teens(a=13, b=13, c=13):
    a_fixed = fix_age(a)
    b_fixed = fix_age(b)
    c_fixed = fix_age(c)
    all_fixed = (a_fixed + b_fixed + c_fixed)
    return all_fixed


print(filter_teens())
print(filter_teens(1, 2, 3))
print(filter_teens(2, 13, 1))
print(filter_teens(2, 1, 15))
