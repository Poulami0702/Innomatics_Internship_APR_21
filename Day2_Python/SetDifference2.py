""" 
Question LinK:
https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
 """
_, a = input(), set(input().split())
_, b = input(), set(input().split())
print(len(a.symmetric_difference(b)))