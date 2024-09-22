'''
A password is said to be strong if it satisfies all the following criteria:

It has at least 8 characters.
It contains at least one lowercase letter.
It contains at least one uppercase letter.
It contains at least one digit.
It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
Given a string password, return true if it is a strong password. Otherwise, return false.

 

Example 1:

Input: password = "IloveLe3tcode!"
Output: true
Explanation: The password meets all the requirements. Therefore, we return true.
Example 2:

Input: password = "Me+You--IsMyDream"
Output: false
Explanation: The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.
Example 3:

Input: password = "1aB!"
Output: false
Explanation: The password does not meet the length requirement. Therefore, we return false.
 

Constraints:

1 <= password.length <= 100
password consists of letters, digits, and special characters: "!@#$%^&*()-+".

'''


class Solution:
    def strongPasswordCheckerII(self, passw: str) -> bool:
        if len(passw)<8:
            return False
        u=0
        l=0
        d=0
        c=0
        i=0
        for i in range(len(passw)-1):
            if passw[i]==passw[i+1]:
                return False
            if passw[i].islower():
                l=1
            elif passw[i].isupper():
                u=1
            elif passw[i] in "1234567890":
                d=1
            elif passw[i] in "!@#$%^&*()-+":
                c=1

        i=len(passw)-1
        if passw[i].islower():
            l=1
        elif passw[i].isupper():
            u=1
        elif passw[i] in "1234567890":
            d=1
        elif passw[i] in "!@#$%^&*()-+":
            c=1
    
        return u==1 and l==1 and d==1 and c==1