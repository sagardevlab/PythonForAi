# immutable sequences

# use tuples for data that shouldn't change:
###
# For Example - 
# Coordinates (x , y)
# RGB colors (255 , 0 , 0)
# Database records
# Function return values
# ###

#Empty tuple
empty = ()

#Tuple with items
point = (3,5)
colors = ("red","green","blue")

#Single item tuple needs comma!
single = (42,) # Note the comma
not_tuple = (42) 

#Without parentheses (implicit)
coordinates = 10, 20