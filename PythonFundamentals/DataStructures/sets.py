# Work with unique collections

# Sets are collections that only store unique values. They automatically remove duplicates

# Creating sets - we can create sets two ways: with set() or with curly braces {} (but only when it has values)
empty_set = set() # can add values as well
fruits = set(["apple", "banana", 5])
fruits

# using curly braces
numbers = {} # we can also add values inside it
numbers = {1, 3, 5, 6, 6} # we added 6 twice, but when we print the set, single 6 will be printed
numbers

#can add a list inside the set to remove duplicates
scores = [85, 90, 85, 90, 90]
unique_scores = set(scores)
unique_scores

# basic operations - 
colors = {"red", "green"}

#add items
colors.add("green")

#remove items
colors.remove("blue") # error if not found
colors.discard("green")

#check membership
if "Red" in colors:
    print("Red is available")
