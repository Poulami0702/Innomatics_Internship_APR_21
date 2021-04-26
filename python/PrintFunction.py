""" 
Print the list of integers from 1 through n as a string, without spaces.

Sample Input 0

3
Sample Output 0

123
 """
n = int(input())
for i in range(1,n+1):
    print(i, end="")
