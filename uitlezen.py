# Open and read the file
with open("README.md", "r") as f:
    text = f.read()

# Print the full text (optional)
print("\nFull text:")
print(text)
print()

# Split the text into sentences using '.'
sentences = text.split('.')

# Go through each sentence and print it separately
for sentence in sentences:
    sentence = sentence.strip()  # remove spaces/newlines
    if sentence:  # skip empty strings
        print(sentence + ".")
