"""
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

# This solution took 849ms. If I use list instead of dictionary I am getting 2400ms

# class Solution:
#     def longestSubstring(self, s):
#         if len(s) <= 1:
#             return len(s)
#         else:
#             max_length = 0
#             for i in range(0, len(s)+1):
#                 char_list = []
#                 cur_length = 0
#                 # print(max_length)
#                 for j in range(i, len(s)):
#                     if s[j] in char_list:
#                         break
#                     cur_length += 1
#                     char_list.append(s[j])
#                     max_length = max(max_length, cur_length)
#             return max_length


# This solution took 81ms
class Solution:
    def longestSubstring(self, s):
        if len(s) <= 1:
            return len(s)
        seenChars = {}
        L = 0
        R = 0
        longest = 0
        while (L < len(s)) and (R < len(s)):
            curChar = s[R]
            if curChar in seenChars:
                prevChar = seenChars[curChar]
                L = max(L, prevChar + 1)
            seenChars[curChar] = R
            longest = max(longest, R-L+1)
            R += 1
        return longest

sl = Solution()
print(sl.longestSubstring('abcabcdcd'))


