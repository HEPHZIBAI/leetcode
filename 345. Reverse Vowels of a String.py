'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        a=""
        b=""
        k=0
        for i in s:
            if i in "aeiouAEIOU":
                a+=i
        
        a=a[::-1]

        for i in s:
            if i in "aeiouAEIOU": 
                b+=a[k]
                k+=1
            else:
                b+=i
        return b