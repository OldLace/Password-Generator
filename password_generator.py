
import string #Used to easily import all possible characters for password
import random #Used to generate random index to choose password characters
import sys #Enables use of quit() 

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
            char_list = list(string.ascii_letters) #list with entire alphabet
            digit_string = string.digits  #string of digits
            symbol_string = string.punctuation #string of punctuation characters\symbols

            for i in digit_string: #loop appends numbers into list with alphabetic characters
                char_list.append(i)

            for i in symbol_string: #loop adds punctuation characters to list with letters & numbers
                char_list.append(i)

            last_index = len(char_list) - 1

            for i in range(password_length):  #loops as many times as there are characters in the sooner to be generated password
                pass_char = char_list[random.randint(0,last_index)] #sets the variable as a random index in the character list (char_list)
                new_password.append(pass_char) #Adds the newly choose character to the new_password list
            empty_string = ""
            new_password = empty_string.join(new_password) #Changes the new password from a list to a easier to read string
            print("This is your new password: " + new_password)
            quit()
                
generate()
