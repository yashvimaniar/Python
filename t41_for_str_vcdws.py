# write a program to count vowels, consonants, digits, words, and symbol in given list 

lst = ["Hello", "World!", "123", "Python3.8"]

vowels = 0
consonants = 0
digits = 0
words = 0
symbols = 0

i = 0
while i < len(lst):
    s = lst[i]
    j = 0
    while j < len(s):
        ch = s[j]
        if ch.isalpha():  # Letter
            if ch.lower() in 'aeiou':
                vowels = vowels + 1
            else:
                consonants = consonants + 1
        elif ch.isdigit():  # Digit
            digits = digits + 1
        else:  # Symbol
            symbols = symbols + 1
        j = j + 1
    words = words + 1  # Counting each element in list as a word
    i = i + 1

print(lst)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Words:", words)
print("Symbols:", symbols)
