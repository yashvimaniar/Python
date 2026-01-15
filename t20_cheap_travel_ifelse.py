dis=float(input("Enter distance from Ahmedabad to Delhi: "))
petrol_prc=float(input("Enter petrol price: "))
mileage=float(input("Enter car mileage: "))
other_cost=float(input("Enter other car expenses: "))

train_cost=float(input("Enter price of 1st class train ticket: "))

tot_petrol=dis/mileage
car_cost=(tot_petrol*petrol_prc)+other_cost

print("\nTotal cost of Travel by Car: ",car_cost)
print("Total cost of Travel by Train: ",train_cost)

if car_cost<train_cost:
    print("\nTravelling by Car is cheaper")
else:
    print("\nTravelling by Train is cheaper")