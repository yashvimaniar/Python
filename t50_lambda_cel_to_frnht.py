# Lambda function to convert Celsius to Fahrenheit
fahrenheit = lambda c: (c * 9/5) + 32
celsius = float(input("Enter temperature in Celsius: "))
res= fahrenheit(celsius)
print("Temperature in Fahrenheit =", round(res, 2))
