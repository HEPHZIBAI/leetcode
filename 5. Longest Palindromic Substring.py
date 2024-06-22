'''
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ml=1
        mat=[]
        b=""
        if len(s)==1:
            return s
        for i in s:
            a=[]
            for j in s:
                a.append(0)
            mat.append(a)
        for i in range(n):
            mat[i][i]=1
        for i in range(n-1):
            if s[i]==s[i+1]:
                mat[i][i+1]=1
                ml=2
                b=s[i]+s[i+1]
        
        for i in range(3,n+1):
            for j in range(0,n-i+1):
                if s[j]==s[i+j-1] and mat[j+1][i+j-2]:
                    mat[j][j+i-1]=1
                    if i>len(b):
                        ml=i
                        b=s[j:i+j]
        if ml==1:
            return s[0]
        return b