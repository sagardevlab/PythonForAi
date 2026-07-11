# We can return values to the caller of the function

def calculate_price(price):
    price *= 0.8
    return price 

finalPrice = calculate_price(50)

# We can return multiple values as well

def simple_function():
    numbers = [1, 2, 3, 4, 5]
    first_number = numbers[0]
    last_number = numbers[-1]

    return first_number, last_number

first_number, last_number = simple_function()