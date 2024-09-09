import nltk

# Sample text for word tokenization
text1 = "I am writing this text to check if my word tokenization works perfectly fine. Thanks for checking out my code!"

# Tokenize text into words
words = nltk.word_tokenize(text1)

print("Printing Words : ")

# Print the list of tokenized words 
print(words)

# Sample text for sentence tokenization
text2 = "Oh! It is such a sunny day today. But I think it will rain after a few hours."

# Tokenize the text into sentences
sentences = nltk.sent_tokenize(text2)

print("Printing Sentences : ")

# Print the list of tokenize sentences 
print(sentences)
