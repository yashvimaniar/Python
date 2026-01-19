y=int(input("Enter a year: "))

if y%1000==0:
    print(y,"is Millennium year")
elif y%1000!=0:
    print(y,"is not Millennium year")
else:
    print("Invalid input")