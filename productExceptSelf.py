class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prod = 1
        j = 0
        final_res = []
        for i in range(len(nums)):
            prod = prod * nums[i]
        
        res = prod/nums[0]
        final_res.append(res)
        for i, value in enumerate(nums):
            print(f"{i} and {value}")
            if (j != i):
                res = prod/nums[i]
                final_res.append(res)
                j = j+1
    #    print(final_res)
        return final_res
        
s1 = Solution()
nums = [2,3,4]
x = s1.productExceptSelf(nums)
print(x)
