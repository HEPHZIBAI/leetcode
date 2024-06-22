'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k1: int) -> bool:
        a={}
        for i in range(len(nums)):
            if nums[i] not in a:
                a[nums[i]]=[i]
            else:
                a[nums[i]].append(i)
        k=a.keys()
        for i in k:
            for j in range(len(a[i])-1):
                if abs(a[i][j]-a[i][j+1])<=k1:
                    return True
        print(a)
        return False