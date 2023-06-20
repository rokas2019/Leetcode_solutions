from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        unique_nums.sort()  # Sort the unique numbers in ascending order

        for i in range(len(unique_nums)):
            nums[i] = unique_nums[i]  # Copy the unique numbers back to the original array

        return len(unique_nums)
