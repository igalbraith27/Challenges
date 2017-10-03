
message = input('Message: ')
key = int(input('Key (0 to 25): '))

eord = input('Encrypt or Decrypt: ')
eord = eord.lower()

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''
message = message.upper()

for x in message:
    if x in LETTERS:
        curr = LETTERS.find(x) 
        if eord == 'encrypt':
            curr = curr + key
        elif eord == 'decrypt':
            curr = curr - key
        if curr >= len(LETTERS):
            curr = curr - len(LETTERS)
        elif curr < 0:
            curr = curr + len(LETTERS)
        result = result + LETTERS[curr]
    else:
        result = result + x

print(result)