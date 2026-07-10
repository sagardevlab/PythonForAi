# Comments are the lines which python ignores while running the .py file

# any line starting with # is a comment in python
print("Comments are ignored and only this line is written in the terminal") # we can add comment after the end of python statement


# if we have to write comment again and again for multiple lines, we can use triple hash tags like this ### and end with ###


###
# This is a 
# multi line comment
# which is starting with triple hashtags and 
# ending with triple hashtags
# ###


#Note : Good comments explain WHY, not WHAT:
# like the below example

subtotal = 5
#Good: Explains why
#Using 1.0625 because sales tax in CA is 6.25%
total = subtotal * 1.0625

#Bad: States the obvious
#Multiply subtotal by 1.0625
total = subtotal * 1.0625
