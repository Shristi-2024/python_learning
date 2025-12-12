# Count word frequency in a paragraph
paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("\nWord Frequency:")
for word, count in word_freq.items():
    print(f"{word}: {count}")