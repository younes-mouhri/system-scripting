# CNET 334 - System Scripting
# Lab 5 - Python Modules
# Author: Younes Mouhri

import datetime
import math_operations


def main():
    # Get two numbers from the user
    a, b = input("Enter 2 numbers: ").split()
    a, b = float(a), float(b)

    # Call the function from our custom module
    print("Using the module math_operations.py: ", end="")
    math_operations.add(a, b)

    # Display the current date and time
    date = datetime.datetime.now()
    print("Today:", date)


main()
