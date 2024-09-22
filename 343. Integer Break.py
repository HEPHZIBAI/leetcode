'''
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 

Constraints:

2 <= n <= 58

'''

class Solution:
    def integerBreak(self, n: int) -> int:
        c=1
        if n<=3:
            return n-1
        while(n>=3):
            c*=3
            n-=3
            print(n)
        print(c)
        if n==1:
            c=(c//3)*4
            print(c)
        elif n==2:
            c*=2
        return c