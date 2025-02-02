#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

# Function to calculate LCM
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Input from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and display the LCM
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {result}")


# In[3]:


import math

# Function to calculate HCF
def hcf(a, b):
    return math.gcd(a, b)

# Input from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and display the HCF
result = hcf(num1, num2)
print(f"The HCF of {num1} and {num2} is {result}")


# In[5]:


# Function to convert decimal to binary, octal, and hexadecimal
def convert_decimal(num):
    binary = bin(num)    # Converts to binary (starts with '0b')
    octal = oct(num)     # Converts to octal (starts with '0o')
    hexadecimal = hex(num)  # Converts to hexadecimal (starts with '0x')

    return binary, octal, hexadecimal

# Input from user
decimal_number = int(input("Enter a decimal number: "))

# Call the function to convert the number
binary, octal, hexadecimal = convert_decimal(decimal_number)

# Print the results
print(f"Decimal: {decimal_number}")
print(f"Binary: {binary}")
print(f"Octal: {octal}")
print(f"Hexadecimal: {hexadecimal}")


# In[6]:


# Function to find ASCII value of a character
def ascii_value(character):
    return ord(character)

# Input from user
char = input("Enter a character: ")

# Check if the input is a single character
if len(char) == 1:
    # Find and print the ASCII value
    result = ascii_value(char)
    print(f"The ASCII value of '{char}' is {result}")
else:
    print("Please enter a single character.")


# In[7]:


# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main function to operate the calculator
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Get the user's choice
    choice = input("Enter choice (1/2/3/4): ")

    # Take input numbers based on the user's choice
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid Input! Please choose a valid operation.")

# Call the calculator function
calculator()


# In[ ]:





# In[ ]:





# In[ ]:




