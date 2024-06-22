'''
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

'''








class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
            a=[]
            m=len(mat)
            n=len(mat[0])
    
            if n==1 or m==1:
                for i in mat:
                    for j in i:
                        a.append(j)
                return a
            elif n==2:
                a.extend(mat[0])
                b=[]
                for i in mat[1:]:
                    a.append(i[1])
                    b.insert(0,i[0])
                return a+b
            else:
                if m%2!=0:
                    k=m//2+1
                else:
                    k=m//2
                for i in range(k):
                    for j in range(i,n-i):
                        a.append(mat[i][j])
                    for j in range(i+1,m-i):
                        a.append(mat[j][n-i-1])
                    for j in range(n-i-2,i-1,-1):
                        a.append(mat[m-i-1][j])
                    for j in range(m-i-2,i,-1):
                        a.append(mat[j][i])
                print(a[:m*n])
            
                return a[:m*n]