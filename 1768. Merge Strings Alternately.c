/*
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
*/

char * mergeAlternately(char * w1, char * w2)
{
    int l=strlen(w1)>=strlen(w2)?strlen(w1):strlen(w2);
    int s=strlen(w1)>=strlen(w2)?strlen(w2):strlen(w1);
    char* m = (char*)malloc((2 * l +s) * sizeof(char));
    int n=0;
    printf("%d %d\n",l,s);
    for(int i=0;i<s;i++)
    {
        m[n]=w1[i];
        n++;
        m[n]=w2[i];
        n++;
        //printf("%c%c",w1[i],w2[i]);
    }
    if(s<strlen(w1))
    {
        while(s<strlen(w1))
        {
            m[n]=w1[s];
            n++;
            s++;
        }
    }
    else
    {
        while(s<strlen(w2))
        {
            m[n]=w2[s];
            n++;
            s++;
        }
    }
    m[n]='\0';
    printf("\n%s",m);
    return m;
}