class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right =len(s)
        max_len = 0
        char_set = set()
        
        for right in range(len(s)):
            while(s[right] in char_set):
                char_set.remove(s[left])
                left =left +1 
                
            char_set.add(s[right])
            max_len = max(max_len, right-left +1)
            
        #print(char_set)
        return max_len
        
        
s = Solution()
m = "abcdabcdbbcad"
ret = s.lengthOfLongestSubstring(m)
print(ret)
