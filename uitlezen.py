def uitlezen(
    bestand    
):
    f = open(bestand, "r")
    text = f.read()
    print()
    print(text)
    if '.' in text:
        position = text.find('.')
        sentence = ""
        print(position)
        importtekst = text[0:position+1]
        return importtekst
    print()