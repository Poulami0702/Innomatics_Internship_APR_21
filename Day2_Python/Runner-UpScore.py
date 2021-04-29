""" 
Quention URL 
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
 """

 import sys

def runnerUp(arr):
    # maxScore and runnerUpScore
    maxScore = -sys.maxsize-1
    runnerUpScore = -sys.maxsize-1
    
    for score in arr:
        if score > maxScore:
            runnerUpScore = maxScore
            maxScore = score
        elif score > runnerUpScore and score < maxScore:
            runnerUpScore = score
            
    return runnerUpScore

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    print(runnerUp(arr))