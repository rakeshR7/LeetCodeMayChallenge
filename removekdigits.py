"""Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
     # check if we need to do any processing
		# if we have to remove all elements, we can simply return '0'
        if len(num) == k:
            return '0'

        # store digits we want to keep in a list so we can easily add and remove them
        result = []
        for n in num:
            # remove the last element in result while we have k > 0 and values in result
            # and the current value is less than the last value in result
            while k and result and n < result[-1]:
                result.pop()
                k -= 1
                
            # add current value
            result.append(n)

        # if we still have elements to remove (k > 0), delete the last k elements
        if k:
            del result[-k:]

        # create string from list
        result = ''.join(result)

        # remove leading 0s
        result = result.lstrip('0')

        # return result if the string is not empty and 0 otherwise
        return result if result else '0'       
            
        
        
        
        
