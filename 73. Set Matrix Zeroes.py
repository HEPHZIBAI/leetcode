'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
	Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
	Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
	Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
	Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 
Constraints:
	m == matrix.length
	n == matrix[0].length
	1 <= m, n <= 200
	-231 <= matrix[i][j] <= 231 - 1
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r=len(matrix)
        c=len(matrix[0])
        h=0
        z=[]


        for i in range(r):
            k=[]
            for j in range(c):
                k.append(matrix[i][j])
            z.append(k)
        
        for i in range(r):
            for j in range(c):
                if(matrix[i][j]==0):
                    h=1
                    for x in range(0,i,1):
                        if(matrix[x][j]!=0 ):
                            if(z[x][j]==2):
                                z[x][j]=0
                            matrix[x][j]=2
                    for x in range(i+1,r,1):
                        if(matrix[x][j]!=0):
                            if(z[x][j]==2):
                                z[x][j]=0
                            matrix[x][j]=2
                    for x in range(0,j,1):
                        if(matrix[i][x]!=0):
                            if(z[i][x]==2):
                                z[i][x]=0
                            matrix[i][x]=2
                    for x in range(j+1,c,1):
                        if(matrix[i][x]):
                            if(z[i][x]==2):
                                z[i][x]=0
                            matrix[i][x]=2
         
        print()
        if(h):
            for i in range(r):
                for j in range(c):
                    if(matrix[i][j]==2 and z[i][j]!=2):
                        matrix[i][j]=0
                   