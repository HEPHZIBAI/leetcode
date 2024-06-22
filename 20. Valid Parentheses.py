'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        s=s.strip()
        a=[]
        a.append(s[0])
        k=0
        b={'(':')' , '[':']' , '{':'}'}
        i=0
        while(i<len(s)):
            if a[k]in b.keys():
                if(b[a[k]]==s[i]):
                    del a[k]
                    k-=1
                else:
                    a.append(s[i])
                    k+=1
                i+=1
                if(len(a)==0 and i<len(s)):
                    i+=1
                    if(i<len(s)):
                        a.append(s[i])
                    k+=1
                    i+=1
            else:
                a.append(s[i])
                i+=1
                k+=1
        if(len(a)==1):
            f=True
        else:
            f=False
        return f