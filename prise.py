time = int(input())
sec1 = time % 60
sec2 =  time % 60 // 10
min = (time - sec)%60
hour = ((time - min - sec)//3600) % 12
print(hour, min, sec)
