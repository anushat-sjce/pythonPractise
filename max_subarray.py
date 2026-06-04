class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max = nums[0]
        cur_max = 0
        for i in range(len(nums)):
            cur_max = cur_max + nums[i]

            if max < cur_max:
                max = cur_max
            
        return max
        
s1 = Solution()
num = [5,4,-1,7,8]
num1 = [-1]
num2 = [-2,1,-3,4,-1,2,1,-5,4]
res = s1.maxSubArray(num1)
print(res)
