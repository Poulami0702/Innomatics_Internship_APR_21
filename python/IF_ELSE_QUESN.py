""" Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Sample Input 0
3
Sample Output 0
Weird
Explanation 0
is odd and odd numbers are weird, so print Weird.

Sample Input 1
24
Sample Output 1
Not Weird
Explanation 1
 and  is even, so it is not weird. """

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if (n%2!=0):
        print('Weird')
    else:
        if (n>=2 and n<=5):
            print('Not Weird')
        elif (n>=6 and n<=20):
            print('Weird')
        else:
            print('Not Weird')
