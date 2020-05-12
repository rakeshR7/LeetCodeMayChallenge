"""
You are given a sorted array consisting of only integers where every element appears exactly twice, 
except for one element which appears exactly once. Find this single element that appears only once.

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left , right = 0, len(nums)-1
        while(left<right):
            mid = left + (right-left)//2
            even = (right-mid)%2 == 0
            if nums[mid] == nums[mid-1]:
                if even:
                    right = mid-2
                else:
                    left = mid+1
            elif nums[mid] == nums[mid+1]:
                if even:
                    left = mid+2
                else:
                    right = mid-1
            else:
                return nums[mid]
        return nums[left]
