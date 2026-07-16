def longestSubstringKDistinct(s, k):
    left = 0
    freq = {}
    max_len = 0

    for right, ch in enumerate(s):
        # Line 1: Add current character
        freq[ch] = freq.get(ch, 0) + 1

        while len(freq) > k:
            # Line 2: Remove left character
            
            freq[s[left]] -= 1 

            # Line 3: Delete if frequency becomes 0
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        # Line 4: Update answer
        max_len = max(max_len, right - left +1)
        
    return max_len

s ="eceba"
k = 3

x = longestSubstringKDistinct(s, k)
print(x)
