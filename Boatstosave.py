"""
Given an array people and an integer limit. People array is an array of people's weights. People[i] is weight of ith
person and Each boat can carry at most limit. Each boat carries at most 2 people at the same time, given that their
weight sum is at most limit. Return the minimum number of boats required to carry all people in the array
People: [1, 2]
Limit : 3
Ans : 1
"""


class Solution:
    def boatsToSave(self, people, limit):
        sorted(people)
        highP = len(people) - 1
        lowP = 0
        boats = 0
        while highP >= lowP:
            if people[highP] + people[lowP] <= limit:
                boats += 1
                highP -= 1
                lowP += 1
            else:
                boats += 1
                highP -= 1
        return boats


people = [2, 3, 1, 3]
limit = 4
print(Solution().boatsToSave(people, limit))


