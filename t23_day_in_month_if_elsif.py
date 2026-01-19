mon=int(input("Enter month number:"))

if mon==1 or mon==3 or mon==5 or mon==7 or mon==8 or mon==10 or mon==12:
    print("this month has 31 days")
elif mon==2:
        print("this month has 28 or 29 days")
else:
    print("this month has 30 days")