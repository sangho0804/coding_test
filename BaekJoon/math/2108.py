# my code
# import sys
# from collections import Counter
# rd = sys.stdin.readline
# w = sys.stdout.write

# n = int(rd())
# arr = []

# for _ in range(n):
#     arr.append(int(rd()))

# arr.sort()

# counter = Counter(arr).most_common()
# if len(counter) > 1 and counter[0][1] == counter[1][1]:
#     mode = counter[1][0]  
# else:
#     mode = counter[0][0]
    

# print(round(sum(arr) / n))
# print(arr[ n // 2])
# print(mode)
# print(arr[n-1] - arr[0])


# gpt code
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

# 1. 산술평균 (소수점 이하 첫째 자리에서 반올림)
mean = round(sum(nums) / n)

# 2. 중앙값
nums.sort()
median = nums[n // 2]

# 3. 최빈값
counter = Counter(nums).most_common()
# counter = [(값, 빈도), ...] 내림차순 정렬됨
if len(counter) > 1 and counter[0][1] == counter[1][1]:
    mode = counter[1][0]  # 두 번째로 작은 값
else:
    mode = counter[0][0]

# 4. 범위
_range = nums[-1] - nums[0]

# 출력
print(mean)
print(median)
print(mode)
print(_range)