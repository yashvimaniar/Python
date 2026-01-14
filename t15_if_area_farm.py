l1=int(input("Enter length of farm 1: "))
w1=int(input("Enter width of farm 1: "))

l2=int(input("Enter length of farm 2: "))
w2=int(input("Enter width of farm 2: "))

area1=l1*w1
area2=l2*w2

if area1>area2:
    print("Farm 1 is Bigger")
if area1<area2:
    print("Farm 2 is Bigger")
if area1==area2:
    print("Both farm are equal")
