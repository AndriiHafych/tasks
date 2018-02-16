a = int(input())
b = int(input())
c = int(input())

firstpart = b + b
kolpartii = int()
if a > c:
    print(firstpart)
elif c % a != 0:
    kolpartii = c // a + 1
    print(firstpart * kolpartii - b)
else:
    kolpartii = c // a
    print(firstpart * kolpartii)
