""" 
Question Link:
https://www.hackerrank.com/challenges/find-angle/problem
  """


import math

degree_sign= u'\N{DEGREE SIGN}'

AB = int(input())
BC = int(input())
hyp = math.pow(((AB*AB) + (BC*BC)), 0.5)

num = (BC*BC) + (hyp*hyp) - (AB*AB)
den = (2*(BC*hyp))
angle_C = math.degrees(math.acos(num/den))

print (str(int(round(angle_C))) + degree_sign)