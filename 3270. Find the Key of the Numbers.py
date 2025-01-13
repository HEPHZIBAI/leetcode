'''
You are given three positive integers num1, num2, and num3.

The key of num1, num2, and num3 is defined as a four-digit number such that:

Initially, if any number has less than four digits, it is padded with leading zeros.
The ith digit (1 <= i <= 4) of the key is generated by taking the smallest digit among the ith digits of num1, num2, and num3.
Return the key of the three numbers without leading zeros (if any).

 

Example 1:

Input: num1 = 1, num2 = 10, num3 = 1000

Output: 0

Explanation:

On padding, num1 becomes "0001", num2 becomes "0010", and num3 remains "1000".

The 1st digit of the key is min(0, 0, 1).
The 2nd digit of the key is min(0, 0, 0).
The 3rd digit of the key is min(0, 1, 0).
The 4th digit of the key is min(1, 0, 0).
Hence, the key is "0000", i.e. 0.

Example 2:

Input: num1 = 987, num2 = 879, num3 = 798

Output: 777

Example 3:

Input: num1 = 1, num2 = 2, num3 = 3

Output: 1

 

Constraints:

1 <= num1, num2, num3 <= 9999

'''

class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1=str(num1)
        while len(num1)<4:
            num1='0'+num1

        num2=str(num2)
        while len(num2)<4:
            num2='0'+num2

        num3=str(num3)
        while len(num3)<4:
            num3='0'+num3

        s=min(num1[0],num2[0],num3[0])+min(num1[1],num2[1],num3[1])+min(num1[2],num2[2],num3[2])+min(num1[3],num2[3],num3[3])
        return int(s)
