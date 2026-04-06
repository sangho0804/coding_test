# 1 - 2 sec remove / 2 - 1 sec assert
# min max failed reson
import sys


input = sys.stdin.readline

N, M, b = map(int, input().split())

land = [list(map(int, input().split())) for _ in range(N)]


result_min = 0
# case : min
land_min = min(map(min, land))
for i in range(N):
    for j in range(M):
        if land_min == land[i][j] :
            # print(land[i][j])
            continue
        diff_h = land[i][j] - land_min
        # print("test : ", diff_h)
        result_min += (diff_h * 2)

# case : max
    # b 가 많을 경우
    # b 가 적을 경우
result_max = 0

land_max = max(map(max, land))
init = 1
while init != 0:
    init = 0
    for i in range(N):
        for j in range(M):
            if land_max == land[i][j]:
                # print("same")
                continue

            if land_max < land[i][j]:
                diff_h =  land[i][j] - land_max
                result_max += (diff_h * 2)
                b += diff_h
                #print("remove")
                continue        
            
            diff_h = land_max - land[i][j]
            
            if diff_h > b :
                # print("init")
                land_max -= 1
                result_max = 0
                init = 1
                break
            
            else:
                # print("assert")
                result_max += (diff_h * 1)
                b -= diff_h
    

if result_max < result_min :
    print(result_max, land_max)
    # print("this max")
elif result_max == result_min :
    print(result_max, land_max)

else:
    print(result_min, land_min)
    # print("this min")


# cluade
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
h = []
for _ in range(N):
    h.extend(map(int, input().split()))

best_time = float('inf')
best_height = 0

for target in range(257):
    remove = 0
    place = 0
    
    for height in h:
        if height > target:
            remove += height - target
        else:
            place += target - height
    
    if B + remove < place:
        continue
    
    time = remove * 2 + place
    
    if time < best_time or (time == best_time and target > best_height):
        best_time = time
        best_height = target

print(best_time, best_height)