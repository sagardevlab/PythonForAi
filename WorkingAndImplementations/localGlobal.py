# In python, we have two types of variable , Local and Global

#Variable inside a function is a local variable and variable outside the function is global


#Global Variable
discount = 20

def calculate_total(price):

    #Local Variable
    tax_rate = 0.08
    discount = 10

    #Calculation
    tax = price * tax_rate
    final_price = price + tax - discount

    #print the final price
    print(f"Total: ${final_price}")

calculate_total(100)

discount
