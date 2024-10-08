from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1, length):
                if nums[i] == 0 and nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for i in range(len(nums)):
            if nums[i] != 0 :
                nums[l], nums[i] = nums[i], nums[l]
                l += 1