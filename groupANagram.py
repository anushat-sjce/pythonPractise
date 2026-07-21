from collections import defaultdict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = {}

for words in strs:
    key = ''.join(sorted(words))
   # print(key, words)
    
    if key not in groups:
        groups[key] = []
    else:
        groups[key].append(words)
        
print(groups)
