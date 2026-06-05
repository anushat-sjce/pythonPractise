class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(s)
        s = s.lower()
        no_space = s.replace(" ","")
        print(no_space)
        no_comma = no_space.replace(",","")
        no_space2 = no_comma.replace(" ","")
        no_space3 = no_space2.replace(":", "")
        print(no_space3)
        i= 0
        max = len(no_space3)
        print(max)
        j = max - 1
        while(i <j):
            if no_space3[i] != no_space3[j]:
                return False
            i = i +1
            j = j - 1
        return True
            
s = Solution()
#m = "MOOSO"
x = "A man, a plan, a canal: Panama"
y = " "
val = s.isPalindrome(y)
print(val)
