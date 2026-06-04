class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == nums[i]:
                    return True
        
        return False
