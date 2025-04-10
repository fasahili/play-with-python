import string

text = input("Enter a string: ")
no_punct = ''.join(char for char in text if char not in string.punctuation)
print("Without punctuations:", no_punct)
