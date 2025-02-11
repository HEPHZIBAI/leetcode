'''
You are given a string s consisting of lowercase English letters. Your task is to find the maximum difference between the frequency of two characters in the string such that:

One of the characters has an even frequency in the string.
The other character has an odd frequency in the string.
Return the maximum difference, calculated as the frequency of the character with an odd frequency minus the frequency of the character with an even frequency.

 

Example 1:

Input: s = "aaaaabbc"

Output: 3

Explanation:

The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
The maximum difference is 5 - 2 = 3.
Example 2:

Input: s = "abcabcab"

Output: 1

Explanation:

The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
The maximum difference is 3 - 2 = 1.
 

Constraints:

3 <= s.length <= 100
s consists only of lowercase English letters.
s contains at least one character with an odd frequency and one with an even frequency.
'''


class Solution:
    def maxDifference(self, s: str) -> int:
        g1={}
        g2={}

        for i in set(s):
            k=s.count(i)
            if k%2==0:
                g1[k]=i
            else:
                g2[k]=i

        x=list(g1.keys())
        y=list(g2.keys())
        
        return max(y)-min(x)