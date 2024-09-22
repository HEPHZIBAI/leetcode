'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30


'''


class Solution:
    def generate(self, num: int) -> List[List[int]]:
        a=[[1]]
        for i in range(1,num):
            a.append([1,1])
            print(a[i])
            h=a[i-1]
            k=1
            y=0
            while(len(a[i])<i+1):
                a[i].insert(k,h[y]+h[y+1])
                y+=1
                k+=1
        return a