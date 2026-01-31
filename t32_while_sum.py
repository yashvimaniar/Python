#write a program to make sum of all digits 
# like input : 12345 process = 1+2+3+4+5 = output : fifteen

no = int(input("Enter number: "))   # 12345
sm = 0

ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen',
         'sixteen','seventeen','eighteen','nineteen']
tens = ['', '', 'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

# sum of digits
while no > 0:
    rem = no % 10
    sm = sm + rem
    no = no // 10

# convert sum to words
if sm < 10:
    print(ones[sm])
elif 10 <= sm < 20:
    print(teens[sm - 10])
else:
    print(tens[sm // 10], ones[sm % 10])
