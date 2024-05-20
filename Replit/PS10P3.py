def discount(quantity,price,disrate):
   total = quantity * price
   discprice = price - (price * disrate)
   discamount = total - (discprice * quantity)
   return (discamount,discprice)

loop = input("Do you want to run this program? (y/n) ")
while loop == "y":
   quantity = int(input("Enter the quantity of the item  "))
   price = float(input("Enter the price of the item  "))
   rate = float(input("Enter the discount rate (in decimal form)  "))
   amountoff, newprice = discount(quantity,price,rate)
   print("The new price after the discount is $","{:.2F}".format(newprice)), "and the amount saved is $","{:.2F}".format(amountoff)
   loop = input("Do you want to run this program again? (y/n)")