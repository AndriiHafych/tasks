a = int(input())
b = int(input())
c = int(input())


if a == b and a == c:
    print('3')
elif a == b and a != c or a == c and a != b:
    print('2')
elif c == a and c != b or c == b and c != a:
    print('2')
elif b == a and b != c or b == c and b != a:
    print('2')
else:
    print('0')
