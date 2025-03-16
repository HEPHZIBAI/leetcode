'''
Initially, you have a bank account balance of 100 dollars.

You are given an integer purchaseAmount representing the amount you will spend on a purchase in dollars, in other words, its price.

When making the purchase, first the purchaseAmount is rounded to the nearest multiple of 10. Let us call this value roundedAmount. Then, roundedAmount dollars are removed from your bank account.

Return an integer denoting your final bank account balance after this purchase.

Notes:

0 is considered to be a multiple of 10 in this problem.
When rounding, 5 is rounded upward (5 is rounded to 10, 15 is rounded to 20, 25 to 30, and so on).
 

Example 1:

Input: purchaseAmount = 9

Output: 90

Explanation:

The nearest multiple of 10 to 9 is 10. So your account balance becomes 100 - 10 = 90.

Example 2:

Input: purchaseAmount = 15

Output: 80

Explanation:

The nearest multiple of 10 to 15 is 20. So your account balance becomes 100 - 20 = 80.

Example 3:

Input: purchaseAmount = 10

Output: 90

Explanation:

10 is a multiple of 10 itself. So your account balance becomes 100 - 10 = 90.

 

Constraints:

0 <= purchaseAmount <= 100

'''

class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount>=5 and purchaseAmount<15:
            return 90
        elif purchaseAmount>=15 and purchaseAmount<25:
            return 80
        elif purchaseAmount>=25 and purchaseAmount<35:
            return 70
        elif purchaseAmount>=35 and purchaseAmount<45:
            return 60
        elif purchaseAmount>=45 and purchaseAmount<55:
            return 50
        elif purchaseAmount>=55 and purchaseAmount<65:
            return 40
        elif purchaseAmount>=65 and purchaseAmount<75:
            return 30
        elif purchaseAmount>=75 and purchaseAmount<85:
            return 20
        elif purchaseAmount>=85 and purchaseAmount<95:
            return 10
        elif purchaseAmount>=95:
            return 0
        

        return 100