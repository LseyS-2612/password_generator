import random
import string

def password_generator(min_length,is_special_bool=True,is_number_bool=True):
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation

    characthers = letters
    if is_special_bool:
        characthers += specials
    if is_number_bool:
        characthers += digits

    password=""
    meets_criteria =False
    has_number = False
    has_special = False
    while not meets_criteria or len(password)<min_length:
        new_char = random.choice(characthers)
        password += new_char

        if new_char in digits:
            has_number =True
        elif new_char in specials:
            has_special = True
        
        meets_criteria =True
        if is_number_bool:
            meets_criteria = has_number
        if is_special_bool:
            meets_criteria = meets_criteria and has_special
    return password

def special_control():
    while True :
        is_special = input("Is there gonna be a special characther ? (Y:N)\n").strip().lower()
        
        if is_special =="yes":
            return True
        elif is_special =="no":
            return False
        else :
            print("!!! Please enter a valid text to continue !!!")
            continue

def number_control():
    while True : 
        is_number = input("Is there gonna be a number ? (Y:N)\n").strip().lower()
        
        if is_number =="yes":
            return True
        elif is_number =="no":
            return False
        else :
            print("!!! Please enter a valid text to continue !!!")
            continue

print("-- Welcome to the Password Generator --")
min_length = int(input("How long can the minimum length be for the password ?\n"))
print("Your password is :", password_generator(min_length, special_control(),number_control()))

