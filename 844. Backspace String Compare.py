'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        x=""
        y=""

        for i in s:
            if i!='#':
                x+=i
            else:
                x=x[:len(x)-1]
        
        print(x)

        for i in t:
            if i!='#':
                y+=i
            else:
                y=y[:len(y)-1]
        print(y)

        if x==y:
            return True
        else:
            return False