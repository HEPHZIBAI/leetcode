'''
You are given a string s and an integer k.

Determine if there exists a 
substring
 of length exactly k in s that satisfies the following conditions:

The substring consists of only one distinct character (e.g., "aaa" or "bbb").
If there is a character immediately before the substring, it must be different from the character in the substring.
If there is a character immediately after the substring, it must also be different from the character in the substring.
Return true if such a substring exists. Otherwise, return false.

 

Example 1:

Input: s = "aaabaaa", k = 3

Output: true

Explanation:

The substring s[4..6] == "aaa" satisfies the conditions.

It has a length of 3.
All characters are the same.
The character before "aaa" is 'b', which is different from 'a'.
There is no character after "aaa".
Example 2:

Input: s = "abc", k = 2

Output: false

Explanation:

There is no substring of length 2 that consists of one distinct character and satisfies the conditions.

 

Constraints:

1 <= k <= s.length <= 100
s consists of lowercase English letters only.
'''


class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        if (k==1 and len(s)==1) or (len(s)==k and len(set(s))==1) :
            return True
        
        for i in range(len(s)-k+1):
            x=s[i:i+k]
            if i>0 and i+k<len(s):
                print(x,s[i-1],s[i+k],len(set(x)),end="..")
            if len(set(x))==1:
                if (i>0 and i+k<len(s) and s[i-1]!=x[0] and s[i+k]!=x[0]) or (i+k>=len(s) and i>0 and s[i-1]!=x[0]) or (i<=0 and i+k<len(s) and s[i+k]!=x[0]):
                    return True    
            if i>0 and i+k<len(s):
                print(x,s[i-1],s[i+k],len(set(x)))          

        return False