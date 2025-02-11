'''
You are given a string s and a pattern string p, where p contains exactly one '*' character.

The '*' in p can be replaced with any sequence of zero or more characters.

Return true if p can be made a 
substring
 of s, and false otherwise.

 

Example 1:

Input: s = "leetcode", p = "ee*e"

Output: true

Explanation:

By replacing the '*' with "tcod", the substring "eetcode" matches the pattern.

Example 2:

Input: s = "car", p = "c*v"

Output: false

Explanation:

There is no substring matching the pattern.

Example 3:

Input: s = "luck", p = "u*"

Output: true

Explanation:

The substrings "u", "uc", and "uck" match the pattern.

 

Constraints:

1 <= s.length <= 50
1 <= p.length <= 50 
s contains only lowercase English letters.
p contains only lowercase English letters and exactly one '*'


'''


class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        k=p.index('*')
        left=p[:k]
        right=p[k+1:]
        if left not in s or right not in s:
            return False
        if (p[0]=='*' and right in s) or (p[-1]=='*' and left in s):
            return True

        

        li=s.index(left)
        s=s[li+len(left):]
        print(s)
        if right not in s:
            return False

        return True