# write a program to count odd and even number in numeric list
list=[45,98,2,56,23,4,7,11,95,40,34]
cnt=0
cnt1=0
for no in list:
    if no%2==0:
        cnt=cnt+1
    else:
        cnt1=cnt1+1
print("\nTotal Even number:",cnt)
print("Total odd number:",cnt1)