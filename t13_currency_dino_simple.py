amount = int(input("Enter amount: "))

n500 = amount //500
amount %= 500

n200 = amount // 200
amount %= 200

n100 = amount // 100
amount %= 100

n50 = amount // 50
amount %= 50

n20 = amount // 20
amount %= 20

n10 = amount // 10
amount %= 10

n5 = amount // 5
amount %= 5

n2 = amount // 2
amount %= 2

n1 = amount // 1

print("500 x", n500, "=", 500 * n500)
print("200 x", n200, "=", 200 * n200)
print("100 x", n100, "=", 100 * n100)
print("50  x", n50,  "=", 50 * n50)
print("20  x", n20,  "=", 20 * n20)
print("10  x", n10,  "=", 10 * n10)
print("5   x", n5,   "=", 5 * n5)
print("2   x", n2,   "=", 2 * n2)
print("1   x", n1,   "=", 1 * n1)
