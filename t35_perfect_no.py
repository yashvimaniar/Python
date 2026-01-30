num = int(input("Enter a number: "))

sum_of_divisors = 0
i = 1

while i < num:
    if num % i == 0:
        sum_of_divisors = sum_of_divisors + i
    i = i + 1

if sum_of_divisors == num:
    print("Perfect number")
else:
    print("Not a perfect number")
