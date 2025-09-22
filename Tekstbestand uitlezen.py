f = open("uitleesbestand.txt", "r")
text = f.read()
print()
print(text)
if '.' in text:
    position = text.find('.')
    sentence = ""
    print(position)
    print(text[0:position+1])
print()