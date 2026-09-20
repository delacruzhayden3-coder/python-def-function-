# This def function is used to calculate the total price of two items.
def calculate_total(price1, price2):
    total = price1 + price2
    return total


# Call/invoke the function
item1 = 100
item2 = 150

total_price = calculate_total(item1, item2)

print("Item 1 Price:", item1)
print("Item 2 Price:", item2)
print("Total Price:", total_price)
