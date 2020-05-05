"""Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
"""

class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        while i <= num:
            i = i << 1
            print(i)
        return (i - 1) ^ num
        

        
