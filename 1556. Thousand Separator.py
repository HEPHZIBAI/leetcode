'''
Given an integer n, add a dot (".") as the thousands separator and return it in string format.

 

Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"
 

Constraints:

0 <= n <= 231 - 1
'''

class Solution:
    def thousandSeparator(self, n: int) -> str:
        a=str(n)
        b=""
        if len(a)>3:
            while(len(a)>3):
                m=len(a)-3
                b='.'+a[m:]+b
                a=a[:m]
            b=a+b
            return b
        else:
            return a