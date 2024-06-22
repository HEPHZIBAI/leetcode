'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=set(s)
        t1=set(t)
        f=s1.union(t1)
        m=True
        f=list(f)
        if(len(s)!=len(t)):
            m=False

        if m:
            for i in f:
                if(s.count(i)!=t.count(i)):
                    m=False
        
        return m
        