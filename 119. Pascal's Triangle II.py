'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33

'''

class Solution:
    def getRow(self, num: int) -> List[int]:
        a=[[1]]
        for i in range(1,num+1):
            a.append([1,1])
            print(a[i])
            h=a[i-1]
            k=1
            y=0
            while(len(a[i])<i+1):
                a[i].insert(k,h[y]+h[y+1])
                y+=1
                k+=1
        print(a)
        return a[-1]