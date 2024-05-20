# Ensure to define or import the sales_forecast function before using it
def Myfunction(sales_forecast):
    control = str(input("Enter yes if you want to run the program, y if yes, n if no:  "))
    while control == "y":
        name = input("Enter your salesperson's name:  ")
        month = input("Enter the month:  ")
        month = month.lower()
        sales = float(input("The amount of sales made:  "))     
        forecasted_sales = sales_forecast(month, sales)     
        print("Salesperson " + name + " will sell {:2f}".format(forecasted_sales) + str(forecasted_sales))





#def Myfunction (import sales_forecast)

#control = str(input("Enter yes if you want to run the program, y if yes, n if no:  "))
#while control == "y":
#    name = input("Enter your salesperson's name:  ")
#    month = input("Enter the month:  ")
#    month = month.lower()
#    sales = float(input("The amount of sales made:  "))
#    forecasted_sales = sales_forecast(month,sales)
#    print("Salesperson " + name + " will sell ","{:2f}".format(forecasted_sales) + str(forecasted_sales))
  