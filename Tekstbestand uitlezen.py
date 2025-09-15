f = open("README.md", "r")
text = f.read()
print()
print(text)
if '.' in text:
    print(position = text.find('.') )
print()