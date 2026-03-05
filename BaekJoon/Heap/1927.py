import sys
input = sys.stdin.readline

N = int(input())
arr = [0]

def heap_append(arr, x):
    arr.append(x)
    cur_index = len(arr) - 1

    while cur_index > 1 :
        parent = cur_index // 2
        if arr[cur_index] < arr[parent] :
            arr[cur_index], arr[parent] = arr[parent], arr[cur_index]

            cur_index = parent
        else : 
            break

def heap_search_and_remove(arr):
    # empty
    if len(arr) == 1 :
        return  0

    # not empty
    result = arr[1]
    rm = arr.pop()

    # only 1 element
    if len(arr) == 1:
        return result
    
    arr[1] = rm
    d = 1
    
        
    while True : 
        left = d * 2
        right = d * 2 + 1

        # no child
        if left > len(arr) - 1:
            break
        # only left child
        if right > len(arr) - 1 :
            if arr[d] > arr[left]:
                arr[d], arr[left] = arr[left], arr[d]
            break

        if arr[left] < arr[d] or arr[right] < arr[d] :
                        
            if arr[left] <= arr[right] :
                c_i = left
            else : 
                c_i = right

            arr[d], arr[c_i] = arr[c_i], arr[d]

            d = c_i
            
        else:
            break

    return result

ans = []
for _ in range(N):
    x = int(input())

    if x > 0 :
        heap_append(arr, x)
    
    elif x == 0 : 
        ans.append(heap_search_and_remove(arr))

for i in ans :
    print(i)


# claude

import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(heap, x)
    else:
        print(heapq.heappop(heap) if heap else 0)