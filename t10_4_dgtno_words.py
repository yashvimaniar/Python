no=int(input("Enter 4 digit amount: "))   #1234
last=no%10  #4
no1=no//10  #123
mid2=no1%10 #3  
no2=no1//10 #12 
mid1=no2%10  #2
first=no2//10  #1
words=['zero','one','two','three','four','five','six','seven','eight','nine']
print(words[first],words[mid1],words[mid2],words[last])