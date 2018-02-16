b = int(input())
a = int(input())
maxim = int()
counter = 0
if a > b:
    maxim = a
else:
    maxim = b
while a != 0:
    if a < maxim:
        a = int(input())
    elif a == maxim:
        counter += 1
        a = int(input())
    else:
        maxim = a
        counter = 1
        a = int(input())
if counter == 0:
    print('1')
else:
    print(counter)
