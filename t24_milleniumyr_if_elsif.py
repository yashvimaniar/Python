y=int(input("Enter a year: "))

if y<=0:
    print("Invalid year")
else:
    if y%1000==0:
        print(y,"is Millennium year")
    else:
        print(y,"is not Millennium year")