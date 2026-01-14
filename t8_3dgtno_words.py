no=int(input("Enter 3 digit amount: "))   
last=no%10  
no1=no//10  
middle=no1%10   
first=no1//10   
words=['zero','one','two','three','four','five','six','seven','eight','nine']
print(words[first],words[middle],words[last])