# if-else
temperature = 25

if temperature > 25: 
    print("It's hot!")
else:
    print("It's nice weather!")

# if-else inside another if
has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Enjoy the movie!")
    else:
        print("Needs supervision!")
else:
    print("Please buy a ticket!")
# Nested if-else
score = 90
if score >= 90:
    print("A - Excellent!")
elif score >= 90:
    print("B - Good Job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")

# Mulitple conditions inside if-else using and, or, not

age = 25
has_license = True
#and
if age >=18 and has_license:
    print("You can drive!")
#or
weekend = True
holiday = False
if weekend or holiday:
    print("No work today!")
#reverse the condition using not
raining = True
if not raining:
    print("Let's go outside!")


