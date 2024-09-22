'''
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
 

Example 1:

Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
Example 2:

Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].
 

Constraints:

1 <= matches.length <= 105
matches[i].length == 2
1 <= winneri, loseri <= 105
winneri != loseri
All matches[i] are unique.
'''


class Solution:
    def findWinners(self, m: List[List[int]]) -> List[List[int]]:
        a=[]
        z={}
        x=[]
        y=[]
        for i in m:
            if i[0] not in z:
                z[i[0]]=[1,1,0]
            else:
                z[i[0]][0]+=1
                z[i[0]][1]+=1
            if i[1] not in z:
                z[i[1]]=[1,0,1]
            else:
                z[i[1]][0]+=1
                z[i[1]][2]+=1
        h=list(z.keys())
        h.sort()
        print(h)
        for i in h:
            if(z[i][0]==z[i][1]):
                x.append(i)
            elif(z[i][2]==1):
                y.append(i)
            print(z[i])
        a.append(x)
        a.append(y)
        return a