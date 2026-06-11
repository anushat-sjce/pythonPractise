from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mapM = Counter(magazine) 
        mapR = Counter(ransomNote)
       
        for char, count in mapR.items():
            if mapM[char] < count:
                return False
        return True
        
s = Solution()
ransomNote = "aaxb"
magazine = ""
ret = s.canConstruct(ransomNote, magazine)
print(ret)
        
