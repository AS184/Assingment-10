def calculate_total(quantity,price):
    global total
    global tax
    total = quantity * price
    tax = total * 0.07
    total += tax
    return()

loop = input("Do you want to run this program? (y/n):  ")
while loop == "y":
    quantity = int(input("Enter the quantity of the item:   "))
    price = float(input("Enter the price of the item:   "))
