'''
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
 

Constraints:

0 <= low <= high <= 10^9
'''

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        s=0
        if low%2==0:
            low+=1
        '''for i in range(low,high+1,2):
            s+=1'''
        return ((high-low)//2)+1