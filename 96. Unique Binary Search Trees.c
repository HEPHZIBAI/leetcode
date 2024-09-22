/*
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Example 1:
	Input: n = 3
	Output: 5

Example 2:
	Input: n = 1
	Output: 1
 

Constraints:
	1 <= n <= 19
*/
int numTrees(int n) 
{
    if(n==1 || n==0)
        return 1;
    else
    {
        int s=0;
        for(int i=1;i<=n;i++)
        {
            s+=numTrees(i-1)*numTrees(n-i);
        } 
        return s;
    } 
}