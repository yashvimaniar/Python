amt=int(input("Enter amount: "))
notes=[500,200,100,50,20,10,5,2,1]
for note in notes:
    cnt=amt//note
    if cnt>0:
        print(note,"x",cnt,"=",note*cnt)
        amt=amt%note
        