
import string
import random
import sys

def generate():
    new_password = []

    while True:
        try:
            password_length = int(input("How many characters would you like your password to be: "))
        except:
            print("Please enter numeric digits: ")
            continue
        if password_length < 10:
            print("Password must be at least 10 characters long!")
            continue
        else:

            char_list = list(string.ascii_letters)
            digit_string = string.digits
            symbol_string = string.punctuation

            for i in digit_string:
                char_list.append(i)

            for i in symbol_string:
                char_list.append(i)

            last_index = len(char_list) - 1

            for i in range(password_length):
                pass_char = char_list[random.randint(0,last_index)]
                new_password.append(pass_char)
            empty_string = ""
            new_password = empty_string.join(new_password)
            print("This is your new password: " + new_password)
            quit()
                
generate()
