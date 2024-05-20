def square_footage(width,length,height):
   total = quantity * price
   discprice = price - (price * disrate)
   discamount = total - (discprice * quantity)
   return (discamount,discprice)

loop = input("Do you want to run this program? (y/n) ")
while loop == "y":
   length = int(input("Enter the length of the room  "))
   width = float(input("Enter the width of the room  "))
   height = float(input("Enter the height of the room  "))
   amountoff, newprice = discount(quantity,price,rate)
   print("The new price after the discount is $","{:.2F}".format(newprice)), "and the amount saved is $","{:.2F}".format(amountoff)
   loop = input("Do you want to run this program again? (y/n)")