bdt=int(input("Enter birth date:"))
bmon=int(input("Enter birth month:"))

if bdt>=21 and bdt<=31 and bmon==3 or bdt>=1 and bdt<=19 and bmon==4: 
    print("zodiac is Aries")
elif bdt>=20 and bdt<=30 and bmon==4 or bdt>=1 and bdt<=20 and bmon==5: 
    print("zodiac is Taurus")
elif bdt>=21 and bdt<=31 and bmon==5 or bdt>=1 and bdt<=21 and bmon==6: 
    print("zodiac is Gemini")
elif bdt>=22 and bdt<=30 and bmon==6 or bdt>=1 and bdt<=22 and bmon==7: 
    print("zodiac is Cancer")
elif bdt>=23 and bdt<=31 and bmon==7 or bdt>=1 and bdt<=22 and bmon==8: 
    print("zodiac is Leo")
elif bdt>=23 and bdt<=31 and bmon==8 or bdt>=1 and bdt<=22 and bmon==9: 
    print("zodiac is Virgo")
elif bdt>=23 and bdt<=30 and bmon==9 or bdt>=1 and bdt<=22 and bmon==10: 
    print("zodiac is Libra")
elif bdt>=24 and bdt<=31 and bmon==10 or bdt>=1 and bdt<=21 and bmon==11: 
    print("zodiac is Scorpio")
elif bdt>=22 and bdt<=30 and bmon==11 or bdt>=1 and bdt<=21 and bmon==12: 
    print("zodiac is Sagittarius")
elif bdt>=22 and bdt<=31 and bmon==12 or bdt>=1 and bdt<=19 and bmon==1: 
    print("zodiac is Capricorn")
elif bdt>=20 and bdt<=31 and bmon==1 or bdt>=1 and bdt<=18 and bmon==2: 
    print("zodiac is Aquarius")
elif bdt>=19 and bdt<=29 and bmon==2 or bdt>=1 and bdt<=20 and bmon==3: 
    print("zodiac is Pisces")
else:
    print("Invalid input")