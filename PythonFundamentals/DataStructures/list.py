

age = 21
has_license = False

# list
my_list = ["Alice", 25, age, True, has_license]

# can access single elements from the lsit
name = my_list[0]
age = my_list[1]

has_license = my_list[-1]

# can slice or get elements in a range from the list
print(my_list[0:2]) # here element of index 0th and 1st will be printed from the list, 2nd index is excluded
print(my_list[-3:-1])

print(my_list[-2:])


# we can manipulate or replace the data of list with something else of our choice

my_list[0] = "Sagar"

# we can add the element inside the list using append, but the element will gets added at the end of the list
my_list.append("Alice")

# if we don't want to append any value in the end of list, we can do that by providing the index and value to insert method
my_list.insert(1, "Alice")

# we can remove any element from our list, if we know the value
my_list.remove("Alice")
my_list




