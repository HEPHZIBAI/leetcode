'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

'''


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k=0
        l=0
        f=0

        while f<len(nums):
            k=0
            while f<len(nums) and nums[f]==1:
                k+=1
                f+=1

            while f<len(nums) and nums[f]==0:
                f+=1

            if k>l:
                l=k

        return l
            