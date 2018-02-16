a = int(input())
b = int(input())
c = int(input())

if a < b and a < c:
    print(a, end=' ')
    if b < c:
        print(b, c, end='')
    else:
        print(c, b, end='')
elif b < a and b < c:
    print(b, end=' ')
    if a < c:
        print(a, c, end='')
    else:
        print(c, a, end='')
else:
    print(c, end=' ')
    if a < b:
        print(a, b, end='')
    else:
        print(b, a, end='')
