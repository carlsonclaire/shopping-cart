products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]
# based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

   Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# SHOPPING CART INPUTS

total_price = 0
selected_ids = []

while True:
    selected_id = input("Please enter a product ID (1-20), type DONE when you have finished entering products:")
    if selected_id == "DONE":
        break
    elif selected_id == ("1") or selected_id == ("2") or selected_id == ("3") or selected_id == ("4") or selected_id == ("5") or selected_id == ("6") or selected_id == ("7") or selected_id == ("8") or selected_id == ("9") or selected_id == ("10") or selected_id == ("11") or selected_id == ("12") or selected_id == ("13") or selected_id == ("14") or selected_id == ("15") or selected_id == ("16") or selected_id == ("17") or selected_id == ("18") or selected_id == ("19") or selected_id == ("20"):
        selected_ids.append(selected_id)
    else:
      print("Oops, invalid product ID, please enter DONE if complete or a product ID 1-20.")


# SHOPPING CART OUTPUTS
print("------------------------------------")
print("CLAIRE'S GROCERY STORE")
print("FIND US AT WWW.CCGROCERIES.COM | 888-888-8888")
print("------------------------------------")
import datetime
now = datetime.datetime.now()
print ("CHECKOUT ON",(now.strftime("%Y-%m-%d %H:%M")))
print("------------------------------------")
print("YOUR PURCHASE:")
for selected_id in selected_ids:
    matching_products = [item for item in products if str(item["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    total_price = (total_price + matching_product["price"])
    print("+ " + matching_product["name"] + " " + str(to_usd(matching_product["price"])))
print("------------------------------------")
print("SUBTOTAL: ")
print(str(to_usd(total_price)))
print("------------------------------------")
Taxes = total_price * .0875
print("NEW YORK SALES TAX @ 8.75%:")
print(str(to_usd(Taxes)))
print("------------------------------------")
Total = Taxes + total_price
print("TOTAL:")
print(str(to_usd(Total)))
print("------------------------------------")
print("THANKS FOR SHOPPING AT CLAIRE'S, SEE YOU NEXT TIME!")


# Date/time source
# https://www.w3resource.com/python-exercises/python-basic-exercise-3.php

# Multiplication source
# https://pythonguides.com/multiply-in-python/#:~:text=In%20python%2C%20to%20multiply%20number,%E2%80%9D%20*%20%E2%80%9D%20to%20multiply%20number.&text=After%20writing%20the%20above%20code,used%20to%20multiply%20the%20number.
