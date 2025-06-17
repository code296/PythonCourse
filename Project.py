# Project ---> Guessing number

import random

target = random.randint(1, 100)
while True:
    num = int(input("Guess the target or Quit "))
    if(num == "Q"):
        break

    num = int(num)
    if(num == target):
        print("Success: Correct Guess!")
        break
    if(num < target):
        print("Your number was too small, take a greater one")
    else:
        print("Your number was too big. Take a smaller one")

print("GAME OVER")

# Project -----> Random password generator
 
import random
import string

# print(string.ascii_letters) # give alphabets
# print(string.digits)    # give digits
# print(string.punctuation)  # give punctuator

pass_len = 12
charValue = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charValue)

print("your random password is: ", password)

















