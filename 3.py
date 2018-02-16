time = int(input())
min = time % 60
hours = int(((time - min)/60) % 12)
print(hours, min)
