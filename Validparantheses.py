"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


# class Solution:
#     def isValid(self, s: str) -> bool:
#         if len(s) % 2 != 0:
#             return False
#         open_paren = set('({[')
#         matches = {('(', ')'), ('[', ']'), ('{', '}')}
#         stack = []
#         for i in s:
#             if i in open_paren:
#                 stack.append(i)
#             else:
#                 if len(stack) == 0:
#                     return False
#                 last_open = stack.pop()
#                 if (last_open, i) not in matches:
#                     return False
#         return len(stack) == 0


class Solution:
    def isValid(self, s: str)-> bool:
        if len(s) % 2 != 0:
            return False
        matches = {('(', ')'), ('[', ']'), ('{', '}')}
        for i in range(0, len(s), 2):
            if (s[i], s[i+1]) not in matches:
                return False
        return True

#Testcase1
s = "([])"
data = Solution().isValid(s)
print(data)