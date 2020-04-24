import random
import string

password_length = int(input("Enter password length:- "))

# print(string.ascii_letters) -A-Za-z
# print(string.digits)  0-9
# print(string.punctuation) !@#$%
# possible_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
possible_characters = string.ascii_letters + string.digits + string.punctuation

# list comprehension 
random_character_list = [random.choice(possible_characters) for i in range(password_length)]

# joining the possible characters in the list to form a string
random_password = ''.join(random_character_list)
print(random_password)