class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        s = sorted(nums)
        z = []
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                for k in range(j+1, len(s)):
                        if s[i] + s[j] + s[k] == 0 :
                            m = [s[i], s[j], s[k]]
                            if m not in z:
                                z.append(m)
                            
        return z 
        
        
s = Solution()
x = [ -1, 0, 1, 2, -1, -4]
y= [[]]
y = s.threeSum(x)
print("hello")
print(y)
