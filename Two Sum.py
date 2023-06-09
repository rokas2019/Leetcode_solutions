# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
# Example 1:
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because
# nums[0] + nums[1] == 9, we
# return [0, 1].
# Example
# 2:
#
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
# Example
# 3:
#
# Input: nums = [3, 3], target = 6
# Output: [0, 1]


class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i
        return []


l1 = [2,4,3]
l2 = [5,6,4]

ratio = 0.529
value1 = 1
value2 = 20
value3 = 5
dollartoone = value1 * ratio
onetodolar = value2 * ratio
print(f"cash :{onetodolar}")
print(f"Ones :{dollartoone}")
print(f"cigars now {value2 / value3}")


