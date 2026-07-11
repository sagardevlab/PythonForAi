# we can define function using def
# code should be indented
def greet():
    print("Hello World")

# below is the code to call the above method and execute all the code written inside that method
greet()

# we can add any logic inside functions, can do any calculations and all
def check_weather():
    temperature = 16
    if temperature > 25:
        print("It's hot")
    else:
        print("It's Nice weather")

check_weather()

# we can provide parameters to the function
def greet(name):
    print(f"Hello {name}")

greet("Sagar")
# or
greet(name = "XYZ")

# multiple parameters can be passed

def greet(firstname, lastname):
    print(f"Hello {firstname} {lastname}")

greet("Sagar", "Mehla")

# so if we have two parameters but one contains a default value and other not, then the non default value will come first
def greet(lastname, firstname = "Sagar"): # here firstname is default value so it will come after last name in the parameters
    print(f"Hello {firstname} {lastname}")

greet("Mehla")
