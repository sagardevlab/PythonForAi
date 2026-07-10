# Arithmentic operations 
a = 5
b = 7
c = a + b

# there are some shortcuts for arithmetic operators like
score = 10
score = score + 5 # instead of writing this, we can write the addition in shortcut form
score += 5

# instead of + we can use - , * , / , %

c = a // b # it is a floor division, which rounds down

# Comparison Operators
print(c == 12) # checks whether value of c is equal to 12 or not

# other comparison operators can be != , > , < , <= , >= 


# Logical Operators
# there are three logical operators which are and , or , not

age = 25
has_license = True

# and - means both condition must be true
can_drive = age >= 16 and has_license

# or - means at least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"

# not - means reverses the value
is_adult = age >=18
is_child = not is_adult
