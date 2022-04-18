text = input("Text: ")
words = text.split(" ")
word_to_count = {word: 0 for word in words}
for word in words:
    word_to_count[word] += 1
