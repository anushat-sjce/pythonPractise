import re
from collections import Counter

#count words
passage = "Hello! welcome to Air Asia airplanes, to India from HongKong"
words = re.findall(r'\b\w+\b', passage.lower())
print(Counter(words))

#count letters
th = "banana"
print(Counter(th))
