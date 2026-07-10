# Numbers
age = 25 # integeres
price = 1.99 # float

# We can apply basic math operations and store them in the variable, like this
# addition and subtraction
total = 10 + 5
change = 20-7

# multiplication and division
area = 6 * 4
half = 10 / 2

# powers
squared = 5 ** 2
cubed = 2 ** 3 

# Integer vs float division
# Regular division (always float), we use single /
result = 10 / 3 # 3.333 will be stored in the result
result = 10 // 3 # 3 will be stored in the result

# Strings, working with text
# Strings are text - any characters inside quotes. Python doesn't care if you use single or double quotes, just be consistent

name = "Sagar"
message = "Hello, world"

# Creating Strings
# Single quotes
first = "Python"

# Double quotes
second = "Python"

# You can write a long string or a paragraph and store it inside a variable 
my_long_string = """
Hi this is a long string
which I'm storing inside triple quotes
"""

# we can concatenate two strings together or using + 
first_name = "Sagar"
second_name = "Mehla"

full_Name = first_name + " " + second_name

full_Name

# we can add a string with continuous repition of same character n number of times
n = 10
long_dash = "-" * 10 
long_dash # output - ----------

print(full_Name)
print(long_dash)

# there is one more concept related to string that is - F String
string = "Hi there, my name is Dave!" # here the user name is hardcoded, even the person other then Dave runs this code will see this exact line
# what we can do is we can store user name is one string and inject that string in the above string at the place, where Dave is written
name = "Sagar"
# we have to write f in the starting of the line and the variable name insdie the curly braces which we want to inject
string = f"Hi there, my name is {name}!"

# Boolean
# Real world example of this can be that in real world customer service automation systems
# ai decide whether a ticked should be escalated to human or not , that status is stored in a variable with value either true or false
is_logged_in = True
is_admin = False
has_permission = True

# the above example is of direct assignment
#but we can assign true or false by performing any conditional operations

age = 18
can_vote = age >= 18 # True

score = 75
passed = score > 60 # True

# these operators like >= or > etc are called as comparison operators#Some of the examples are - 
#Equality
print(age >= 25)
print(age !=30)

#Greater/ Less than
print(age > 20)

print(age < 30)
print(age >= 25)

print(age <= 35)

