'''
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.
 

Constraints:

1 <= name.length, typed.length <= 1000
name and typed consist of only lowercase English letters.
'''


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        a=[]
        b=[]
        i=0
        k=0
        if len(name)>len(typed):
            return False
        while(i<len(name)):
            x=[]
            u=name[i]
            while(i<len(name) and name[i]==u):
                x.append(name[i])
                i+=1
            a.append(x)

        i=0

        while(i<len(typed)):
            x=[]
            u=typed[i]
            while(i<len(typed) and typed[i]==u):
                x.append(typed[i])
                i+=1
            b.append(x)

        if len(a)!=len(b):
            return False

        for i in range(len(a)):
            if len(a[i])>len(b[i]):
                return False
            elif (a[i][0]!=b[i][0]):
                return False
        print(a)
        print(b)
        return True