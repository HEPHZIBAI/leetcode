'''
You are given a 2D matrix grid of size m x n. You need to check if each cell grid[i][j] is:

Equal to the cell below it, i.e. grid[i][j] == grid[i + 1][j] (if it exists).
Different from the cell to its right, i.e. grid[i][j] != grid[i][j + 1] (if it exists).
Return true if all the cells satisfy these conditions, otherwise, return false.

 

Example 1:

Input: grid = [[1,0,2],[1,0,2]]

Output: true

Explanation:



All the cells in the grid satisfy the conditions.

Example 2:

Input: grid = [[1,1,1],[0,0,0]]

Output: false

Explanation:



All cells in the first row are equal.

Example 3:

Input: grid = [[1],[2],[3]]

Output: false

Explanation:



Cells in the first column have different values.

 

Constraints:

1 <= n, m <= 10
0 <= grid[i][j] <= 9
'''
class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i<len(grid)-1 and grid[i][j]!=grid[i+1][j]:
                    return False
                if j<len(grid[0])-1 and grid[i][j]==grid[i][j+1]:
                    return False
        return True