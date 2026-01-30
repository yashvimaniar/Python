# Program to find day of the week using if-elif

d = int(input("Enter day: "))
m = int(input("Enter month: "))
y = int(input("Enter year: "))

# Adjust month and year for January and February
if m == 1:
    m = 13
    y = y - 1
elif m == 2:
    m = 14
    y = y - 1

k = y % 100
j = y // 100

h = (d + (13 * (m + 1)) // 5 + k + (k // 4) + (j // 4) + 5 * j) % 7

# Using if-elif to print day
if h == 0:
    print("Saturday")
elif h == 1:
    print("Sunday")
elif h == 2:
    print("Monday")
elif h == 3:
    print("Tuesday")
elif h == 4:
    print("Wednesday")
elif h == 5:
    print("Thursday")
elif h == 6:
    print("Friday")
