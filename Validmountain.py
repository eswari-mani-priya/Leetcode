"""
Given an array of integers, return True if following conditions are fulfilled
1. Length of array is bigger than or equal to 3
2. There exists some index i such that:
a[0] < a[1] < ...a[i]
a[i] > a[i+1] >....a[a.size - 1]
"""
from typing import List

# class Solution:
#     def validMountain(self, arr):
#         increasing = 0
#         decreasing = 0
#         if len(arr) < 3:
#             return False
#         for i in range(len(arr)):
#             if i + 1 < len(arr):
#                 if arr[i] == arr[i + 1]:
#                     return False
#                 elif (arr[i] > arr[i + 1]) and increasing == 0:
#                     return False
#                 elif (arr[i] < arr[i + 1]) and decreasing == 0:
#                     increasing += 1
#                 elif (i + 1 < len(arr)) and (arr[i] > arr[i + 1]) and increasing > 0:
#                     decreasing += 1
#                 elif (i + 1 < len(arr)) and (arr[i] < arr[i + 1]) and decreasing > 0:
#                     return False
#         if increasing > 0 and decreasing > 0:
#             return True
#         else:
#             return False

class Solution:
    def validMountain(self,  arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        i = 1
        while (i < len(arr)) and (arr[i] > arr[i-1]):
            i += 1
        if (i == 1) or (i == len(arr)):
            return False
        while (i < len(arr)) and (arr[i] < arr[i-1]):
            i += 1
        return i == len(arr)


input = [0, 2, 1, 2]
print(Solution().validMountain(input))