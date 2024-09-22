'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''

class Solution:
    def convert(self, s: str, n: int) -> str:
        a=[]
        k=0
        for i in range(n):
            a.append([])

        while(k<len(s)):
            for i in range(n):
                if(k>=len(s)):
                    break
                a[i].append(s[k])
                k+=1
            for i in range(n-2,0,-1):
                if(k>=len(s)):
                    break
                a[i].append(s[k])
                k+=1
        b=""
        for i in a:
            for j in i:
                b+=j
            #print(i)
        return b