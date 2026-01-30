# write a program to sum of all the values in tuple and also calculate average 
num=(45,98,2,56,23,4,7,11,95,40,34)
tot=0
cnt=0
for no in num:
    cnt=cnt+1
    tot=tot+no 
avg=tot/cnt
print("Sum of all values:",tot)
print("Average:",avg)