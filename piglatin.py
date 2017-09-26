y = input("Enter a string")
word = y.lower()
pig = "ay"
first = word[0]
if first == ('a' or 'e' or 'i' or 'o' or 'u'):
    new_word = word + pig
    print (new_word)
else:
    new_word = word[1:] + first + pig
    print (new_word)