#There are various built-in packages which we can directly use, 

# One of them is math, which provide all math related methods, like sqrt, pi

# First Pattern: To use math moudle, we have to import that in our module
import math # in this way we have imported the whole math module, and all methods inside it we can use

# To use sqrt from math module
math.sqrt(16) # this function will tell the sqrt of math


# Second Pattern: But if we want to use specific methods from any module, we can import specific methods instead of the whole module
from math import sqrt, pi

sqrt(16)

# Below are some math module functions we can directly use
math.pi # 3.14
math.inf # positive infinity
math.ceil(4.2) # rounds upward - output is 5
math.floor(4.9) # round downward - output is 4
math.trunc(4.99) # remove decimal part - output - 4
math.trunc(-4.99) # remove trunc
math.factorial(5) # tell the factorial of any number
math.gcd(24,36) # calculates gcd of two numbers

# other methods are 
###
# cuberoot - .cbrt(x)
# power - .pow(x)
# exponential e^x - .exp(x)
# log - .log()
# and more and more
# ###
#-------------------------------

# Module - random
import random

number = random.random() # gives a random float between 0.0 (inclusive) and 1.0 (exclusive)

number = random.randint(1, 10) # gives a random int value between 1 and 10, here 10 is inclusive

choice = random.choice(["apple", "banana","orange"]) # randomly element from the list will get selected

# there are more methods as well, I'm tired now to type everything here, just do chatgpt, btw sagar this side, if you are reading this

#--------------------------------
# Module - Date and Time

import datetime

today = datetime.date.today()
print(today)

# there are more built-in methods do chatgpt

#--------------------------------
# Module - os - operating system

import os
current_dir = os.getcwd()
print(current_dir)

#---------------------------------
# Module - json

import json

data = {
    "name": "Alice",
    "age": 30
    }

json_string = json.dumps(data)

#----------------------------------
import pandas as pd # here pd acts as an alisa, we don't need to write pandas again and again
df = pd.DataFrame(data)

# we are importing pandas, but it will show you yellow line or error while running the import line
# before running that line, make sure to install the pandas by running this command in the terminal - 'pip install pandas' , if pip not installed do that before running this command, ask chatgpt to install pip

# There are some terminal commands for installing packages

# 1. To install a package
# pip install requests

# 2. Install specific version
# pip install requests==2.28.0

# 3. Install multiple packages
# pip install pandas numpy matplotlib
