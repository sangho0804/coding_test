# strip -> 앞뒤 공백 제거
S = input().strip()

# alphabet 수 26개
pos = [-1] * 26

for i, ch in enumerate(S):
    # ord ascii code
    idx = ord(ch) - ord('a') 
    if pos[idx] == -1:       
        pos[idx] = i

print(" ".join(map(str, pos)))