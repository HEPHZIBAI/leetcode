'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=0
        f=""
        l=strs[0]
        k=0
        while(k<len(l)):
            s=0
            for i in strs:
                if(k<len(i)):
                    if(l[k]==i[k]):
                        s+=1
                else:
                    break
            if(s==len(strs)):
                f+=l[k]
            else:
                break
            k+=1

        return f