ci=lambda p,r,n,t:p*(1+r/n)**(n*t)-p

p = float(input("Enter Principal amount: "))
r = float(input("Enter Annual Interest Rate (in %): ")) / 100
n = int(input("Enter number of times interest is compounded per year: "))
t = float(input("Enter time in years: "))

res= ci(p,r,n,t)
print("Compound interest=",round(res,2))