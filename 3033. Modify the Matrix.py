'''
Given a 0-indexed m x n integer matrix matrix, create a new 0-indexed matrix called answer. Make answer equal to matrix, then replace each element with the value -1 with the maximum element in its respective column.

Return the matrix answer.

 

Example 1:


Input: matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
Output: [[1,2,9],[4,8,6],[7,8,9]]
Explanation: The diagram above shows the elements that are changed (in blue).
- We replace the value in the cell [1][1] with the maximum value in the column 1, that is 8.
- We replace the value in the cell [0][2] with the maximum value in the column 2, that is 9.
Example 2:


Input: matrix = [[3,-1],[5,2]]
Output: [[3,2],[5,2]]
Explanation: The diagram above shows the elements that are changed (in blue).
 

Constraints:

m == matrix.length
n == matrix[i].length
2 <= m, n <= 50
-1 <= matrix[i][j] <= 100
The input is generated such that each column contains at least one non-negative integer.
'''


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=matrix[::]

        for i in range(len(matrix[0])):
            b=[]
            for j in range(len(matrix)):
                b.append(matrix[j][i])
            print(b)
            for j in range(len(matrix)):
                if matrix[j][i]==-1:
                    matrix[j][i]=max(b)
        return ans