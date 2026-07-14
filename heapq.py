import heapq

nums = [4,2,8,1, 13, 12, 19, 30, 43]
z = nums.sort()
print(z)
print(nums)
small = heapq.nsmallest(3, nums)

print(small[2])
largest = heapq.nlargest(4, nums)
print(largest[3])
