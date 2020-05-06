"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Example:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        note = collections.Counter(s)
        j = 0
        for i in s:
            if note[i] == 1:
                return j
            j = j+1
        return -1
                
