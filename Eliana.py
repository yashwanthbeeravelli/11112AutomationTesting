import sys
# import pytest

number1=float(input("Enter first number sum: "))
number2=float(input("Enter second number sum: "))
def sum(a,b):
    sum=a+b
    return sum
print("Result is: ",sum(number1,number2))

# #========================================================

number1=float(input("Enter first number to div: "))
number2=float(input("Enter second number to div: "))
def division(a,b):
    div=a/b
    return div
print("Result is: ",division(number1,number2))

# ===========================================================

number1=float(input("Enter first number to sus: "))
number2=float(input("Enter second number to sus: "))
def sustration(a,b):
    sus=a-b
    return sus
print("Result is: ",sustration(number1,number2))

# ===========================================================

number1=float(input("Enter first number to mul: "))
number2=float(input("Enter second number to mul: "))
def multiplication(a,b):
    mul=a*b
    return mul
print("Result is: ",multiplication(number1,number2))

