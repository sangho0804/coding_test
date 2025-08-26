year = int(input())

c1 = (year % 4 == 0 and year % 100 != 0)
c2 = (year % 400 == 0)

out = 1 if (c1 or c2) else 0
print(out)