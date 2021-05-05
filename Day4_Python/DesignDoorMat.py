
rows,columns = map(int,input().split())
middle = rows//2+1
for i in range(1,middle):
    center = (i*2-1)*".|." 
    print(center.center(columns,"-"))
print("WELCOME".center(columns,"-"))
for i in reversed(range(1,middle)):
    center = (i*2-1)*".|."
    print(center.center(columns,"-"))