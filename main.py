import os
from read import *
from write import *
from sell import *
from purchase import *
from display import *
from operations import *
import datetime
# print display message
print("\n")
print("\n")
print("\t \t \t \t \t Ash Laptop Land")
print("\n")
print("\t \t \t \t\t Kupondol,Lalitpur " )
print("\t \t \t \t\t Phone No:9851045654 ")
print("\n")
print("--------------------------------------------------------------------------
--------------------------------")
print("\t \t \t \t Welcome to the system : Hope you have a wonderful day")
print("--------------------------------------------------------------------------
--------------------------------")
print("\n")
flag = True
while flag:
print("----------------------------------------------------------------------
-------------------------------------")
print("Here are some options for you to carry out the necessary system
operations:")
print("\n")
print("Press 1 to Display the Laptops ")
print("Press 2 to Sell the laptop to customer")
print("Press 3 to Purchase from the manufacturer")
print("Press 4 to Exit from the system")
print("\n")
print("----------------------------------------------------------------------
-------------------------------------")
print("\n")



#try except
try:
user_input = int(input("Enter the option to continue: "))
except:
print("Please enter a valid option from the menu")
print("\n")
else:
print("\n")
if user_input == 1:
display(laptop_dict)
elif user_input == 2:
sell(laptop_dict)
elif user_input == 3:
purchase(laptop_dict)
elif user_input == 4:
print("Thank you for using the system, have a good day!")
flag = False
else :
print("The option you are trying to choose doesn't exist.Please enter

valid option number")