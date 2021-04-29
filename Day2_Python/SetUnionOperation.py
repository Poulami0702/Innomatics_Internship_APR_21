""" 
Question Link:
https://www.hackerrank.com/challenges/py-set-union/problem
 """

_, a = input(), set(input().split())
_, b = input(), set(input().split())
print(len(a.union(b)))
