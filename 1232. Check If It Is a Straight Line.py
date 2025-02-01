'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
'''

class Solution:
    def checkStraightLine(self, coor: List[List[int]]) -> bool:
        x1,y1=coor[0]
        x2,y2=coor[1]
        dx=x2-x1
        dy=y2-y1
        
        for i in range(1,len(coor)-1):
            x1,y1=coor[i]
            x2,y2=coor[i+1]
            x=x2-x1
            y=y2-y1

            if dx*y!=dy*x:
                return False
        
        return True
