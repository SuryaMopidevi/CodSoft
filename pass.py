import random
import string


# password generation function
def passwordGenerator(len):
    characters=string.ascii_letters+string.digits+string.punctuation
    password = ''.join(random.choice(characters) for _ in range(len))
    return password

# taking input length of the password
len=input("Enter length of the password  : ")

# checking number 1 whether it is digit or not 
if(len.isdigit()):
        len=int(len)

        # checking whether password length is equal to 0 or not 
        if len == 0 :
            print("Password length must be greater than 0 ")
        else:
            # generating password of specified length
            print("Generated password  : " ,passwordGenerator(len))
else:
    # checking whether the input given is character 
    if len.isalpha():
        print("Please enter numbers only ")
    else:
        # checking whether the input given (length) is negative 
        print(" length cannot be negative  number ")
    quit()

