'''
Given an integer num, return a string of its base 7 representation.

 

Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"
 

Constraints:

-107 <= num <= 107

'''

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return '0'
        k=""
        t=num
        if num<0:
            num*=-1

        while (num>0):
            r=num%7
            print(num,r)
            num//=7
            k+=str(r)
        
        

        if t<0:
            return '-'+str(k)[::-1]

        return str(k)[::-1]