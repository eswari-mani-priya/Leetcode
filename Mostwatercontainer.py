"""
Container with Most water

Given n non-negative integers where each integer represent the height of a vertical line on a chart. Find two lines,
which together with x-axis forms a container, that holds the highest amount of water and return the area of that water.
input: [1,8,6,2,5,4,8,3,7]
output: area = 7 * 7 (here we chose 8 and 7 lines) = 49
"""
from typing import List


class Solution:
    def maxArea(self,  height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        smaxArea = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            smaxArea = max(smaxArea, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return smaxArea


height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))