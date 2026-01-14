no=int(input("Enter 3 digit amount: "))   #123

f=no//100   #1
n1=no%100   #23
mid=n1//10  #2
l=n1%10     #3

ones=['','one','two','three','four','five','six','seven','eight','nine']
tens=['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
teens=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']

print("no in Words: ",ones[f],"hundred ", end="")
if n1>=10 and n1<20:
    print(teens[n1-10])
else:
    print(tens[mid],ones[l])