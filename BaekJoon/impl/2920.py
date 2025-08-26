# hard coding 
# import sys

# rd = sys.stdin.readline
# w = sys.stdout.write

# n = rd().strip()

# if n == '1 2 3 4 5 6 7 8':
#     print('ascending')
# elif n == '8 7 6 5 4 3 2 1':
#     print('descending')
# else :
#     print('mixed')


# sort coding 
import sys

rd = sys.stdin.readline
w = sys.stdout.write

n = list(map(int, rd().split()))

if n == sorted(n):
    print('ascending')
elif n == sorted(n, reverse=True):
    print('descending')
else :
    print('mixed')

