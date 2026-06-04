class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        s = nums
      #  m = []
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                for k in range(j+1, len(s)):
                        if s[i] + s[j] + s[k] == 0 :
                            m = [s[i], s[j], s[k]]
                            y.append(m)
                            print(y)
        return y 
        
        
s = Solution()
x = [ -1, 0, 1, 2, -1, -4]
y= [[]]
y = s.threeSum(x)
print("hello")
print(y)
