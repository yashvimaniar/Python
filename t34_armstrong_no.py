num = int(input("Enter a number: "))

temp = num
sum = 0
count = 0

# Count number of digits
dgt = num
while dgt > 0:
    count = count + 1
    dgt = dgt // 10

# Calculate Armstrong sum
while temp > 0:
    rem = temp % 10
    sum = sum + (rem ** count)
    temp = temp // 10

if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
