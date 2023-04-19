"""
Given an array of integers, write a function to move all 0's to the end while maintaining the relative order of the
other elements
Input:
array = [0, 1, 0, 3, 12]
Expected Output:
output = [1, 3, 12, 0, 0]
"""


class Solution:
    def moveZeros(self, nums):
        """Here fetching all non-zero elements to the front of array then filling the remaining with 0's"""
        j = 0
        n = len(nums)
        for i in nums:
            if i != 0:
                nums[j] = i
                j += 1
        for x in range(j, n):
            nums[x] = 0
        return nums


nums = [0, 1, 0, 3, 12]
print(Solution().moveZeros(nums))
