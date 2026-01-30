num = int(input("Enter a number: "))

if num <= 1:
    print("Neither composite nor prime")
else:
    i = 2
    is_composite = False
    while i <= num // 2:
        if num % i == 0:
            is_composite = True
            break
        i = i + 1

    if is_composite:
        print("Composite number")
    else:
        print("Not a composite number (Prime number)")
