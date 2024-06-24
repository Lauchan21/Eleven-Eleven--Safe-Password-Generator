#Eleven:Eleven Safe Password Generator V1.02
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '^','@']

print("Eleven:Eleven Safe Password Generator Version 1.02")
print("\n")
print("SPG is an opensource non custodial password generator.")
print("\n")
print("Before proceed do acknowledge the following:")
print("1. Each password will be uniquely generated; be sure to carefully save it before closing the app.")
print("2. Carefully note the generated password before closing the app, as it will not be saved.")
print("3. To confirm data integrity We recommend to disconntect from Wifi or teethering before proceeding.")
print("4. We suggest you to safely save your password in a dedicated app such as KeePassX for additional security.")
print("\n")
nr_letters = int(input("Choose how many letters you would like in your password?\n"))
nr_symbols = int(input(f"Choose how many symbols you would like in your password?\n"))
nr_numbers = int(input(f"Choose how many numbers would you like in your password?\n"))

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your unique password is your password: {password}")
