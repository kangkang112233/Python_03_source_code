# Import standard library
import os
import sys

# Import third-party library
# import numpy as np
# import pandas as pd

# # Import local module
# import my_module

# Using alias for a module
import datetime as dt


# Example function using imports
def print_current_directory():
    print("Current Directory:", os.getcwd())


def print_python_version():
    print("Python Version:", sys.version)


def print_current_date():
    print("Current Date:", dt.datetime.now())


# Call the example functions
print_current_directory()
print_python_version()
print_current_date()
