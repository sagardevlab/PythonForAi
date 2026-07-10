name = "Sagar"

# we can find the length of any string
#using len

len(name) # output will be 5 as there are 5 characters in a string Sagar



#String methods

# changing case
text = "Python Programming"

print(text.lower()) # 'python programming'

print(text.upper()) # 'PYTHON PROGRAMMING'

print(text.title()) # 'Python Programming'

# cleaning strings
messy = "   sagar mehla    "
print(messy.strip()) # remove whitespaces from start and end

price = "$19.99"
print(price.strip("$")) # 19.99 , $ got removed from the string

# Finding and replacing
message = "I love Python programming with Python"

#check if something exists
print("Python" in message)
print(message.startswith("I"))
print(message.endswith("Python"))

# find position
print(message.find("Python"))
print(message.count("Python"))

# replace
new_message = message.replace("Python", "JavaScript")
print(new_message)

