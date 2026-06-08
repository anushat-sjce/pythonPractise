class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        maxarea = 0
        while(i <j):
            w = j-i
            h = min(height[i], height[j])
            area = w * h
            maxarea = max(area, maxarea)
            if(height[i] < height[j]):
                i = i +1
            else:
                j = j-1
        
        return maxarea
        
        

s = Solution()
height = [1,8,6,2,5,4,8,3,7]
ret = s.maxArea(height)
print(ret)
