'''
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.


'''

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans=[]
        g={}
        k=words[0]

        for i in k:
            if i not in g:
                g[i]=0
            g[i]+=1

        for i in words:
            for j in set(i):
                if j in g:
                    k=i.count(j)
                    if k<g[j]:
                        g[j]=k
            for k in list(g.keys()):
                if k not in i:
                    del g[k]


        for i in list(g.keys()):
            for j in range(g[i]):
                ans.append(i)
                
        print(g)

        return ans