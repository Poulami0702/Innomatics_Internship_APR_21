""" 
Question Link:
https://www.hackerrank.com/challenges/python-lists/problem
 """

 n = int(input())
operations = [input().strip() for _ in range(n)]

list_ = []

commands = {
    'insert': lambda idx, ele: list_.insert(int(idx), int(ele)),
    'print': lambda: print(list_),
    'remove': lambda ele: list_.remove(int(ele)),
    'append': lambda ele: list_.append(int(ele)),
    'sort': lambda: list_.sort(),
    'pop': lambda: list_.pop(),
    'reverse': lambda: list_.reverse(),
}

for operation in operations:
    name, args = [i.strip() for i in (operation + ' ').split(' ', maxsplit=1)]
    command = commands.get(name)
    command(*args.split())
