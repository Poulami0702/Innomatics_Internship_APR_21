def merge_the_tools(string, k):
    # your code goes here
    m=0
    res=[]
    for i in range(k,len(string) + 1, k):
        l=list(string[m:i])
        m += k
        for o in l:
            if o not in res:
                res.append(o)
        for j in res:
            print(j,end="")
        res.clear()
        print()
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)