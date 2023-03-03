word_keys = [el.lower() for el in input().split()]
defaults = 0

occurrences = dict.fromkeys(word_keys, defaults)
for word in word_keys:
    occurrences[word] += 1
for word, count in occurrences.items():
    if count % 2 != 0:
        print(word, end=" ")

