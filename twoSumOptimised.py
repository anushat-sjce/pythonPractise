def twoSums(nums, target):
    seen = {}

    for index, value in enumerate(nums):
        complement = target - value

        if complement in seen:
            return [index, seen[complement]]

        seen[value] = index
