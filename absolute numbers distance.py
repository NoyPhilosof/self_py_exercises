# find and compare numbers distance in absolute values

def distance(num1, num2, num3):
    if (abs(num1 - num2) == 1 or abs(num1 - num3) == 1) and ((abs(num2 - num1) >= 2 and abs(num2 - num3) >= 2) or (abs(num3 - num1) >= 2 and abs(num3 - num2) >= 2)):
        print("True")
        return True
    else:
        print("False")
        return False
