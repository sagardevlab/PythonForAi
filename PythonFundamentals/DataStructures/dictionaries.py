# key value pairs

#declaration
person = {
    "name" : "Alice",
    "age" : 25,
    "city" : "New York"
}

# during creation of dict we use {}, but during retrieval of data we use [] square brackets

person["city"]

# we can replace the value of any key like that
person["name"] = "Sagar"

# so currently the person dictionary is having 3 keys, we can manually add the new key value pais as well
person["email"] = "sagar.dev.lab@gmail.com"
person["license"] = True

person

# we can remove any key as well from the dict

del person["license"]

person