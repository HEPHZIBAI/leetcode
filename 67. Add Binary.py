'''
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a1=0
        x=len(a)-1
        b1=0
        y=len(b)-1
        f=0
        while(x>=0):
            a1+=(pow(2,f))*int(a[x])
            f+=1
            x-=1
        f=0
        while(y>=0):
            b1+=(pow(2,f))*int(b[y])
            #print(b1,end=" ")
            f+=1
            y-=1
        z=a1+b1
        q=""
        while(z>0):
            q+=str(z%2)
            z//=2
        #print(z)
        if(len(q)==0):
            return("0")
        return q[::-1]