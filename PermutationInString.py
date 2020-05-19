"""
567. Permutation in String
Medium

1378

54

Add to List

Share
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

"""

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        cs1 = Counter(s1)
        print(cs1)
        cs2 = dict()
        for i in range(len(s2)):
            cs2[1] = Counter(s2[i:(i+l)])
            if(cs2[1] == cs1):
                return True
            
        return False
