import heapq

nums = [4,2,8,1, 13, 12, 19, 30, 43]
print(nums)
small = heapq.nsmallest(3, nums)

print(small)
