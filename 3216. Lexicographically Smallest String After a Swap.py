'''
Given a string s containing only digits, return the 
lexicographically smallest string
 that can be obtained after swapping adjacent digits in s with the same parity at most once.

Digits have the same parity if both are odd or both are even. For example, 5 and 9, as well as 2 and 4, have the same parity, while 6 and 9 do not.

 

Example 1:

Input: s = "45320"

Output: "43520"

Explanation:

s[1] == '5' and s[2] == '3' both have the same parity, and swapping them results in the lexicographically smallest string.

Example 2:

Input: s = "001"

Output: "001"

Explanation:

There is no need to perform a swap because s is already the lexicographically smallest.

 

Constraints:

2 <= s.length <= 100
s consists only of digits.


'''

class Solution:
    def getSmallestString(self, s: str) -> str:
        i=0
        j=1
        while j<len(s):
            x=int(s[i])
            y=int(s[j])
            if ((x%2==0 and y%2==0) or (x%2!=0 and y%2!=0)) and x>y:
                s=s[:i]+s[j]+s[i]+s[j+1:]
                break
            i+=1
            j+=1
        return s