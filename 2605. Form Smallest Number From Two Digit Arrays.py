'''
Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least one digit from each array.
 

Example 1:

Input: nums1 = [4,1,3], nums2 = [5,7]
Output: 15
Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have.
Example 2:

Input: nums1 = [3,5,2,6], nums2 = [3,1,7]
Output: 3
Explanation: The number 3 contains the digit 3 which exists in both arrays.
 

Constraints:

1 <= nums1.length, nums2.length <= 9
1 <= nums1[i], nums2[i] <= 9
All digits in each array are unique.
'''

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        k=sum(nums1)+sum(nums2)
        nums1.sort()
        nums2.sort()
        if len(nums1)>len(nums2):
            for i in nums2:
                if i in nums1:
                    return i
        else:
            for i in nums1:
                if i in nums2:
                    return i

        x=str(nums1[0])+str(nums2[0])
        y=str(nums2[0])+str(nums1[0])
        if x<y:
            return int(x)

        return int(y)