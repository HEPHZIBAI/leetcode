'''
Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
 

Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
Example 2:

Input: s = "aaaa"

Output: 2

Explanation:

The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 

Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.

'''

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        for i in range(len(s),1,-1):
            for j in range(len(s)-i+1):
                k=s[j:j+i]
                m=0
                for l in set(k):
                    if k.count(l)>2:
                        m=1
                        break
           
                if m==0:
                    return len(k)

                
        return 0