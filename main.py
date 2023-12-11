import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

number_of_letters = int(input("How many letters would you like in your password? \n"))
number_of_symbols = int(input("How many symbols would you like in your password? \n"))
number_of_numbers = int(input("How many numbers would you like in your password? \n"))

password_characters = []

# Add random letters to the password
for _ in range(number_of_letters):
  password_characters.append(random.choice(letters))
  
# Add random symbols to the password
for _ in range(number_of_symbols):
  password_characters.append(random.choice(symbols))
  
# Add random numbers to the password
for _ in range(number_of_numbers):
  password_characters.append(random.choice(numbers))
  
# Shuffle the characters in the password
random.shuffle(password_characters)

# Convert a list of characters into a string
password = "".join(password_characters)

print(f"Your password is: {password}")