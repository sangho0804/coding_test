# my code 52400kb 224 ms
import sys
rd = sys.stdin.readline
w = sys.stdout.write


N, M = map(int, rd().split())

arr = {}

for i in range(1, N+1):
    poket_name =  rd().strip()

    arr[poket_name] = i

ans = []
name_list = list(arr.keys())

for i in range(M):
    quiz = rd().strip()

    try:
        quiz = int(quiz)
        ans.append(name_list[quiz-1])
    except:
        ans.append(arr[quiz])


w("\n".join(str(x) for x in ans))


# gpt code 52644kb 164 ms
import sys
rd = sys.stdin.readline
w = sys.stdout.write

N, M = map(int, rd().split())

# 1번부터 N번까지 인덱스로 바로 접근하려고 더미("") 하나 추가
num2name = [""] * (N + 1)
name2num = {}

for i in range(1, N + 1):
    name = rd().strip()
    num2name[i] = name
    name2num[name] = i

out = []
for _ in range(M):
    q = rd().strip()
    if q.isdigit():                 # 숫자 → 이름
        out.append(num2name[int(q)])
    else:                           # 문자 → 번호
        out.append(str(name2num[q]))

w("\n".join(out))
