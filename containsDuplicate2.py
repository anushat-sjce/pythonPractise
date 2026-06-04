class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = sorted(nums)
        y = set(nums)
        z = sorted(y)

        if len(x) == len(z): return False

        return True
