import random

# All chars we can use for password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")

password = ""
password_list = []

# Inputs for user to give some parameters
nr_letters= int(input("How many letters would you like in your password?: "))
nr_numbers = int(input(f"How many numbers would you like in your password?: "))
nr_symbols = int(input(f"How many symbols would you like in your password?: "))

# Loops for randomly selecting chars out of arrays
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

# This function shuffles an array of chosen chars
random.shuffle(password_list)

# Concat all chars into string so we can print it to user
for char in password_list:
    password += char

# At the end password is printed to the user
print(f"Your password is: {password}")