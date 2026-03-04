import sys
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split())) 

cnt = 0


for i in (arr):
    if is_prime(i) == True:
        cnt += 1

print(cnt)
