

# question 2

def split_and_join(line):
    # write your code here
    x=line.split(" ")
    x='-'.join(x)
    return x

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)