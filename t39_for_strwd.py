# write a program to count words in given string 
line = input("Enter string:")
count = 0
c1=0
for letter in line:
    if letter==' ':
        c1=c1+1
    else:
        count = count + 1
print("Total words in string is:",count," and space in string is:",c1)