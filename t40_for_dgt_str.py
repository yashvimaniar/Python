#write a program to count digits in given string 
line = input("Enter string:")
dgt=['0','1','2','3','4','5','6','7','8','9']
count = 0
for letter in line:
    if letter in dgt:
        count = count + 1
print("Total digit in string is:",count)