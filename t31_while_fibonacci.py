n = int(input("Enter number of terms: "))

a = 0
b = 1
i = 0

while i < n:
    print(a, end=" ")
    
    temp = a + b
    a = b
    b = temp
    
    i=i+1
