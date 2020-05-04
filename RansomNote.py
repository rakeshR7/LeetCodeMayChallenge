"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; 
otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = collections.Counter(ransomNote)
        mag = collections.Counter(magazine)
     
        for i in note:
            if i not in mag.keys() or note[i]>mag[i] :
                return False
            
        return True
                
                
        
