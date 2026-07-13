from collections import Counter

word = "bbangalore"
count = Counter(word)
print(count)

for i in word:
    if count[i] == 1:
        print(i)
        exit()
