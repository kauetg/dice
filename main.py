import random

def dice_number(number):
    return random.randint(1,number)

print(f"The number is {dice_number(20)}")