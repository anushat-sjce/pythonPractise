class Solution:
    def isPalindrome(self, s: str) -> bool:
        i= 0
        max = len(s)
        print(max)
        j = max - 1
        while(i <j):
            if s[i] != s[j]:
                return False
            i = i +1
            j = j - 1
        return True
            
s = Solution()
m = "MOOSO"
val = s.isPalindrome(m)
print(val)
