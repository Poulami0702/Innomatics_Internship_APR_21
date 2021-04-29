""" 
Question Link:
https://www.hackerrank.com/challenges/py-check-subset/problem
 """

 for _ in range(int(input())):
    x, a, z, b = input(), set(input().split()), input(), set(input().split())
    print(a.issubset(b))