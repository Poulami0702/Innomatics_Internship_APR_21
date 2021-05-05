def print_rangoli(size):
    # your code goes here
    import string
    alphabet = string.ascii_lowercase
    rows = (size*2) - 1
    width = (rows*2) - 1
    s = alphabet[:size]
    for i in range(1, size+1):
        r = s[::-1][:i]
        print('-'.join(r+r[:i-1][::-1]).center(width, '-'))

    for i in range(size-1, 0, -1):
        r = s[::-1][:i]
        print('-'.join(r+r[:i-1][::-1]).center(width, '-'))
if __name__ == '__main__':
     int(input())
     print_rangoli(n)