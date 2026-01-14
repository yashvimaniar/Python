hr=int(input("Enter hour:"))

if hr<12:
    print(hr,"AM")

if hr==12:
    print(hr,"PM")

if hr>12 and hr<24:
    hr=hr-12
    print(hr,"PM")

if hr==24:
    hr=hr-12
    print(hr,"AM")

if hr>24:
    print("Invalid input")


