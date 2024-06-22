/*
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

 

Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.
*/

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def leap(y):
            if (y%4==0 and y%100!=0) or y%400==0 and y%100==0:
                return 1
            else:
                return 0
        s=0
       
        date1=date1.split('-')
        date2=date2.split('-')

        y1=int(date1[0])
        m1=int(date1[1])
        d1=int(date1[2])

        y2=int(date2[0])
        m2=int(date2[1])
        d2=int(date2[2])

        if y1==y2:
            if m1==m2:
                s+=abs(d1-d2)
        elif y1<y2:
            if m1==2:
                if leap(y1):
                    s+=29-d1
                else:
                    s+=28-d1
            elif m1<=7 and m1%2==0:
                s+=30-d1
            elif m1<=7 and m1%2!=0:
                s+=31-d1
            elif m1>7 and m1%2==0:
                s+=31-d1
            else:
                s+=30-d1
            for i in range(m1+1,13):
                if i==2:
                    if leap(y1):
                        s+=29
                    else:
                        s+=28
                elif i<=7 and i%2==0:
                    s+=30
                elif i<=7 and i%2!=0:
                    s+=31
                elif i>7 and i%2==0:
                    s+=31
                else:
                    s+=30
            for i in range(y1+1,y2):
                if leap(i):
                    s+=366
                else:
                    s+=365
            for i in range(1,m2):
                if i==2:
                    if leap(y2):
                        s+=29
                    else:
                        s+=28
                elif i<=7 and i%2==0:
                    s+=30
                elif i>7 and i%2==0:
                    s+=31
                elif i<=7 and i%2!=0:
                    s+=31
                else:
                    s+=30
            s+=d2
        else:
            if m2==2:
                if leap(y2):
                   s+=29-d2
                else:
                    s+=28-d2
            elif m2<=7 and m2%2==0:
                s+=30-d2
            elif m2<=7 and m2%2!=0:
                s+=31-d2
            elif m2>7 and m2%2==0:
                s+=31-d2
            else:
                s+=30-d2
            print(s)
            for i in range(m2+1,13):
                if i==2:
                    if leap(y2):
                        s+=29
                    else:
                        s+=28
                elif i<=7 and i%2==0:
                    s+=30
                elif i<=7 and i%2!=0:
                    s+=31
                elif i>7 and i%2==0:
                    s+=31
                else:
                    s+=30
            print(s)
            for i in range(y2+1,y1):
                if leap(i):
                    s+=366
                else:
                    s+=365
            for i in range(1,m1):
                if i==2:
                    if leap(y1):
                        s+=29
                    else:
                        s+=28
                elif i<=7 and i%2==0:
                    s+=30
                elif i<=7 and i%2!=0:
                    s+=31
                elif i>7 and i%2==0:
                    s+=31
                else:
                    s+=30
            
            s+=d1
        return s