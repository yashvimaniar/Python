a=float(input("Enter first number:"))
b=float(input("Enter second number:"))

print("\n1 for Addition")
print("2 for Subtraction")
print("3 for Multiplication")
print("4 for Division")
no=int(input("\nEnter choice:"))

if no==1:
    res=a+b
    print("Addition=",res)
elif no==2:
    res=a-b
    print("Subtraction=",res)
elif no==3:
    print("Multiplication=",a*b)
elif no==4:
    print("Division=",a/b)
else:
    print("Invalid choice")