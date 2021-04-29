""" 
Question Link:
https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
 """

 def average(array):
    
    heights = set(array)
    averg = sum(heights) / len(heights)
    return averg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)