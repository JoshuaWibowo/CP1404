text = input("Text: ")
words = text.split(" ")
word_to_count = {word: 0 for word in words}
for word in words:
    word_to_count[word] += 1
sorted_values = sorted(word_to_count.items(), key=lambda x: x[0])
sorted_values = dict(sorted_values)
for key in sorted_values:
    print(f"{key:<10} : {sorted_values[key]:<}")
