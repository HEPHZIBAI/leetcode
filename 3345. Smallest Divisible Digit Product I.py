'''
You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.

 

Example 1:

Input: n = 10, t = 2

Output: 10

Explanation:

The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.

Example 2:

Input: n = 15, t = 3

Output: 16

Explanation:

The digit product of 16 is 6, which is divisible by 3, making it the smallest number greater than or equal to 15 that satisfies the condition.

 

Constraints:

1 <= n <= 100
1 <= t <= 10
'''

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        temp1=n
        m=0
        while(m==0):
            temp2=temp1
            p=1
            while(temp1>0):
                p*=(temp1%10)
                temp1//=10

            if p%t==0:
                m=1
                n=temp2
            else:
                temp1=temp2+1

        
        return n