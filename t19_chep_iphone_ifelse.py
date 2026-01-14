ind_prc=float(input("Enter iphone price in India (INR):"))
usa_prc=float(input("Enter iphone price in USA (USD):"))
exchange_rate=float(input("Enter exchange rate:"))

usa_ind_prc=usa_prc*exchange_rate

if usa_ind_prc < ind_prc:
    print("Buying iphone from USA is cheaper")
else:
    print("Buying iphone from India is cheaper")