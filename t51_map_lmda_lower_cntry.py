#write a program to convert list that has mixed case countries names into lowercase countries name  using lambda
countries = ["India", "USA", "bRaZiL", "CaNaDa", "GERMANY"]
list1=[]

lowercase_cntry = map(lambda x: x.lower(), countries)
list1.append(countries)

print("Original List:", countries)
print("Lowercase List:",list(lowercase_cntry))
