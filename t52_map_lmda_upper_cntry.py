#write a program to convert list that has mixed case countries names into uppercase countries name  using lambdacountries = ["India", "USA", "bRaZiL", "CaNaDa", "GERMANY"]
countries = ["India", "USA", "bRaZiL", "CaNaDa", "GERMANY"]
list1=[]

lowercase_cntry = map(lambda x: x.upper(), countries)
list1.append(countries)

print("Original List:", countries)
print("Lowercase List:",list(lowercase_cntry))
