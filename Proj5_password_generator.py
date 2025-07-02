import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
no_letters = int(input("How many letters would you like in your password?\n")) 
no_symbols = int(input(f"How many symbols would you like?\n"))
no_numbers = int(input(f"How many numbers would you like?\n"))

#Easy level
# password = ""
# for char in range(1, no_letters + 1):
#     password += random.choice(letters)
# for char in range(1, no_symbols + 1):
#     password += random.choice(symbols)
# for char in range(1, no_numbers + 1):
#     password += random.choice(numbers)

# print(password)

#Hard level
password_list = []
for char in range(1, no_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, no_symbols + 1):
    password_list += random.choice(symbols)
for char in range(1, no_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = "" 
for word in password_list:
    password += word

print(f"{password}")