x = int(input())
x2 = x
minim = x
while x != 0:
    if x > minim:
        continue
    else:
        minim = x
    x = int(input())
    x2 = x
print(x)

