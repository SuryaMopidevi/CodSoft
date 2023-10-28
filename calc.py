# addition operation
def add(num1,num2):
    try :
        num1 = complex(num1)
        num2 = complex(num2)
        result = num1.real + num2.real
        print(f"{num1.real} + {num2.real} : {result.real}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
    

# subtraction operation
def subtract(num1,num2):
    try :
        num1 = complex(num1)
        num2 = complex(num2)
        result = max(num1.real,num2.real) - min(num1.real,num2.real)
        print(f"{max(num1.real,num2.real)} - {min(num1.real,num2.real)} : {result.real}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

# multiplication operation
def product(num1,num2):
    try :
        num1 = complex(num1)
        num2 = complex(num2)
        result = num1.real * num2.real
        print(f"{num1.real} * {num2.real} : {result.real}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

# division operation
def division(num1,num2):
    try :
        num1 = complex(num1)
        num2 = complex(num2)
        result = max(num1.real,num2.real) // min(num1.real,num2.real)
        print(f"{max(num1.real,num2.real)} // {min(num1.real,num2.real)} : {result.real}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

# modulo operation
def modulo(num1,num2):
    try :
        num1 = complex(num1)
        num2 = complex(num2)
        result = max(num1.real,num2.real) % min(num1.real,num2.real)
        print(f"{max(num1.real,num2.real)} % {min(num1.real,num2.real)} : {result.real}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")


# taking input numbers 
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# taking input arithematic operator
operator=input("Enter Operator(+,-,*,//,%) : ")

# checking an operator for performing operation
if operator=='+' :
    add(num1,num2)
elif operator == '-' :
    subtract(num1,num2)
elif operator == '*' :
    product(num1,num2)
elif operator == '%' :
    modulo(num1,num2)
elif operator == '//' :
    division(num1,num2)
else :
    print("invalid operator ")