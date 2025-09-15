f = open("README.md", "r")
text = f.read()
print()
print(text)
if '.' in text:
    position = text.find('.')
    print(position)
print()