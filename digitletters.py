iner = input()
d={"DIGITS":0, "LETTERS":0}
for x in iner:
    if x.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print ("LETTERS", d["LETTERS"])
print ("DIGITS", d["DIGITS"])