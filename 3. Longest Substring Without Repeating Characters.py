'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=set(s)
        print(a)
        b=""
        i=0
        l=0
        while(i<len(s)):
            if(s[i] not in b):
                b+=s[i]
            else:
                h=b.index(s[i])
                if(h+1==len(b)):
                    b=s[i]
                else:
                    b=b[h+1:]+s[i]
            i+=1
            if(len(b)>l):
                l=len(b)
            print(b)

        if len(s)==1 or len(a)==len(s) or len(a)<l:
            return len(a)
        return l