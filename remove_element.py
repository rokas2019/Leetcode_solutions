from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int):
        while val in nums:
            nums.remove(val)



class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i