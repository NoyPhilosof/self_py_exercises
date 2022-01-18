def multiplication(num1, num2): 
    """Calculates multiplication of two numbers.
    :param num1: first value
    :param num2: second value
    :type num1: int
    :type num2: int
    :return: The result of multiplying two numbers
    :rtype: int """
    after_multiplication = (num1 * num2)
    return after_multiplication


def main():
    """Call the function func
    :return: None
    """
    print(multiplication(5, 4))
    return


if __name__ == "__main__":  
    main()
