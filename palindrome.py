def is_palindrome(user_string):
  backwards_string = user_string[::-1]
  is_it_palindrome = (backwards_string == user_string)
  return is_it_palindrome


user_string = input("Please enter a string: ")
answer = is_palindrome(user_string)
 
if answer:
    print("Ok")
else:
    print("NOT")

