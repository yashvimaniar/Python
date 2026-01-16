s1=float(input("Enter first subject mark:"))
s2=float(input("Enter second subject mark:"))
s3=float(input("Enter third subject mark:"))
s4=float(input("Enter fourth subject mark:"))
s5=float(input("Enter fifth subject mark:"))

tot=s1+s2+s3+s4+s5
per=tot/5

print("\nTotal marks of 5 subject:",tot)
print("Percentage:",per)

if per>=90 and per<=100:
    print("Grade:A+")
elif per>=80 and per<90:
    print("Grade:A")
elif per>=70 and per<80:
    print("Grade:B")
elif per>=60 and per<70:
    print("Grade:C")
elif per>=50 and per<60:
    print("Grade:D")
elif per<50:
    print("Need to improve")
else:
    print("Invalid input")