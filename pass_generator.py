import random
import string

# string.ascii_letters   A-Za-z
# string.digits     0-9
# string.punctuation     !@#$%
chars = string.ascii_letters + string.digits + string.punctuation

# How many passwords do you want to be generated
number = int(input('Number of passwords:- '))

# How long the password will be
length = int(input("Password length:- "))

for p in range(number):
    # start as an empty string
    password = ''
    for c in range(length):
        # adds random letters tp password string 
        password += random.choice(chars)
    print(password)

print(user)
