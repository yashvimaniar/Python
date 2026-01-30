#write a program to convert all negative values into positive values in the same list 
list=[12,-45,7,-3,89,-22,0,34,-9,56]
list1=[]
for item in list:
    if item>0:
        list1.append(item)
    else:
        item=item*-1
        list1.append(item)
print(list)
print("\nafter convert...")
print(list1)



